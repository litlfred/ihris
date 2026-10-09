#!/usr/bin/env python3
"""Ingest the Moodle course backup 'iHRIS Administrator - Level I' into library/ihris-admin-course/.

The source is a Moodle 1.9.9 course backup (moodle.xml + course_files/), uploaded by the
owner (uploads/ihris-admin-course/, git-ignored, pinned by manifest.json). The backup states
no licence. Its author, the folio owner, stated on 2026-10-09 that it is CC BY 4.0, attributed
to IntraHealth International; the declaration (ihris-admin-course.json) records that.

What is written depends on the declaration's `licence` (AGENTS.md rule 4):

- `licence: null`: STRUCTURE ONLY. course.json and course.md list the course by path and
  heading: sections, modules, lesson page titles, resource links, question counts, files.
- a `stated` licence or the owner's `permission`: the content as well. Section summaries
  (sections/), one Markdown file per module with content (modules/: lesson pages, html
  resources, quiz questions with their answers, questionnaire questions with their choices,
  introductions), the transcripts' text (transcripts/, extracted with `antiword -w 0`) and
  the course's images (images/), with the image links in the text rewritten to them.

Deterministic, in order:

1. Verify the zip against manifest.json (size, md5 AND sha256). Refuse on a mismatch.
2. Read it with zipfile, in memory. The input is treated as untrusted: member paths must be
   relative with no `..`; sizes and compression ratios are capped; moodle.xml is refused if
   it declares a DOCTYPE or an ENTITY (no entity expansion), then parsed with ElementTree.
   HTML from it is parsed with BeautifulSoup and reduced to a small set of tags and
   attributes (no script, style, iframe, event handler or inline style survives) before
   it is converted to Markdown with markdownify. An embedded YouTube player becomes a link.
3. Refuse a backup that holds people: INFO/DETAILS/USERS must be `none` and every module
   type's USERINFO `false` (so no users, posts, attempts, responses or user entries).
4. Record the course, the backup, the sections in order and each section's modules in
   course order (joined to their module record by type and instance). Every module record
   must be placed in exactly one section, or the tool stops.
5. Inventory every regular file in the zip: path, bytes, sha256, media type (a fixed table),
   and what it is published as (an image, a transcript's text) or null. The slide audio is
   inventoried only: it is not committed, for its size.
6. Check the totals against the manifest's `expect`. Refuse on any difference.
7. Remove every e-mail address from what is written (counted in `redactions`); the
   certificate's settings, which name a contact address, are never read.
8. Write course.json (ihris-moodle-course/v1), course.md, manifest.jsonld and, with a
   licence, sections/, modules/, transcripts/ and images/ (each emptied first, so nothing
   stale survives).

  python3 -I src/tools/ingest_moodle_course.py   # needs beautifulsoup4, markdownify and antiword
"""
import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UP = os.path.join(ROOT, "uploads", "ihris-admin-course")
OUT = os.path.join(ROOT, "library", "ihris-admin-course")
ENTRY = "library/ihris-admin-course"
MANIFEST = "uploads/ihris-admin-course/manifest.json"
DECL = f"{ENTRY}/ihris-admin-course.json"
CONTENT_DIRS = ("sections", "modules", "transcripts", "images")

MAX_MEMBERS = 5000
MAX_MEMBER_BYTES = 64 * 1024 * 1024
MAX_TOTAL_BYTES = 512 * 1024 * 1024
MAX_RATIO = 200  # uncompressed / compressed, per member

MEDIA = {".xml": "application/xml", ".mp3": "audio/mpeg", ".gif": "image/gif", ".png": "image/png",
         ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".doc": "application/msword", ".pdf": "application/pdf",
         ".html": "text/html", ".htm": "text/html", ".txt": "text/plain", ".swf": "application/x-shockwave-flash",
         ".ppt": "application/vnd.ms-powerpoint", ".zip": "application/zip"}
IMAGE_TYPES = {"image/gif", "image/png", "image/jpeg"}
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
# How the course's own HTML points at its files: http://<host>/moodle/file.php/<course id>/<path in course_files>
FILE_PHP = re.compile(r"^(?:https?://[^/]+)?(?:/[^/]+)*/file\.php/\d+/(.+)$")
YOUTUBE_EMBED = re.compile(r"^https?://(?:www\.)?youtube\.com/embed/([A-Za-z0-9_-]+)")
# Third parties named in the text. The owner, who taught and wrote the course, directed attribution to IntraHealth
# International (2026-10-09); the other people the overview credits are not named here. Each rule is counted in `withheld`.
WITHHOLD = [("course development team",
             re.compile(r"(\*\*Course Development Team:\*\*)[^\n]*"),
             r"\1 (names withheld)",
             "the Course Development Team named on the course overview: four people besides the instructor, who are third parties; "
             "attribution is to IntraHealth International, as the owner directed")]
