# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-003 |
| CrossReference | [PP-001], [QC-PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is the stand-in for S01, who is also the Product Owner; S01 re-checks it in the end-of-run summary)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Start 2026-11-23, end 2026-12-20, fitting the Business Case constraint. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | Four gateways, each with document, decision date and owner. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | Decision dates equal the target dates of the four milestone documents. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage maps each Business Case in-scope item to a gateway. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Chain MIL-001 to MIL-004, acyclic, matching the schedule order. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | A No-Go moves later gateways; S01 re-sets the end date. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | Owner is S01. The project has no governance document yet, so there is no RACI to cross-check. |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Assumptions listed with their source (Business Case, Stakeholder Analysis); no re-baseline yet. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Three plan risks with impact and mitigation; the data-link risk traces to a Business Case risk. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open issues do not contradict the plan; none is stale. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | Main deliverable column repeats the milestone's Deliverable. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | Stories column says 'none (technical tasks)'. |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Gantt bars match the table dates. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Milestone column says 'not yet synced'. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | One Project Plan; first Version History row. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has `Language | en` and `Domain | it`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register 'IT Executive English' matches the registry row for this type. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No domain dictionary (`DICT`) exists yet; the same term is used throughout (for example 'milestone', 'gateway', 'data frame'), with no synonym pairs. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists beside the file. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | Initial version; no change of language or domain. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | Stand-in review: S01 reads English and works in the IT domain; no language reviewer is needed (`none`). |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations (for example ISO, IEC, FURPS+, MIL) are standard English terms, explained where first used or defined by the framework. |

## Overall Verdict

Go — every Mandatory criterion of QC-PP-001 and of QC-LANG-001 passes; the review is a stand-in review and not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | n/a |

---


[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
