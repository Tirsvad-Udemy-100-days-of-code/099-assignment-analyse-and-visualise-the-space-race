# Repository baseline

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after RC-004 (Go) | pending |

---

## Purpose

Decide whether the repository is ready to take analysis code: structure, tooling, documentation skeleton and metadata are in place.

## Deliverable

A cloneable repository with `src/`, `tests/`, `docs/`, `pyproject.toml`, `constants.py`, a Python `.gitignore`, a Doxyfile, a README from the framework template that explains the local `.venv`, and a description and topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pip install -e .` and `pytest` succeed in a new `.venv` on Python 3.14 or newer | Both exit 0 | Either fails |
| 2 | `dependencies` in `pyproject.toml` is empty | Empty | Any runtime dependency listed |
| 3 | The README follows the framework template and documents `.venv`, `python -m pip install --upgrade pip`, run and test | All present | Any missing |
| 4 | Repository description and at least 5 topics are visible on the git host | Visible | Missing |
| 5 | opengrep reports no findings | 0 findings | Any open finding |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First gateway |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| BC-001 Objective 5; Success Criteria 1, 4, 5, 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-29 — within the Business Case target end of 2026-12-20.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Set repository description and topics | Set a one-line description and topics (for example python, jupyter, pandas, plotly, data-visualization, udemy, 100-days-of-code, space-race) on the Gitea repository through its API, with the token read from `.env` by hand. The project never imports or tests `.env`. Serves S03. | No |  |
| 2 | Create project layout and pyproject.toml | Create `src/` and `tests/` with a package, `pyproject.toml` (requires-python 3.14 or newer, no runtime dependencies, optional extra `notebook` for the analysis libraries, extra `dev` for pytest), and `constants.py` for all constants. Follows the framework's folder-structure rules. | No |  |
| 3 | Add Python .gitignore and editorconfig | Add a Python `.gitignore` that also ignores `.env`, `.venv`, data downloads and notebook checkpoints, and the root `.editorconfig` from the framework baseline template. | No |  |
| 4 | Add Doxyfile and Doxygen comment convention | Add a Doxyfile for `src/` and write the first Doxygen-commented module so the convention is set for later tasks. | No |  |
| 5 | Write README with venv instructions | Create the README from the framework template: create and use a local `.venv`, `python -m pip install --upgrade pip`, install, run the notebook, run the tests, and the project documents appendix. Serves S02 and S03. | No |  |
| 6 | Document the local opengrep check | Document the command for the local opengrep run (`~\.opengrep\cli\latest\opengrep.exe`) before each push and run it on the baseline. The outcome must be zero open findings. | No |  |

---

[BC-001]: ../business-case.md