# Images that show personal data, reviewed one by one (2026-10-09). They are inventoried, never copied, and the text
# that shows one says it is withheld. A decision, not a heuristic: a new image is published unless it is listed here.
THIRD_PARTY = "a third party's name"
WITHHOLD_IMAGES = {
    "installing_ubuntu_native10.gif": f"{THIRD_PARTY} (an Ubuntu installer's account form filled in by someone else; likely from a third-party tutorial)",
    "installing_ubuntu_native11.gif": f"{THIRD_PARTY} (an Ubuntu login screen; likely from a third-party tutorial)",
    "install_ubuntu_vmware6.gif": f"{THIRD_PARTY} (an Ubuntu login screen; likely from a third-party tutorial)",
    "translating_ihris2.gif": f"{THIRD_PARTY} (a Launchpad translator's name)",
    "translating_ihris3.gif": f"{THIRD_PARTY} (a Launchpad translator's user name)",
    "troubleshooting3.gif": f"{THIRD_PARTY} (other pastebin users' handles)",
    "user_roles4.gif": "an e-mail address (in a filled-in user form)",
    "user_roles5.gif": "an e-mail address (in a filled-in user form)",
    "into_forms1.gif": "a date of birth with a name (example data of real people)",
    "into_forms3.gif": "a photograph of a child",
}
KEEP_TAGS = {"p", "br", "ul", "ol", "li", "strong", "b", "em", "i", "a", "img", "table", "thead", "tbody", "tr", "td", "th",
             "h1", "h2", "h3", "h4", "h5", "h6", "pre", "code", "blockquote", "hr", "sup", "sub"}
DROP_TAGS = {"script", "style", "object", "embed", "form", "input", "button", "select", "textarea", "noscript"}

NOT_RECORDED_STRUCTURE = [
    "the course summary, the section summaries and the course-overview page (body text; no licence recorded)",
    "lesson page contents and answers (body text; no licence recorded): only each page's title is recorded",
    "forum, glossary, quiz, certificate and questionnaire introductions (body text)",
    "quiz questions and questionnaire questions and choices (text): only their number is recorded",
]
NOT_RECORDED_ALWAYS = [
    "lesson pages' answers: in these lessons every page is a content page, and its answers are only the Next and Previous buttons",
    "the certificate's settings, which name a contact e-mail address (personal data), and its images (a signature and a seal)",
    "blocks, roles, question categories, the gradebook and every timestamp but the course's creation and the backup's date (site configuration)",
    "user data: the backup holds none (USERS none, USERINFO false), so there are no posts, attempts or responses",
]


def fail(msg):
    sys.exit(f"ingest_moodle_course: {msg}")


