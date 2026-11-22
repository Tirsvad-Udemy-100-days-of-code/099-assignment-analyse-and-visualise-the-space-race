# Data preparation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after RC-005 (Go) | pending |

---

## Purpose

Decide whether the data set is understood and clean enough to analyse: lecture steps preliminary exploration and data cleaning.

## Deliverable

A tested loading and cleaning module, a notebook section for each of the two steps with its screenshot, and a recorded checksum of the data file.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The data file is loaded by a function in `src/` with tests | Tests pass | No tests or failing tests |
| 2 | Missing values, duplicates and the price column are handled and each decision is written in the notebook | All three handled | Any unhandled |
| 3 | The notebook runs top to bottom without error | No error | Any error |
| 4 | A screenshot exists for each step of this milestone | All present | Any missing |
| 5 | The raw data file is not committed unless its licence allows it | Confirmed | Unconfirmed |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Needs the repository structure and tooling |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| BC-001 Objectives 1, 2, 3; Success Criteria 1, 2 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-12-06 — within the Business Case target end of 2026-12-20.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Obtain the data set and read the start notebook | Get the course zip (the download link is signed and may have expired; S01 supplies the file if so), open the start notebook, list the assignment's steps and the function names S02 expects, and record the data file's checksum. Check the data licence before deciding whether the file goes in the repository. | No |  |
| 2 | Implement the data loading function | Write a documented function in `src/` that reads the CSV into a data frame, with constants for the column names and file path in `constants.py`, and tests that use a small sample file. | No |  |
| 3 | Preliminary data exploration step | Show the shape, columns, data types, missing values and duplicates, as the first lecture step asks. Capture the screenshot. Serves S02. | No |  |
| 4 | Data cleaning step | Convert the price to a number, parse the launch date, split location into country, remove the stray index column, and decide what to do with missing prices. Each cleaning function has tests. Capture the screenshot. | No |  |
| 5 | Create the notebook scaffold and screenshot method | Create the Jupyter notebook with one section per lecture step, and a repeatable headless way to render each result to an image, so no screenshot needs the host desktop (framework GUI-testing rule). | No |  |

---

[BC-001]: ../business-case.md
