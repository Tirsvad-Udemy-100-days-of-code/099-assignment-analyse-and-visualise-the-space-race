# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [a2af282] |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after RC-001 (Go) | [a2af282] |

---

## Executive Summary

The project solves the Day 99 assignment of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp": analyse and visualise the space missions listed on nextspaceflight.com from 1957 onwards. It is delivered as a Jupyter notebook backed by a small, tested Python package, a README and a wiki in three languages, with a screenshot for every lecture step. The result is a readable, runnable reference for fellow course participants and a clear portfolio repository for visitors. The effort is a few weeks of part-time work with no budget. The recommendation is to proceed.

## Methodological and Standards Foundation

- Plan-first delivery with reviewed artifacts, as set by the SQA and QC framework mounted in `framework/`.
- Quality characteristics follow ISO/IEC 25010:2023 (maintainability, usability, portability, functional suitability).
- Code follows the framework's Python conventions and Clean Architecture layering; source comments use Doxygen.
- Tests use pytest; the environment is a local `venv`.

## Problem Statement

The assignment gives a data set and open questions but no worked solution that is readable, tested and documented step by step. A participant who is stuck, or who wants to compare answers, finds loose notebooks without instructions, without explanation of what each step teaches, and often without a way to run them. The belief that would kill the idea if false: **other participants and visitors find a documented, runnable solution more useful than a bare notebook.** The idea is a hunch, not yet validated by behaviour; because the project is cheap to build, the Product Owner has chosen to build it without a separate test of that belief.

## Business Opportunity

The course has thousands of student solutions for this assignment. A solution that runs from a fresh clone with three commands, shows what every step produces, and explains what was learnt, stands out in a portfolio and gives the Product Owner a worked example of project discipline.

## Objectives

1. Answer the assignment's questions (launches per year and organisation, cost over time, popular months, safety over time) with correct, reproducible analysis.
2. Deliver the analysis as a Jupyter notebook that uses tested functions from `src/`.
3. Show the output of every lecture step as a screenshot in the README and in the wiki.
4. Explain in the wiki, in English, Danish and Bahasa Malaysia, what each lecture step taught.
5. Make the repository clear to visitors: description, topics, README and run instructions.

## Scope

### In Scope

- Loading, exploring and cleaning the nextspaceflight.com data set supplied with the assignment.
- Every analysis and chart the assignment asks for, including the choropleth, sunburst and segmented bar charts, plus the reflection journal.
- A Python package in `src/` (Python 3.14 or newer, constants in `constants.py`), tests in `tests/`, `pyproject.toml`, a Python `.gitignore`, a Doxyfile and Doxygen comments.
- Documentation of how to create and use a local `.venv`, upgrade `pip`, run the notebook and run the tests.
- README from the framework template, and a wiki in English, Danish and Bahasa Malaysia (flat pages, one file per language).
- A screenshot per lecture step.
- Repository description and topics on the git host.
- A local static-analysis pass with opengrep before every push.

### Out of Scope

- Any change to the framework in `framework/`.
- A web application, API or database.
- Importing or testing the personal `.env` file; it holds tokens for personal use only and the project never reads it.
- Mentioning or crediting automated assistants in any artifact.
- Languages other than English, Danish and Bahasa Malaysia.

## Expected Benefits

### Tangible Benefits

- A runnable solution of all assignment steps with passing tests.
- A repository that a visitor understands within a minute (description, topics, README).
- Reusable, tested helper functions for cleaning and aggregating the data.

### Intangible Benefits

- Practice in data cleaning, visualisation and project discipline for the Product Owner.
- A learning resource in three languages for participants.

## Strategic Alignment

The project is one step of the Product Owner's learning path through the course and a portfolio entry on the Tirsvad-Udemy-100_days_of_code organisation. It exercises the framework's plan-first workflow on a small, complete project.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | The tests pass from a fresh clone | 100% pass | `pytest` exit code 0 in a new `.venv` |
| 2 | Every lecture step has a screenshot in README and wiki | 100% of steps | A checklist of steps against the images in `docs/` |
| 3 | The wiki exists in three languages with the same page set | 3 languages, 0 missing pages | Page list compared across `en`, `da`, `ms` |
| 4 | Static analysis is clean before each push | 0 open findings | opengrep run output |
| 5 | Runtime dependencies of the package | 0 | `dependencies` list in `pyproject.toml` is empty; notebook libraries are an optional extra |
| 6 | Repository metadata is set | Description and at least 5 topics | Git host repository page |
| 7 | Every public function has a Doxygen comment | 100% | Doxygen run with warnings for undocumented items shows none |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The signed download link for the data set has expired | The data cannot be fetched | The Product Owner supplies the zip; the project stores a checksum, not the link |
| The data licence is unclear | Redistribution is not allowed | Keep the raw file out of the repository if the licence forbids it; document where to get it |
| Plotting libraries are needed by the notebook while visitors expect no runtime dependencies | Conflict between S02 and S03 concerns | Keep the package dependency-free; put notebook libraries in an optional extra `notebook` |
| Screenshots taken on the host desktop take over mouse and keyboard | Disruption; breaks the framework's GUI rule | Render charts headlessly (notebook export, image export) or in a container |
| Python 3.14 is not installed on a participant's machine | The project does not run | State the requirement and the check in the README |
| A token leaks | Account compromise | `.env` is in `.gitignore`; no script or test reads it; opengrep runs before push |

## Assumptions

- The Product Owner and the only reviewer is S01; the people for whom the idea is made cannot be interviewed within this project, so the belief in the Problem Statement stays untested.
- The data set is the one supplied in the assignment's zip file and is stable.
- The git host is `git.tirsystem.com`; the GitHub copy is a mirror of it.
- The Product Owner's domain language is English and the domain is IT.

## Constraints

- Python 3.14 or newer; `venv` for the environment; pytest for tests; constants in `constants.py`; configuration in `pyproject.toml`.
- Folder structure `src/`, `tests/`, `docs/`.
- Work happens on a branch per step and reaches `main` through a pull request.
- No budget; part-time effort by one person; target end 2026-12-20 (to be confirmed by the Product Owner).
- Tokens come from `.env` for personal use only; they are never committed, imported or tested.
- No artifact mentions automated assistants.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About 40 to 60 hours of the Product Owner's time (qualitative estimate) | A complete, documented solution and a portfolio entry |
| No licence or infrastructure cost | Reusable tested helpers and a three-language learning resource |

The assessment is qualitative: the project has no revenue, and a monetary figure would be invented.

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, developer and reviewer: wants a correct solution and a reflection on the learning |
| S02 | Udemy participants: want readable, runnable code with the assignment's function names and clear run instructions |
| S03 | GitHub visitors: want a clear description, topics and README, and no runtime dependencies |

## Recommendation

Proceed — the scope is small, the cost is only the Product Owner's time, and the result is a documented reference that serves all three stakeholders.

---

[SA-001]: ./stakeholder-analysis.md
[a2af282]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/commit/a2af2824cad60b6814f7e783c4efa3c416b4b080
