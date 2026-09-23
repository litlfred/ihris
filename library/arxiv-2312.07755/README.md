# Designing with Language: Wireframing UI Design Intent with Generative LLMs (WireGen)

Feng, Yuan, Chen, Xing and Chen. arXiv:2312.07755v1 [cs.HC], 12 Dec 2023. 21 pages.

> **Reference only.** The PDF states no licence, so this entry holds the section headings and page ranges ([`structure.json`](structure.json)) and the summary below, written in our own words. The PDF itself is in `uploads/arxiv-2312.07755/`, which is git-ignored; [`manifest.json`](../../uploads/arxiv-2312.07755/manifest.json) pins it by MD5 and SHA-256.

## What it claims

A short natural-language statement of **design intent** can drive the generation of a **mid-fidelity wireframe**. A mid-fidelity wireframe is monochrome, but it carries real content, semantic icons and interactive elements, rather than the boxes and placeholder text of a low-fidelity sketch. The authors fine-tune a generative LLM on pairs of UI screens (Rico, Android) and screen summaries (Screen2Words). The screens are expressed as an HTML-like, UI-specific language. The raw output is then post-processed into a usable wireframe: semantic icons, typography, and UI guideline rules. The abstract reports 77.5% of wireframes rated significantly better, outperforming two in-context-learning baselines. It also reports a user study with five designers that supports its practical usefulness.

## What this folio takes from it (method, not results)

| from the paper (section) | how we use it |
|---|---|
| Design intent written as a short description, before any drawing (§3, §5.2) | Every wireframe candidate starts from a written **intent statement**, and that statement is the criterion it is judged against. |
| Mid-fidelity: real content and semantic icons, not lorem ipsum (§3.1.1, §3.3) | Wireframes for the data-model site use **real iHRIS content**: actual form classes, fields and lists. |
| Output as HTML, post-processed against UI guidelines (§3.3) | Wireframes are HTML pages, checked mechanically before anyone judges them. |
| Blind, independent raters comparing shuffled candidates against the description (§4.3) | Reviewers see candidates without knowing who or what produced them. Disagreement goes to **adjudication**. |
| Rating relatedness to the description, usefulness and diversity (§5.2) | Review criteria: *intent-fit*, *usability*, and *alternatives considered*. |
| Iterative, conversational refinement (§6) | Rounds of candidate → review → adjudication, each recorded. |
| **Limitation:** trained and evaluated on mobile screens only (§3.1.1) | We require **both web and mobile layouts** in every usability review. |

These uses are ours. The paper evaluates a generator; it does not propose a review or adjudication process. Its reported numbers are about its own model and datasets, and nothing here depends on them.

## Sections

See [`structure.json`](structure.json). There are 23 sections from the embedded outline: Introduction, Related Work (2.1 to 2.3), Approach (3.1 to 3.3), Evaluation (4.1 to 4.5), User Study (5.1 to 5.3), Discussion, Conclusion and References.