def iso(ts):
    return datetime.datetime.fromtimestamp(int(ts), tz=datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def text(e, tag):
    v = e.findtext(tag)
    if v is None:
        fail(f"<{e.tag}> has no <{tag}>")
    return v


class Redactor:
    def __init__(self):
        self.n = 0

    def __call__(self, s):
        s, k = EMAIL_RE.subn("[e-mail removed]", s)
        self.n += k
        return s


RED = Redactor()


def clean(s):
    return RED(" ".join((s or "").split()))


def safe_members(z):
    infos = z.infolist()
    if len(infos) > MAX_MEMBERS:
        fail(f"{len(infos)} members, more than {MAX_MEMBERS}")
    total = 0
    for i in infos:
        n = i.filename
        if n.startswith(("/", "\\")) or re.match(r"^[A-Za-z]:", n) or ".." in n.replace("\\", "/").split("/") or "\x00" in n:
            fail(f"unsafe member path {n!r}")
        if i.is_dir():
            continue
        if i.file_size > MAX_MEMBER_BYTES:
            fail(f"{n}: {i.file_size} bytes, more than {MAX_MEMBER_BYTES}")
        if i.compress_size and i.file_size / i.compress_size > MAX_RATIO:
            fail(f"{n}: compression ratio above {MAX_RATIO}")
        total += i.file_size
    if total > MAX_TOTAL_BYTES:
        fail(f"{total} bytes uncompressed, more than {MAX_TOTAL_BYTES}")
    return [i for i in infos if not i.is_dir()]


def course_file(ref, files):
    """A resource reference: an http(s) URL, or a file in course_files/ (relative, or ../../file.php/<course>/...)."""
    if re.match(r"^https?://", ref):
        return {"url": ref}
    m = re.match(r"^(?:\.\./\.\./file\.php/\d+/)?([^:]+)$", ref)
    if not m or m.group(1).startswith("/"):
        fail(f"resource reference {ref!r} is neither a URL nor a course file")
    path = "course_files/" + m.group(1)
    if path not in files:
        fail(f"resource reference {ref!r} names {path}, which the backup does not hold")
    return {"courseFile": path}


def md_esc(s):
    return re.sub(r"([\\`*_\[\]<>#|])", r"\\\1", s)


def slug_doc(path):
    return os.path.splitext(os.path.basename(path))[0]


# ------------------------------------------------------------------ HTML to Markdown
class _Converter(MarkdownConverter):
    """markdownify, with `<` and `>` in running text written as entities: the course teaches HTML templates and shows
    their code as text, which must stay text when the Markdown is rendered (no raw HTML, no event handler survives)."""

    def escape(self, text, parent_tags):
        return super().escape(text, parent_tags).replace("<", "&lt;").replace(">", "&gt;")


def markdownify(html, **options):
    return _Converter(**options).convert(html)


class Converter:
    """The course's HTML, sanitised, with its links to course files rewritten, as Markdown.
    Links are written relative to a file one directory below the entry (modules/, sections/)."""

    def __init__(self, files, published):
        self.files = files            # zip path -> inventory record
        self.published = published    # zip path -> path in the entry (images/..., transcripts/...md)
        self.missing = {}             # an image the text shows but the backup does not hold -> who shows it
        self.audio = set()            # audio the text links to (not committed)
        self.images_used = {}         # images/<file> -> {module ids}
        self.withheld = {}            # WITHHOLD key -> count
        self.withheld_images = {}     # WITHHOLD_IMAGES file -> {module ids}

    def target(self, url):
        m = FILE_PHP.match(url.strip())
        return ("course_files/" + m.group(1)) if m else None

    def __call__(self, html, who):
        soup = BeautifulSoup(html or "", "html.parser")
        for t in soup.find_all(DROP_TAGS):
            t.decompose()
        for t in soup.find_all("iframe"):
            m = YOUTUBE_EMBED.match(t.get("src") or "")
            if m:
                a = soup.new_tag("a", href=f"https://www.youtube.com/watch?v={m.group(1)}")
                a.string = f"YouTube video {m.group(1)}"
                p = soup.new_tag("p")
                p.append(a)
                t.replace_with(p)
            else:
                t.decompose()
        for t in soup.find_all("img"):
            src = (t.get("src") or "").strip()
            cf = self.target(src)
            alt = t.get("alt") or t.get("title") or ""
            if cf and cf in self.published:
                rel = self.published[cf]
                self.images_used.setdefault(rel, set()).add(who)
                t.attrs = {"src": "../" + rel, "alt": alt}
            elif cf and os.path.basename(cf) in WITHHOLD_IMAGES:
                self.withheld_images.setdefault(os.path.basename(cf), set()).add(who)
                t.replace_with(soup.new_string(f"[image withheld: {os.path.basename(cf)} shows {WITHHOLD_IMAGES[os.path.basename(cf)].split(' (')[0]}]"))
            else:
                self.missing.setdefault(cf or src, set()).add(who)
                t.replace_with(soup.new_string(f"[image not in the backup: {os.path.basename(cf or src)}]"))
        for t in soup.find_all("a"):
            href = (t.get("href") or "").strip()
            cf = self.target(href)
            if cf:
                if cf in self.published:
                    t.attrs = {"href": "../" + self.published[cf]}
                elif cf in self.files and self.files[cf]["mediaType"].startswith("audio/"):
                    self.audio.add(cf)
                    t.replace_with(soup.new_string(f"{t.get_text()} [audio {os.path.basename(cf)}, not published] "))
                else:
                    t.replace_with(soup.new_string(f"{t.get_text()} [{os.path.basename(cf)}, not in the backup]"))
            else:
                t.attrs = {"href": href} if href else {}
        # HTML collapses whitespace; so does this, outside <pre>, so that indented source text is not read as a Markdown code block.
        for t in soup.find_all(string=True):
            if not t.find_parent(["pre", "code"]) and re.search(r"\s{2,}|\n", t):
                t.replace_with(re.sub(r"\s+", " ", str(t)))
        for t in soup.find_all(True):
            if t.name in KEEP_TAGS:
                t.attrs = {k: v for k, v in t.attrs.items() if (t.name, k) in {("a", "href"), ("img", "src"), ("img", "alt")}}
            else:
                t.unwrap()
        md = markdownify(str(soup), heading_style="ATX", bullets="-", strip=None)
        md = md.replace("\xa0", " ")
        md = "\n".join(line.rstrip() for line in md.split("\n"))
        md = re.sub(r"\n{3,}", "\n\n", md).strip()
        for key, rx, sub, _ in WITHHOLD:
            md, k = rx.subn(sub, md)
            if k:
                self.withheld[key] = self.withheld.get(key, 0) + k
        return RED(md)


def transcript_md(data, name):
    """A transcript .doc's text, with `antiword -w 0` under a fixed UTF-8 locale, as Markdown: the first line is the
    title, a `Slide N:` line a heading, every other non-empty line a paragraph."""
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "t.doc")
        with open(p, "wb") as f:
            f.write(data)
        try:
            out = subprocess.run(["antiword", "-w", "0", p], capture_output=True, text=True, check=True,
                                 env={**os.environ, "LC_ALL": "C.UTF-8", "LANG": "C.UTF-8"}).stdout
        except FileNotFoundError:
            fail("antiword is not installed (apt-get install antiword); it extracts the transcripts")
    lines = [" ".join(x.split()) for x in out.split("\n")]
    lines = [x for x in lines if x]
    if not lines:
        fail(f"{name}: antiword extracted no text")
    md = [f"# {md_esc(lines[0])}", ""]
    for x in lines[1:]:
        m = re.fullmatch(r"Slide (\d+):?", x)
        md += ([f"## Slide {m.group(1)}", ""] if m else [md_esc(x), ""])
    return RED("\n".join(md).rstrip() + "\n"), hashlib.sha256(out.encode()).hexdigest()


