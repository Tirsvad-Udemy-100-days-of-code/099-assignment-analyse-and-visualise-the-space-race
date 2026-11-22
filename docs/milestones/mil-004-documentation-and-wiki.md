# Documentation and wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after RC-007 (Go) | pending |

---

## Purpose

Decide whether the project can be published as finished: screenshots, README, reflection and the three-language wiki are complete.

## Deliverable

A README with a screenshot for each lecture step, a wiki in English, Danish and Bahasa Malaysia in `docs/wiki/` explaining what each step taught, and the reflection journal.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Every lecture step has a screenshot in the README and in each wiki language | 100% of steps | Any step without |
| 2 | The wiki has the same page set in English, Danish and Bahasa Malaysia, a language line on each page, and a sidebar | Same set | A page missing |
| 3 | Each wiki page explains what was gained in its step | All pages | Any page without |
| 4 | The wiki passes its checklist review | Go | No-Go |
| 5 | The reflection journal answers the assignment's questions | Present | Missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | Needs the finished analysis and its screenshots |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| BC-001 Objectives 3, 4, 5; Success Criteria 2, 3 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-12-20 — within the Business Case target end of 2026-12-20.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Collect screenshots for every lecture step | Gather the screenshots from the earlier milestones into `docs/images/` with a stable naming scheme, and check that no step is missing. | No |  |
| 2 | Complete the README with the step gallery | Add the step-by-step gallery with screenshots to the README, and re-check the run and test instructions from a fresh clone. | No |  |
| 3 | Write the English wiki | Write `docs/wiki/` pages in English (flat folder): Home, one page per lecture step with screenshot and what was gained, setup, and the sidebar. English is the authoritative text. | No |  |
| 4 | Write the Danish wiki | Translate every English page to Danish as `<Page>-da.md`, with the language line on each page. Code, commands and file names stay in English. | No |  |
| 5 | Write the Bahasa Malaysia wiki | Translate every English page to Bahasa Malaysia as `<Page>-ms.md`, with the language line on each page and the same page set. | No |  |
| 6 | Write the reflection journal | Answer the assignment's reflection questions: approach, what was hard and easy, the biggest learning, and what to do differently. | No |  |
| 7 | Run Doxygen and the final checks | Run Doxygen without warnings for undocumented items, the opengrep check and the tests from a fresh clone. | No |  |
| 8 | Check the GitHub mirror metadata | Confirm the description and topics also show on the GitHub mirror, if it exists. | No |  |

---

[BC-001]: ../business-case.md
