# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [a2af282] |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after RC-002 (Go) | [a2af282] |

---

## Purpose

This analysis names the people affected by the project, ranks their power and interest, and fixes who reviews and who accepts each artifact. It uses a power/interest grid; its IDs are used by the Business Case, the Project Plan and the milestones.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A correct, documented solution and a record of what was learnt |
| S02 | Udemy course participants | Users of the shared code | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub visitors | Browsers of the repository | Public | LOW | MEDIUM | Keep Informed | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **S01** decides scope, reviews and accepts every artifact, and does the work: power and interest are both high.
- **S02** cannot change the project but depends on it when comparing solutions: low power, high interest. Their needs shape the code layout and the instructions.
- **S03** is an occasional reader with no influence; interest is medium because they judge the project within seconds.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The analysis answers the assignment's questions correctly | Functionality |
| CN-002 | S01 | Each step is explained and its learning recorded | Functionality, Documentation |
| CN-003 | S02 | Code is readable and uses the assignment's function names | Usability, Supportability |
| CN-004 | S02 | The project runs from a fresh clone with documented commands | Usability, Installability |
| CN-005 | S03 | Clear description, topics and README | Usability |
| CN-006 | S03 | No runtime dependencies in the package | Implementation constraint |
| CN-007 | S01 | Tokens never leave `.env` and the project never reads it | Security |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CM-001 | Pull request review | Per milestone | Reviewed changes merged by S01 | All |
| CM-002 | README and wiki | At each milestone end | Steps with screenshots and explanation | MIL-004 |
| CM-003 | Repository description and topics | Once, updated when scope changes | Visible summary for S03 | MIL-001 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| The notebook needs analysis and plotting libraries, while S03 wants no runtime dependencies | S02, S03 | The package has no runtime dependencies; notebook libraries are an optional extra named `notebook`, installed on request |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001, CN-002 | Objectives 1, 2 and 4 |
| S02 | CN-003, CN-004 | Objectives 2 and 3 |
| S03 | CN-005, CN-006 | Objective 5 |

## Sign-Off

| Stakeholder | Role in sign-off | Status |
| --- | --- | --- |
| S01 | Reviewer and approver of every artifact | Pending |

---

[BC-001]: ./business-case.md
[a2af282]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/commit/a2af2824cad60b6814f7e783c4efa3c416b4b080
