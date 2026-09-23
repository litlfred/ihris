#!/usr/bin/env python3
"""Ingest the iHRIS Administrator Handbook (2010 wiki export) into library/ihris-admin-handbook/.

The handbook is an mwlib/PediaPress PDF of 79 articles from the iHRIS wiki
(open.intrahealth.org), generated 2010-09-17. Its text is licensed GFDL-1.2 (page
534); its images say "License: unknown" and are published with the owner's
permission (2026-09-23). See ihris-admin-handbook.json.

Steps, all deterministic:

1. Verify uploads/ihris-admin-handbook/<pdf> against its manifest's sha256. Refuse on mismatch.
2. Run folio-assistant's rungs on it: cat-harness/scripts/pdf-structure.py
   (structure.json, pdf-structure/v1) and cat-harness/scripts/pdf-images.py
   (images.json, folio-document-images/v1, plus images/*.png). structure.json's
   metadata.title is corrected from the DocInfo /Title (the rung took the mwlib
   banner on page 1), and source.mtime is nulled so a re-run gives the same file.
3. Write one Markdown file per wiki article to sections/<id>.md (+ a .jsonld node),
   from the PDF's own text layer: outline level-1 entries are the articles, bold
   headings become Markdown headings, FreeMono runs become fenced code, bullets
   become list items. Running page headers are dropped. Two mwlib artefacts are
   undone: the spaces it puts inside URLs ("http:/ / www. gnu. org/") and hidden
   1-pt text. Real e-mail addresses and phone numbers are REDACTED (placeholders
   such as your@email.add.ress are kept); each redaction is counted in book.json.
4. Parse the appendices: "Article Sources and Contributors" (each article's wiki
   revision and contributors, the GFDL attribution) and "Image Sources, Licenses
   and Contributors" (each image's file name, source and licence line). Credits
   are matched to the placed images in order of appearance (page, then top edge),
   and the counts must agree or the script refuses.
5. Write book.json (ihris-wiki-book/v1) and manifest.jsonld.

  python3 src/tools/ingest_handbook.py        # needs pymupdf and a folio-assistant checkout
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UP = os.path.join(ROOT, "uploads", "ihris-admin-handbook")
OUT = os.path.join(ROOT, "library", "ihris-admin-handbook")
ENTRY = "library/ihris-admin-handbook"
FA = os.environ.get("FOLIO_ASSISTANT", os.path.join(ROOT, "..", "litlfred", "folio-assistant"))
MONO = ("FreeMono",)
# Placeholder addresses in example configuration. Kept: they identify nobody.
PLACEHOLDER_EMAILS = {"your@email.add.ress", "someone@somwhere.org", "my_email@somewhere.com"}
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
PHONE = re.compile(r"(?<![\w.-])(?:\+?1-)?\d{3}-\d{3}-\d{4}(?![\w-])|\+\d{1,3}[ -]\d{2,4}[ -]\d{3,4}[ -]?\d{0,4}")
URL_START = re.compile(r"(https?|ftp):/ / ")


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def slug(t):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", t.lower())).strip("-")


def fix_urls(s):
    """Undo mwlib's line-break spaces inside URLs: a space right after one of ./+-_?=&#:~% inside a URL."""
    out, i = [], 0
    for m in URL_START.finditer(s):
        if m.start() < i:
            continue
        out.append(s[i:m.start()])
        j = m.end()
        url = m.group(1) + "://"
        while j < len(s):
            c = s[j]
            if c == " ":
                if url[-1] in "./+-_?=&#:~%" and j + 1 < len(s) and s[j + 1] not in " \n":
                    j += 1
                    continue
                break
            url += c
            j += 1
        out.append(url)
        i = j
    out.append(s[i:])
    return "".join(out)