# ------------------------------------------------------------------ module content (only with a licence)
def lesson_md(m, rec, conv):
    out = [f"# {md_esc(rec['name'])}", ""]
    for i, pg in enumerate(m.find("PAGES").findall("PAGE"), 1):
        title = clean(text(pg, "TITLE"))
        out += [f"## {i}. {md_esc(title) if title else '(untitled page)'}", "", conv(pg.findtext("CONTENTS"), rec["id"]), ""]
    return out


def question_md(q, conv, who):
    qt = text(q, "QTYPE")
    out = [conv(q.findtext("QUESTIONTEXT"), who), ""]
    answers = {a.findtext("ID"): a for a in (q.find("ANSWERS").findall("ANSWER") if q.find("ANSWERS") is not None else [])}
    if qt in ("multichoice", "truefalse"):
        for a in answers.values():
            right = float(a.findtext("FRACTION") or 0) > 0
            out.append(f"- {'**(correct)** ' if right else ''}{conv(a.findtext('ANSWER_TEXT'), who)}")
            fb = a.findtext("FEEDBACK") or ""
            if fb.strip():
                out.append(f"  - feedback: {conv(fb, who)}")
    elif qt == "match":
        out += ["| statement | answer |", "|---|---|"]
        for mt in q.find("MATCHS").findall("MATCH"):
            out.append(f"| {conv(mt.findtext('QUESTIONTEXT'), who).replace('|', '/')} | {conv(mt.findtext('ANSWERTEXT'), who).replace('|', '/')} |")
    else:
        fail(f"question type {qt} is not one this tool knows; teach it how to write one")
    fb = q.findtext("GENERALFEEDBACK") or ""
    if fb.strip():
        out += ["", f"*Feedback:* {conv(fb, who)}"]
    return out + [""], qt


def quiz_md(m, rec, conv, questions):
    out = [f"# {md_esc(rec['name'])}", ""]
    intro = conv(m.findtext("INTRO"), rec["id"])
    if intro:
        out += [intro, ""]
    for i, qi in enumerate(m.find("QUESTION_INSTANCES").findall("QUESTION_INSTANCE"), 1):
        q = questions.get(text(qi, "QUESTION"))
        if q is None:
            fail(f"quiz {rec['id']} uses question {text(qi, 'QUESTION')}, which no question category holds")
        body, qt = question_md(q, conv, rec["id"])
        out += [f"## Question {i} ({qt})", ""] + body
    return out


def questionnaire_md(m, rec, conv):
    out = [f"# {md_esc(rec['name'])}", ""]
    s = conv(m.findtext("SUMMARY"), rec["id"])
    if s:
        out += [s, ""]
    qs = [q for q in m.find("SURVEY").findall("QUESTION") if q.findtext("DELETED") != "y"]
    for q in sorted(qs, key=lambda q: int(q.findtext("POSITION") or 0)):
        out += [f"## {q.findtext('POSITION')}. {md_esc(clean(q.findtext('NAME')))}", "", conv(q.findtext("CONTENT"), rec["id"]), ""]
        for c in q.findall("QUESTION_CHOICE"):
            out.append("- " + md_esc(clean(re.sub(r"^!other=", "", c.findtext("CONTENT") or ""))))
        out.append("")
    return out


def intro_md(m, rec, conv, tag):
    body = conv(m.findtext(tag), rec["id"])
    return [f"# {md_esc(rec['name'])}", "", body, ""] if body else None


def write_md(rel, lines):
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    data = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).rstrip() + "\n"
    with open(p, "w", encoding="utf-8") as f:
        f.write(data)
    return hashlib.sha256(data.encode()).hexdigest()


