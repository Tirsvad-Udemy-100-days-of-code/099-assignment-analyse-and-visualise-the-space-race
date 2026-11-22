# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-002 |
| CrossReference | [SA-001], [QC-SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [a2af282] |

---

## Artifact Under Review

- Instance reviewed: [SA-001]
- Checklist used: [QC-SA-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is the stand-in for S01, who is also the Product Owner; S01 re-checks it in the end-of-run summary)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Power/Interest grid is filled for every stakeholder, with no gaps or unclassified entries | Pass | S01, S02 and S03 all have Power, Interest and Quadrant. |
| 2 | Each stakeholder is assigned a unique, stable ID (e.g. S01-S11 style) reusable for RACI assignments in other artifacts | Pass | IDs S01 to S03. |
| 3 | Roles and organizational context are defined with explicit Power and Interest levels, not just narrative description | Pass | Role, organisation, Power and Interest are given as levels. |
| 4 | Communication needs (channel, frequency, deliverable type) are mapped to project phases or milestones | Pass | Communication table CM-001 to CM-003 names channel, frequency, deliverable and milestone. |
| 5 | Conflicting stakeholder interests are identified with documented mitigation or resolution strategies | Pass | One conflict (notebook libraries against no runtime dependencies) with a mitigation. |
| 6 | Stakeholder concerns are explicitly traced to Business Case objectives | Pass | The Business Goal Alignment table maps each stakeholder to Business Case objectives. |
| 7 | Primary concerns are expressed in both business language and a recognized quality-attribute mapping (e.g. FURPS+) | Pass | Concerns CN-001 to CN-007 carry a FURPS+ attribute. |
| 8 | Document is understandable and navigable by non-technical stakeholders reviewing their own entry | Pass | Short table, plain wording. |
| 9 | Every concern has a stable ID (`CN-NNN`) in the concern register, with the stakeholder who raised it; IDs are never renumbered or reused | Pass | CN-001 to CN-007 each name the raising stakeholder. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has `Language | en` and `Domain | it`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register 'IT Professional English' matches the registry row for this type. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No domain dictionary (`DICT`) exists yet; the same term is used throughout (for example 'milestone', 'gateway', 'data frame'), with no synonym pairs. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists beside the file. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | Initial version; no change of language or domain. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | Stand-in review: S01 reads English and works in the IT domain; no language reviewer is needed (`none`). |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations (for example ISO, IEC, FURPS+, MIL) are standard English terms, explained where first used or defined by the framework. |

## Overall Verdict

Go — every Mandatory criterion of QC-SA-001 and of QC-LANG-001 passes; the review is a stand-in review and not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | n/a |

---


[SA-001]: ../../stakeholder-analysis.md
[QC-SA-001]: ../../../framework/qc/artifacts/qc-stakeholder-analysis.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[a2af282]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/commit/a2af2824cad60b6814f7e783c4efa3c416b4b080