class Redactor:
    def __init__(self):
        self.log = []  # (article id, page, kind)

    def __call__(self, s, art, page):
        def em(m):
            if m.group(0) in PLACEHOLDER_EMAILS:
                return m.group(0)
            self.log.append((art, page, "email"))
            return "[e-mail redacted]"

        def ph(m):
            self.log.append((art, page, "phone"))
            return "[phone number redacted]"
        return PHONE.sub(ph, EMAIL.sub(em, s))


def md_escape(s):
    s = s.replace("\\", "\\\\").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    for c in "`*_[]":
        s = s.replace(c, "\\" + c)
    return s


def verify():
    man = json.load(open(os.path.join(UP, "manifest.json")))
    pdf = os.path.join(UP, man["file"])
    if not os.path.exists(pdf):
        sys.exit(f"{pdf}: missing. Upload it (see uploads/ihris-admin-handbook/manifest.json).")
    got = sha256_file(pdf)
    if got != man["sha256"]:
        sys.exit(f"{pdf}: sha256 {got} does not match the manifest's {man['sha256']}; refusing to derive from it")
    return pdf, man


def run_rungs(pdf):
    scratch = os.path.join(ROOT, ".build", "handbook-rungs")
    shutil.rmtree(scratch, ignore_errors=True)
    os.makedirs(scratch)
    scripts = os.path.join(FA, "cat-harness", "scripts")
    for s, extra in (("pdf-structure.py", ["--no-sections"]), ("pdf-images.py", [])):
        r = subprocess.run([sys.executable, os.path.join(scripts, s), pdf, "-o", scratch] + extra, capture_output=True, text=True)
        if r.returncode != 0:
            sys.exit(f"{s} failed:\n{r.stdout}\n{r.stderr}")
    (doc_dir,) = [d for d in os.listdir(scratch) if os.path.isdir(os.path.join(scratch, d))]
    src = os.path.join(scratch, doc_dir)
    st = json.load(open(os.path.join(src, "structure.json")))
    st["source"]["mtime"] = None
    st["metadata"]["title"] = st["metadata"]["docinfo"]["Title"]
    st["metadata"]["title_note"] = ("title corrected from the DocInfo /Title (the rung read the mwlib banner on page 1 as the title); "
                                    "source.mtime nulled so a re-run reproduces this file (src/tools/ingest_handbook.py)")
    with open(os.path.join(OUT, "structure.json"), "w", encoding="utf-8") as f:
        json.dump(st, f, indent=1, ensure_ascii=False)
        f.write("\n")
    shutil.rmtree(os.path.join(OUT, "images"), ignore_errors=True)
    shutil.copytree(os.path.join(src, "images"), os.path.join(OUT, "images"))
    shutil.copy(os.path.join(src, "images.json"), os.path.join(OUT, "images.json"))
    return st, json.load(open(os.path.join(OUT, "images.json")))


# ------------------------------------------------------------------ text
def line_info(line):
    spans = [s for s in line["spans"] if s["size"] >= 2 and s["text"] != ""]
    text = "".join(s["text"] for s in spans)
    vis = [s for s in spans if s["text"].strip()]
    mono = bool(vis) and all(s["font"].startswith(MONO) for s in vis)
    bold = bool(vis) and all("Bold" in s["font"] for s in vis)
    size = max((s["size"] for s in vis), default=0)
    return {"text": text, "mono": mono, "bold": bold, "size": size, "x": line["bbox"][0], "y": line["bbox"][1]}


def image_order(doc):
    """[(rung image id, page, top)] in the rung's own id order (pdf-images.py enumerates get_images, then rects)."""
    out = []
    for i in range(doc.page_count):
        page = doc[i]
        n = 0
        for info in page.get_images(full=True):
            for rect in page.get_image_rects(info[0]):
                n += 1
                out.append((f"img-p{i + 1:03d}-{n}", i + 1, rect.y0, rect))
    return out