# ------------------------------------------------------------------ main
def main():
    man = json.load(open(os.path.join(ROOT, MANIFEST), encoding="utf-8"))
    decl = json.load(open(os.path.join(ROOT, DECL), encoding="utf-8"))
    lic = decl.get("licence")
    full = bool(lic) and lic.get("status") in ("stated", "permission")
    p = os.path.join(UP, man["file"])
    if not os.path.exists(p):
        fail(f"{p}: missing. Upload it (see {MANIFEST}).")
    raw = open(p, "rb").read()
    md5, sha = hashlib.md5(raw).hexdigest(), hashlib.sha256(raw).hexdigest()
    if (md5, sha, len(raw)) != (man["md5"], man["sha256"], man["bytes"]):
        fail(f"{p}: md5/sha256/size do not match {MANIFEST}; refusing to derive from it")

    with zipfile.ZipFile(p) as z:
        members = safe_members(z)
        files, blobs = {}, {}
        for i in sorted(members, key=lambda i: i.filename):
            data = z.read(i)  # zipfile checks the CRC
            if len(data) != i.file_size:
                fail(f"{i.filename}: read {len(data)} bytes, the directory says {i.file_size}")
            ext = os.path.splitext(i.filename)[1].lower()
            files[i.filename] = {"path": i.filename, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
                                 "mediaType": MEDIA.get(ext, "application/octet-stream"), "publishedAs": None}
            blobs[i.filename] = data
    xml_bytes = blobs.get("moodle.xml")
    if xml_bytes is None:
        fail("the zip holds no moodle.xml: not a Moodle 1.9 backup")
    if re.search(rb"<!(DOCTYPE|ENTITY)", xml_bytes, re.I):
        fail("moodle.xml declares a DOCTYPE or ENTITY; refusing to parse it")
    root = ET.fromstring(xml_bytes)
    if root.tag != "MOODLE_BACKUP":
        fail(f"moodle.xml root is <{root.tag}>, not <MOODLE_BACKUP>")

    info = root.find("INFO")
    det = info.find("DETAILS")
    if text(det, "USERS") != "none":
        fail(f"the backup holds users ({text(det, 'USERS')}); a person's data is never ingested")
    for m in det.findall("MOD"):
        if text(m, "USERINFO") != "false":
            fail(f"module type {text(m, 'NAME')} carries user info; a person's data is never ingested")

    # What is published, and where: every image in course_files, and every .doc transcript's text.
    published = {}
    if full:
        for path, f in files.items():
            if not path.startswith("course_files/"):
                continue
            if f["mediaType"] in IMAGE_TYPES:
                if os.path.basename(path) not in WITHHOLD_IMAGES:
                    published[path] = "images/" + os.path.basename(path)
            elif f["mediaType"] == "application/msword":
                published[path] = "transcripts/" + slug_doc(path) + ".md"
        if len(set(published.values())) != len(published):
            fail("two course files would be published under one name")
        for path, rel in published.items():
            files[path]["publishedAs"] = rel
    conv = Converter(files, published)

    course = root.find("COURSE")
    head = course.find("HEADER")
    byref = {}
    for m in course.find("MODULES").findall("MOD"):
        key = (text(m, "MODTYPE"), text(m, "ID"))
        if key in byref:
            fail(f"module {key} appears twice")
        byref[key] = m
    questions = {}
    for cat in course.find("QUESTION_CATEGORIES").findall("QUESTION_CATEGORY"):
        qs = cat.find("QUESTIONS")
        for q in (qs.findall("QUESTION") if qs is not None else []):
            questions[text(q, "ID")] = q

    if full:
        for d in CONTENT_DIRS:
            shutil.rmtree(os.path.join(OUT, d), ignore_errors=True)
    else:
        for d in CONTENT_DIRS:
            if os.path.isdir(os.path.join(OUT, d)):
                shutil.rmtree(os.path.join(OUT, d))
    sections, modules, placed = [], [], set()
    counts = {"lessonPages": 0, "quizQuestions": 0, "questionnaireQuestions": 0, "glossaryEntries": 0, "externalUrls": 0}
    for s in course.find("SECTIONS").findall("SECTION"):
        num = int(text(s, "NUMBER"))
        ids = []
        for sm in (s.find("MODS") if s.find("MODS") is not None else []):
            mtype, inst, cmid = text(sm, "TYPE"), text(sm, "INSTANCE"), text(sm, "ID")
            m = byref.get((mtype, inst))
            if m is None:
                fail(f"section {num} places {mtype} {inst}, which MODULES does not hold")
            if (mtype, inst) in placed:
                fail(f"{mtype} {inst} is placed twice")
            placed.add((mtype, inst))
            rec = {"id": f"cm-{int(cmid)}", "type": mtype, "name": clean(text(m, "NAME")), "section": num,
                   "indent": int(text(sm, "INDENT")), "visible": text(sm, "VISIBLE") == "1"}
            body = None
            if mtype == "lesson":
                pages = m.find("PAGES")
                rec["pages"] = [clean(text(pg, "TITLE")) for pg in (pages.findall("PAGE") if pages is not None else [])]
                counts["lessonPages"] += len(rec["pages"])
                if full:
                    body = lesson_md(m, rec, conv)
            elif mtype == "resource":
                rec["resourceType"] = text(m, "TYPE")
                ref = (m.findtext("REFERENCE") or "").strip()
                if rec["resourceType"] == "file" and ref:
                    rec["reference"] = course_file(ref, files)
                    counts["externalUrls"] += "url" in rec["reference"]
                    if "courseFile" in rec["reference"] and rec["reference"]["courseFile"] in published:
                        rec["reference"]["publishedAs"] = published[rec["reference"]["courseFile"]]
                elif ref:
                    fail(f"resource {cmid} of type {rec['resourceType']} has a reference this tool does not read")
                if full and rec["resourceType"] in ("html", "text"):
                    body = [f"# {md_esc(rec['name'])}", "", conv(m.findtext("ALLTEXT"), rec["id"]), ""]
            elif mtype == "quiz":
                qi = m.find("QUESTION_INSTANCES")
                rec["questions"] = len(qi.findall("QUESTION_INSTANCE")) if qi is not None else 0
                counts["quizQuestions"] += rec["questions"]
                if full:
                    body = quiz_md(m, rec, conv, questions)
            elif mtype == "questionnaire":
                sv = m.find("SURVEY")
                rec["questions"] = sum(1 for q in (sv.findall("QUESTION") if sv is not None else []) if q.findtext("DELETED") != "y")
                counts["questionnaireQuestions"] += rec["questions"]
                if full:
                    body = questionnaire_md(m, rec, conv)
            elif mtype == "glossary":
                en = m.find("ENTRIES")
                rec["entries"] = len(en.findall("ENTRY")) if en is not None else 0
                counts["glossaryEntries"] += rec["entries"]
                if rec["entries"]:
                    fail("the glossary has entries; teach this tool to write them (concept, definition, verbatim)")
                if full:
                    body = intro_md(m, rec, conv, "INTRO")
            elif mtype in ("forum", "certificate"):
                if full:
                    body = intro_md(m, rec, conv, "INTRO")
            else:
                fail(f"module type {mtype} is not one this tool knows; teach it what is a heading and what is text")
            if body:
                rec["file"] = f"modules/{rec['id']}.md"
                rec["sha256"] = write_md(rec["file"], body)
            modules.append(rec)
            ids.append(rec["id"])
        sec = {"number": num, "visible": text(s, "VISIBLE") == "1", "modules": ids}
        if full:
            summ = conv(s.findtext("SUMMARY"), f"section-{num}")
            if summ:
                sec["file"] = f"sections/section-{num}.md"
                sec["sha256"] = write_md(sec["file"], [f"# {'General' if num == 0 else 'Section ' + str(num)}", "", summ])
        sections.append(sec)
    if set(byref) - placed:
        fail(f"modules in no section: {sorted(set(byref) - placed)}")
    if [s["number"] for s in sections] != list(range(len(sections))):
        fail("sections are not numbered 0..n-1 in order")

    images, transcripts = [], []
    if full:
        for path, rel in sorted(published.items(), key=lambda kv: kv[1]):
            f = files[path]
            if rel.startswith("images/"):
                os.makedirs(os.path.join(OUT, "images"), exist_ok=True)
                with open(os.path.join(OUT, rel), "wb") as fh:
                    fh.write(blobs[path])
                images.append({"file": rel, "from": path, "bytes": f["bytes"], "sha256": f["sha256"], "mediaType": f["mediaType"],
                               "usedBy": sorted(conv.images_used.get(rel, set()), key=lambda x: (x.split("-")[0], int(x.split("-")[1])))})
            else:
                md, text_sha = transcript_md(blobs[path], path)
                sha_md = write_md(rel, md.rstrip("\n").split("\n"))
                transcripts.append({"file": rel, "from": path, "title": md.split("\n", 1)[0][2:].replace("\\", ""),
                                    "sha256": sha_md, "textSha256": text_sha, "extractedWith": "antiword -w 0"})

    by_type = {}
    for m in modules:
        by_type[m["type"]] = by_type.get(m["type"], 0) + 1
    inv = [files[k] for k in sorted(files)]
    counts = {"sections": len(sections), "modules": len(modules), "modulesByType": dict(sorted(by_type.items())), **counts,
              "files": len(inv), "fileBytes": sum(f["bytes"] for f in inv),
              "images": len(images), "transcripts": len(transcripts),
              "contentFiles": sum(1 for x in modules + sections if x.get("file")) + len(transcripts) + (1 if full and head.findtext("SUMMARY") else 0)}
    exp = man["expect"]
    got = {"sections": counts["sections"], "modules": counts["modules"], "modulesByType": counts["modulesByType"],
           "files": counts["files"], "uncompressedBytes": counts["fileBytes"]}
    if got != exp:
        fail(f"parsed {got}, and {MANIFEST} expects {exp}")

    bk = {"name": text(info, "NAME"), "date": iso(text(info, "DATE")), "moodleRelease": text(info, "MOODLE_RELEASE"),
          "moodleVersion": text(info, "MOODLE_VERSION"), "backupRelease": text(info, "BACKUP_RELEASE"),
          "originalWwwroot": text(info, "ORIGINAL_WWWROOT"), "users": "none", "userInfo": False}
    summary = conv(head.findtext("SUMMARY"), "course") if full else None
    summary_ptr = None
    if summary:
        summary_ptr = {"file": "sections/course-summary.md"}
        summary_ptr["sha256"] = write_md(summary_ptr["file"], ["# " + md_esc(clean(text(head, "FULLNAME"))), "", summary])
    rec = {
        "$schema": "ihris-moodle-course/v1",
        "title": clean(text(head, "FULLNAME")),
        "shortname": clean(text(head, "SHORTNAME")),
        "format": text(head, "FORMAT"),
        "category": clean(head.find("CATEGORY").findtext("NAME")),
        "createdAt": iso(text(head, "TIMECREATED")),
        "backup": bk,
        "summaryFile": summary_ptr,
        "source": {"file": man["file"], "bytes": len(raw), "md5": md5, "sha256": sha, "manifest": MANIFEST,
                   "moodleXmlSha256": files["moodle.xml"]["sha256"]},
        "licence": ({"status": lic["status"], "id": lic.get("id"), "attribution": lic["attribution"], "declaration": DECL} if full else None),
        "licenceNote": ((f"{lic['status'].capitalize()} licence {lic.get('id') or ''} recorded in {DECL}: the content is ingested, attributed. "
                         "The backup itself states no licence.") if full else
                        ("No licence is stated in the backup (course summary, overview page, lesson pages, section summaries), "
                         "its transcripts or its media files, and none is recorded in the declaration. AGENTS.md rule 4: listed by "
                         "path and heading only. Only the owner can grant permission to publish more.")),
        "counts": counts,
        "sections": sections,
        "modules": modules,
        "images": images,
        "transcripts": transcripts,
        "withheldImages": [{"from": p, "why": WITHHOLD_IMAGES[os.path.basename(p)],
                            "shownBy": sorted(conv.withheld_images.get(os.path.basename(p), set()))}
                           for p in sorted(files) if full and os.path.basename(p) in WITHHOLD_IMAGES],
        "missingImages": [{"src": k, "shownBy": sorted(v)} for k, v in sorted(conv.missing.items())],
        "files": inv,
        "notRecorded": ([] if full else NOT_RECORDED_STRUCTURE) + NOT_RECORDED_ALWAYS
        + (["the slide audio: inventoried by path, size and sha256 only, not committed because of its size; "
            "a link to it in the text says so"] if full else []),
        "redactions": 0,
        "withheld": [{"what": key, "why": why, "count": conv.withheld[key]} for key, _, _, why in WITHHOLD if conv.withheld.get(key)],
    }
    os.makedirs(OUT, exist_ok=True)
    write_course_md(rec, summary)
    rec["redactions"] = RED.n
    with open(os.path.join(OUT, "course.json"), "w", encoding="utf-8") as f:
        json.dump(rec, f, indent=1, ensure_ascii=False)
        f.write("\n")
    contains = [f"{ENTRY}/course"] + [f"{ENTRY}/{x['file'][:-3]}" for x in sections + modules + transcripts if x.get("file")]
    with open(os.path.join(OUT, "manifest.jsonld"), "w", encoding="utf-8") as f:
        json.dump({"@context": "https://litlfred.github.io/folio-assistant/ns/content/v1.jsonld", "@id": f"{ENTRY}/manifest",
                   "@type": ["folio:SourceDocument"], "title": f"{rec['title']} (Moodle course backup)",
                   "contains": contains, "provenance": "ingested" if full else "described",
                   "meta": {"source_files": [man["file"]], "document_class": "moodle-course-backup",
                            "licence": (f"{lic.get('id')} ({lic['status']}); {lic['attribution']}" if full
                                        else "none stated: listed by path and heading only (AGENTS.md rule 4)"),
                            "disposition": (("ingested: the structure in course.json (ihris-moodle-course/v1) and course.md, the section "
                                             "summaries, one Markdown file per module with content, the transcripts' text and the images; "
                                             "the slide audio is inventoried, not committed; the zip is held in uploads/ (git-ignored)") if full else
                                            ("described: the course structure and a file inventory, in course.json (ihris-moodle-course/v1) "
                                             "and course.md; no body text and no course file is reproduced; the zip is held in uploads/ (git-ignored)"))}},
                  f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"course: {rec['title']!r} ({rec['shortname']}), backed up {bk['date']} from {bk['originalWwwroot']}; "
          f"{'full (' + lic['status'] + ' ' + str(lic.get('id')) + ')' if full else 'structure only'}")
    print(f"counts: {json.dumps(counts)}; redactions: {RED.n}; images not in the backup: {[os.path.basename(x['src']) for x in rec['missingImages']]}; "
          f"audio linked, not published: {len(conv.audio)}")


