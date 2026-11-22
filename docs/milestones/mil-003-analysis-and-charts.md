# Analysis and charts

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [a2af282] |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after RC-006 (Go) | [a2af282] |

---

## Purpose

Decide whether every question of the assignment has a correct, reproducible answer and chart.

## Deliverable

The notebook sections for all analysis steps, backed by tested functions in `src/`, with one screenshot per step.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Each analysis step has a function in `src/` with at least one test | All steps | Any step untested |
| 2 | The notebook runs top to bottom without error | No error | Any error |
| 3 | Each assignment question (most launches per year, cost over time, popular months, failure over time) is answered in the notebook | All answered | Any unanswered |
| 4 | A screenshot exists for each step | All present | Any missing |
| 5 | opengrep reports no findings | 0 findings | Any open finding |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | Needs the cleaned data |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| BC-001 Objectives 1, 2, 3; Success Criteria 1, 2, 4, 7 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-12-13 — within the Business Case target end of 2026-12-20.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Launches per organisation and rocket status | Count launches per organisation (bar chart) and show active versus retired rockets and the mission status split. Capture the screenshot. | No |  |
| 2 | Launch prices and money spent | Show the distribution of launch prices, the total money spent per organisation and the cost per launch per organisation. Capture the screenshot. | No |  |
| 3 | Launches per year, month and over time | Count launches per year and per month (the most popular month), and show the price over time. Answers who launched most in any year. Capture the screenshot. | No |  |
| 4 | Country analysis with choropleth maps | Show launches per country and failures per country as choropleth maps, using ISO country codes. Capture the screenshot. | No |  |
| 5 | Sunburst chart of country, organisation and status | Build the sunburst chart of country, organisation and mission status. Capture the screenshot. | No |  |
| 6 | Organisations and countries over time | Show the top organisations per year, and the USA versus USSR (Russia) comparison of the Space Race as a segmented bar chart. Capture the screenshot. | No |  |
| 7 | Mission safety over time | Compute the failure rate per year and judge whether missions have become safer. Capture the screenshot. | No |  |

---

[BC-001]: ../business-case.md
[a2af282]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/commit/a2af2824cad60b6814f7e783c4efa3c416b4b080