def blocks_of(doc, pno, imgs_on_page):
    """The page's content blocks in reading order, running header dropped; images as ('image', id)."""
    page = doc[pno - 1]
    d = page.get_text("dict")
    items = []
    for b in d["blocks"]:
        if b["bbox"][3] < 50 and pno > 1:
            continue  # running header: article title and page number
        if b["type"] == 1:
            continue  # placed images come from image_order, which matches the rung's ids
        lines = [line_info(l) for l in b.get("lines", [])]
        lines = [l for l in lines if l["text"].strip()]
        if lines:
            items.append((b["bbox"][1], "text", lines))
    for iid, _, top, _ in imgs_on_page:
        items.append((top, "image", iid))
    items.sort(key=lambda t: t[0])
    return items


def render_text_block(lines, red, art, pno):
    """One text block to Markdown: a heading, code, a list or a paragraph."""
    if all(l["mono"] for l in lines):
        return ("code", "\n".join(red(l["text"].rstrip(), art, pno) for l in lines))
    if len(lines) <= 3 and all(l["bold"] and l["size"] >= 12 for l in lines):
        # a heading; a long article title wraps onto a second line at 22pt
        return ("heading", {**lines[0], "text": " ".join(l["text"].strip() for l in lines)})
    if any(l["text"].strip() == "•" for l in lines):
        items, cur = [], None
        for l in lines:
            if l["text"].strip() == "•":
                cur = []
                items.append(cur)
            elif cur is None:
                items.append([l])
                cur = items[-1]
            else:
                cur.append(l)
        out = []
        for it in items:
            t = " ".join(x["text"].strip() for x in it)
            out.append("- " + md_escape(red(fix_urls(t), art, pno)))
        return ("list", "\n".join(out))
    t = " ".join(l["text"].strip() for l in lines)
    return ("para", md_escape(red(fix_urls(t), art, pno)))


def parse_article_sources(doc, first, last):
    text = "\n".join(doc[p - 1].get_text() for p in range(first, last + 1))
    text = re.sub(r"Article Sources and Contributors\n\d+\n", "", text)
    text = text.replace("Article Sources and Contributors\n", "", 1)
    out = {}
    for m in re.finditer(r"(.+?)\s+Source: (\S+)\s+Contributors: (.+?)(?=\n.+?\s+Source: |\Z)", text, re.S):
        title = m.group(1).strip()
        out[title] = {"source": m.group(2), "oldid": int(re.search(r"oldid=(\d+)", m.group(2)).group(1)),
                      "contributors": [c.strip() for c in " ".join(m.group(3).split()).split(",") if c.strip()]}
    return out


def parse_image_credits(doc, pno):
    text = doc[pno - 1].get_text()
    text = text.split("Image Sources, Licenses and Contributors\n", 2)[-1]
    text = re.sub(r"^\d+\n", "", text)
    out = []
    for m in re.finditer(r"((?:Image|File|image|file):\S+)\s+Source: (\S+)\s+License: (\S+)\s+Contributors:\s*(.+?)(?=\n(?:Image|File|image|file):|\Z)", text, re.S):
        out.append({"name": m.group(1), "source": m.group(2), "licence": m.group(3),
                    "contributors": [c.strip() for c in " ".join(m.group(4).split()).split(",") if c.strip()]})
    return out


