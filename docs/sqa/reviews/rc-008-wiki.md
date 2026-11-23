# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [MIL-004], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [e32aa44] |
| 2026-11-23 | Proposed | Jens Tirsvad Nielsen | S01 | Criterion 14 checked on the published wiki | [fd81959] |

---

## Artifact Under Review

- Instance reviewed: the wiki in `docs/wiki/` (MIL-004 tasks 3 to 5)
- Checklist used: [QC-WIKI-001]
- Scope: full review; QC-LANG-001 applies to the language of the pages only, because a wiki page has no Metadata table
- Language and domain: en, da, ms / it
- Language reviewer: none (open action item)
- Mode: autonomous, not independent (the reviewer is the stand-in for S01, who is also the Product Owner; S01 re-checks it in the end-of-run summary)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | `docs/wiki/_Sidebar.md` exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Starts with the bold title, then one English page list with Home first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | All 13 English pages are listed; a link check of every wiki file found no dead link. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | Pass | The wiki has no related wikis, so there is no Related section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Languages is the last section: English, Dansk and Bahasa Malaysia, each linking to its Home page. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | Pass | The sidebar is written by hand and carries a comment that says so. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Every page has the language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English and the PO language (English) exist; Danish and Bahasa Malaysia are added on top. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | 13 English pages each have a `-da` and a `-ms` page (39 pages plus the sidebar). |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Every page starts with the language line, the current language in bold, linking to the same page in the other two. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Translations are named `<Page>-da.md` and `<Page>-ms.md`; English has no suffix. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Code blocks, commands, file names and function names are English in all languages. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pass | Checked on the published wiki on 2026-11-23, after the merge of PR 31: all 40 pages and the sidebar exist and match the repository line for line (only line endings differ), no link is dead, and all 10 screenshots load. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | Pass | Optional; no generator or template is used. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | All 40 files are directly in `docs/wiki/`; there is no subfolder. |

## Overall Verdict

Go — every Mandatory criterion passes, criterion 14 included (checked on the published wiki). The review is a stand-in review and not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Read the Danish and Bahasa Malaysia pages for wording; no native-speaker review has happened | S01 | 2026-12-20 |

---

[MIL-004]: ../../milestones/mil-004-documentation-and-wiki.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[e32aa44]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/commit/e32aa4404f1851913782f6f99bd4ded072f10e6f
[fd81959]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/commit/fd8195954dfa62e2506315c4e9fee8225699a3a4