def write_course_md(rec, summary):
    c, bk = rec["counts"], rec["backup"]
    lic = rec["licence"]
    by_id = {m["id"]: m for m in rec["modules"]}
    out = [f"# {md_esc(rec['title'])}", "",
           f"Moodle course **{md_esc(rec['title'])}** (shortname *{md_esc(rec['shortname'])}*, {rec['format']} format), "
           f"from <{bk['originalWwwroot']}>, created {rec['createdAt'][:10]} and backed up {bk['date'][:10]} "
           f"with Moodle {md_esc(bk['moodleRelease'])}. Generated by `src/tools/ingest_moodle_course.py` from "
           f"`{rec['source']['file']}` (sha256 `{rec['source']['sha256']}`); never edit this file.", ""]
    if lic:
        out += [f"**{md_esc(lic['attribution'])}**", ""]
        if summary:
            out += [summary, ""]
    else:
        out += ["**Structure only.** The course states no licence and none is recorded, so it is listed by path and heading only "
                "(AGENTS.md rule 4): sections, modules, lesson page titles, resource links and question counts. "
                "Only the owner can grant permission to publish more.", ""]
    out += [f"{c['sections']} sections, {c['modules']} modules ("
            + ", ".join(f"{n} {t}" for t, n in c["modulesByType"].items())
            + f"), {c['lessonPages']} lesson pages, {c['quizQuestions']} quiz questions, "
            f"{c['questionnaireQuestions']} questionnaire questions, {c['glossaryEntries']} glossary entries, "
            f"{c['externalUrls']} external links, {c['images']} images, {c['transcripts']} transcripts, "
            f"{c['files']} files in the backup ({c['fileBytes']} bytes).", ""]
    for s in rec["sections"]:
        out += [f"## {'General' if s['number'] == 0 else 'Section ' + str(s['number'])}", ""]
        if s.get("file"):
            body = open(os.path.join(OUT, s["file"]), encoding="utf-8").read().split("\n", 2)[2].strip()
            out += [re.sub(r"\]\(\.\./", "](", body), ""]
        for mid in s["modules"]:
            m = by_id[mid]
            ind = "  " * m["indent"]
            name = f"[{md_esc(m['name'])}]({m['file']})" if m.get("file") else md_esc(m["name"])
            line = f"{ind}- *{m['type']}* {name}"
            if m["type"] == "lesson":
                line += f" ({len(m['pages'])} pages)"
            elif m["type"] in ("quiz", "questionnaire"):
                line += f" ({m['questions']} questions)"
            elif m["type"] == "glossary":
                line += f" ({m['entries']} entries)"
            ref = m.get("reference") or {}
            if "url" in ref:
                line += f": <{ref['url']}>"
            elif ref.get("publishedAs"):
                line += f": [{ref['publishedAs']}]({ref['publishedAs']})"
            elif "courseFile" in ref:
                line += f": `{ref['courseFile']}` (not reproduced)"
            elif m["type"] == "resource" and not m.get("file"):
                line += f" ({m['resourceType']} page, not reproduced)"
            out.append(line)
            if not m.get("file"):
                for i, t in enumerate(m.get("pages") or [], 1):
                    out.append(f"{ind}    {i}. {md_esc(t) if t else '*(untitled page)*'}")
        out.append("")
    if rec["transcripts"]:
        out += ["## Transcripts", ""] + [f"- [{md_esc(t['title'])}]({t['file']}) (from `{t['from']}`)" for t in rec["transcripts"]] + [""]
    out += ["## Files in the backup", "", "| path | bytes | media type | published as | sha256 |", "|---|---|---|---|---|"]
    out += [f"| `{f['path']}` | {f['bytes']} | {f['mediaType']} | {f['publishedAs'] or '-'} | `{f['sha256'][:16]}…` |" for f in rec["files"]]
    data = RED("\n".join(out) + "\n")
    with open(os.path.join(OUT, "course.md"), "w", encoding="utf-8") as fh:
        fh.write(data)


if __name__ == "__main__":
    main()