def main():
    pdf, man = verify()
    os.makedirs(OUT, exist_ok=True)
    st, imgs = run_rungs(pdf)
    doc = pymupdf.open(pdf)
    toc = doc.get_toc()
    arts = [(t, p) for lvl, t, p in toc if lvl == 1]
    # the appendices mwlib appends after the last article
    page_title = {i + 1: (doc[i].get_text().split("\n", 1)[0].strip()) for i in range(doc.page_count)}
    src_pages = [p for p, t in page_title.items() if t == "Article Sources and Contributors"]
    img_pages = [p for p, t in page_title.items() if t == "Image Sources, Licenses and Contributors"]
    lic_pages = [p for p, t in page_title.items() if t == "License"]
    assert arts[-1][0] == "License" and len(img_pages) == 1 and lic_pages, "unexpected appendix layout"
    arts = arts[:-1]
    last_text_page = src_pages[0] - 1
    sources = parse_article_sources(doc, src_pages[0], src_pages[-1])
    credits = parse_image_credits(doc, img_pages[0])
    lic_text = " ".join(fix_urls(doc[lic_pages[0] - 1].get_text()).split("\n")[2:]).strip()

    order = image_order(doc)
    rung_ids = [i["id"] for i in imgs["images"]]
    if sorted(rung_ids) != sorted(o[0] for o in order):
        sys.exit("image ids differ from pdf-images.py's; refusing to match credits")
    by_flow = sorted(order, key=lambda o: (o[1], o[2]))
    if len(by_flow) != len(credits):
        sys.exit(f"{len(by_flow)} placed images but {len(credits)} image credits; refusing to guess the match")

    # walk every page, cutting at article title headings (outline level 1)
    red = Redactor()
    titles = {t for t, _ in arts}
    ids = {t: slug(t) for t, _ in arts}
    assert len(set(ids.values())) == len(ids), "article ids collide"
    sub = {}
    for lvl, t, p in toc:
        if lvl > 1:
            sub.setdefault((p, t.strip()), lvl)
    body = {t: [] for t, _ in arts}
    pages = {t: [None, None] for t, _ in arts}
    img_article = {}
    cur = None
    for pno in range(2, last_text_page + 1):
        imgs_here = [o for o in order if o[1] == pno]
        for _, kind, payload in blocks_of(doc, pno, imgs_here):
            if kind == "image":
                if cur:
                    body[cur].append(("image", payload))
                    img_article[payload] = cur
                    pages[cur][1] = pno
                continue
            r = render_text_block(payload, red, ids.get(cur, "front"), pno)
            if r[0] == "heading":
                ln = r[1]
                t = ln["text"].strip()
                if ln["size"] >= 20 and t in titles:
                    cur = t
                    pages[cur] = [pno, pno]
                    continue
                lvl = sub.get((pno, t)) or sub.get((pno, ln["text"])) or (2 if ln["size"] >= 14 else 3)
                r = ("heading-md", "#" * min(lvl, 6) + " " + md_escape(t))
            if cur:
                body[cur].append(r)
                pages[cur][1] = pno
    missing = [t for t in body if pages[t][0] is None]
    if missing:
        sys.exit(f"articles never found in the text: {missing}")

    # write the sections
    sec_dir = os.path.join(OUT, "sections")
    shutil.rmtree(sec_dir, ignore_errors=True)
    os.makedirs(sec_dir)
    credit_of = {o[0]: c for o, c in zip(by_flow, credits)}
    art_recs = []
    for t, _ in arts:
        aid = ids[t]
        s = sources.get(t)
        if not s:
            sys.exit(f"{t}: no entry in Article Sources and Contributors")
        parts = []
        for kind, x in body[t]:
            if kind == "code":
                if parts and parts[-1].startswith("```\n"):
                    parts[-1] = parts[-1][:-4] + "\n" + x + "\n```"
                else:
                    parts.append("```\n" + x + "\n```")
            elif kind == "image":
                c = credit_of[x]
                parts.append(f"![{md_escape(c['name'])}](../images/{x}.png)")
            elif kind in ("para", "list", "heading-md"):
                parts.append(x)
        fm = ["---", f"title: {json.dumps(t, ensure_ascii=False)}", f"source: {s['source']}",
              f"contributors: {json.dumps(s['contributors'], ensure_ascii=False)}", f"pages: {pages[t][0]}-{pages[t][1]}",
              "licence: GFDL-1.2", f"capturedFrom: uploads/ihris-admin-handbook/{man['file']}", "---", ""]
        text = "\n".join(fm) + f"# {md_escape(t)}\n\n" + "\n\n".join(parts) + "\n"
        with open(os.path.join(sec_dir, aid + ".md"), "w", encoding="utf-8") as f:
            f.write(text)
        with open(os.path.join(sec_dir, aid + ".jsonld"), "w", encoding="utf-8") as f:
            json.dump({"@context": "https://litlfred.github.io/folio-assistant/ns/content/v1.jsonld", "@id": f"{ENTRY}/sections/{aid}",
                       "@type": ["doco:Section"], "title": t, "derivedFrom": f"{ENTRY}/manifest", "sourceDocument": f"{ENTRY}/manifest",
                       "provenance": "ingested"}, f, indent=2, ensure_ascii=False)
            f.write("\n")
        art_recs.append({"id": aid, "title": t, "pageStart": pages[t][0], "pageEnd": pages[t][1], "source": s["source"], "oldid": s["oldid"],
                         "contributors": s["contributors"], "file": f"sections/{aid}.md", "sha256": hashlib.sha256(text.encode()).hexdigest()})

    from collections import Counter
    rc = Counter(red.log)
    book = {
        "$schema": "ihris-wiki-book/v1",
        "title": st["metadata"]["docinfo"]["Title"],
        "titleNote": "sic: 'Administator' is the export's own spelling",
        "wiki": "http://open.intrahealth.org/",
        "generator": "mwlib (PediaPress) with ReportLab",
        "generatedAt": "2010-09-17T16:32:14Z",
        "source": {"file": man["file"], "md5": man["md5"], "sha256": man["sha256"], "pages": doc.page_count,
                   "manifest": "uploads/ihris-admin-handbook/manifest.json"},
        "licence": {"text": {"id": "GFDL-1.2", "statement": lic_text, "page": lic_pages[0]},
                    "images": {"statedLicence": sorted({c["licence"] for c in credits}), "page": img_pages[0],
                               "publishedUnder": "permission (see ihris-admin-handbook.json)"}},
        "appendices": {"articleSources": src_pages, "imageCredits": img_pages, "licence": lic_pages},
        "articles": art_recs,
        "images": [{"id": o[0], "file": f"images/{o[0]}.png", "page": o[1], "article": ids.get(img_article.get(o[0]), None),
                    "credit": c, "creditMatchedBy": "order of appearance (page, then top edge) against the image-credits appendix"}
                   for o, c in zip(by_flow, credits)],
        "redactions": [{"article": a, "page": p, "kind": k, "count": n} for (a, p, k), n in sorted(rc.items())],
        "redactionNote": "Real e-mail addresses and phone numbers are replaced with '[e-mail redacted]' / '[phone number redacted]'. "
                         "Placeholder addresses in example configuration (" + ", ".join(sorted(PLACEHOLDER_EMAILS)) + ") are kept.",
        "notIngested": ["The 'License' page's full GFDL text is not in the export: it names the licence and links to it.",
                        "No talk or user pages are in the export, so there are no reader comments to exclude."],
    }
    with open(os.path.join(OUT, "book.json"), "w", encoding="utf-8") as f:
        json.dump(book, f, indent=1, ensure_ascii=False)
        f.write("\n")
    with open(os.path.join(OUT, "manifest.jsonld"), "w", encoding="utf-8") as f:
        json.dump({"@context": "https://litlfred.github.io/folio-assistant/ns/content/v1.jsonld", "@id": f"{ENTRY}/manifest",
                   "@type": ["folio:SourceDocument"], "title": book["title"] + " (iHRIS wiki export, 2010-09-17)",
                   "contains": [f"{ENTRY}/sections/{a['id']}" for a in art_recs], "provenance": "ingested",
                   "meta": {"doc_id": st["doc_id"], "source_file": man["file"], "source_sha256": man["sha256"], "document_class": "wiki-export",
                            "licence": "GFDL-1.2 (text); images with the owner's permission",
                            "disposition": "ingested: one section per wiki article, images extracted; the PDF is held in uploads/ (git-ignored)"}},
                  f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"{len(art_recs)} articles, {len(book['images'])} images, {sum(r['count'] for r in book['redactions'])} redactions")


if __name__ == "__main__":
    main()
