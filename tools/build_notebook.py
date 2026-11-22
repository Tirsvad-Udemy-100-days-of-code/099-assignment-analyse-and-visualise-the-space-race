"""@file build_notebook.py
@brief Write the analysis notebook from its cell list.

Run from the repository root: python tools/build_notebook.py
Every markdown cell that starts a lecture step carries the metadata key
`step`; tools/capture_steps.py uses it to make one screenshot per step.
"""

from pathlib import Path

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

NOTEBOOK_PATH = Path("notebooks") / "space_missions_analysis.ipynb"
## Separator of the lines of a cell.
LINE_BREAK = chr(10)


def md(*lines: str) -> nbformat.NotebookNode:
    """!
    @brief Make a markdown cell from lines of text.

    @param lines The lines, joined with line breaks.
    @return The cell.
    """
    return new_markdown_cell(LINE_BREAK.join(lines))


def code(*lines: str) -> nbformat.NotebookNode:
    """!
    @brief Make a code cell from lines of code.

    @param lines The lines, joined with line breaks.
    @return The cell.
    """
    return new_code_cell(LINE_BREAK.join(lines))


def step(slug: str, *lines: str) -> nbformat.NotebookNode:
    """!
    @brief Make the markdown cell that opens a lecture step.

    @param slug Step name used in the screenshot file name.
    @param lines The lines of the cell.
    @return The cell, tagged with the step slug.
    """
    cell = md(*lines)
    cell.metadata["step"] = slug
    return cell


CELLS = [
    md(
        "# Analyse and Visualise the Space Race",
        "",
        "Day 99 assignment of the 100 Days of Code Python bootcamp.",
        "The data was scraped from nextspaceflight.com and holds the space",
        "missions since 1957.",
    ),
    md("### Import Statements"),
    code(
        "import pandas as pd",
        "",
        "from space_race.cleaning import clean_missions",
        "from space_race.exploration import explore",
        "from space_race.loading import load_missions",
    ),
    md("### Notebook Presentation"),
    code("pd.options.display.float_format = '{:,.2f}'.format"),
    md("### Load the Data"),
    code("df_data = load_missions()"),
    step(
        "01-preliminary-data-exploration",
        "# Preliminary Data Exploration",
        "",
        "* What is the shape of `df_data`?",
        "* How many rows and columns does it have?",
        "* What are the column names?",
        "* Are there any NaN values or duplicates?",
    ),
    code(
        "facts = explore(df_data)",
        "print(f'Shape: {df_data.shape}')",
        "print(f'Rows: {facts.row_count}, columns: {facts.column_count}')",
        "print(f'Columns: {facts.column_names}')",
        "print(f'Missing values per column: {facts.missing_by_column}')",
        "print(f'Duplicate rows: {facts.duplicate_count}')",
    ),
    code("df_data.head()"),
    step(
        "02-data-cleaning",
        "## Data Cleaning - Check for Missing Values and Duplicates",
        "",
        "Remove the junk index columns and the duplicate row, make `Price`",
        "numeric (USD millions, missing stays missing), parse the dates and",
        "add the launching country.",
    ),
    code(
        "df_data = clean_missions(df_data)",
        "print(f'Shape after cleaning: {df_data.shape}')",
        "df_data.isna().sum()",
    ),
    code("df_data.head()"),
    step("03-descriptive-statistics", "## Descriptive Statistics"),
    code("df_data.describe(include='all')"),
]


def main() -> None:
    """!
    @brief Write the notebook file.
    """
    notebook = new_notebook(cells=CELLS)
    notebook.metadata["kernelspec"] = {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3",
    }
    NOTEBOOK_PATH.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(notebook, NOTEBOOK_PATH)


if __name__ == "__main__":
    main()
