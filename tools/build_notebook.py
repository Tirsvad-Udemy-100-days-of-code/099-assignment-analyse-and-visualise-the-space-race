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


def step(slug: str, text: str) -> nbformat.NotebookNode:
    """!
    @brief Make the markdown cell that opens a lecture step.

    @param slug Step name used in the screenshot file name.
    @param text Markdown of the cell.
    @return The cell, tagged with the step slug.
    """
    cell = new_markdown_cell(text)
    cell.metadata["step"] = slug
    return cell


CELLS = [
    new_markdown_cell(
        "# Analyse and Visualise the Space Race\n\n"
        "Day 99 assignment of the 100 Days of Code Python bootcamp. "
        "The data was scraped from nextspaceflight.com and holds the space "
        "missions since 1957."
    ),
    new_markdown_cell("### Import Statements"),
    new_code_cell(
        "import pandas as pd\n\n"
        "from space_race.cleaning import clean_missions\n"
        "from space_race.exploration import explore\n"
        "from space_race.loading import load_missions"
    ),
    new_markdown_cell("### Notebook Presentation"),
    new_code_cell("pd.options.display.float_format = '{:,.2f}'.format"),
    new_markdown_cell("### Load the Data"),
    new_code_cell("df_data = load_missions()"),
    step(
        "01-preliminary-data-exploration",
        "# Preliminary Data Exploration\n\n"
        "* What is the shape of `df_data`?\n"
        "* How many rows and columns does it have?\n"
        "* What are the column names?\n"
        "* Are there any NaN values or duplicates?",
    ),
    new_code_cell(
        "facts = explore(df_data)\n"
        "print(f'Shape: {df_data.shape}')\n"
        "print(f'Rows: {facts.row_count}, columns: {facts.column_count}')\n"
        "print(f'Columns: {facts.column_names}')\n"
        "print(f'Missing values per column: {facts.missing_by_column}')\n"
        "print(f'Duplicate rows: {facts.duplicate_count}')"
    ),
    new_code_cell("df_data.head()"),
    step(
        "02-data-cleaning",
        "## Data Cleaning - Check for Missing Values and Duplicates\n\n"
        "Remove the junk index columns and the duplicate row, make `Price` "
        "numeric (USD millions, missing stays missing), parse the dates and "
        "add the launching country.",
    ),
    new_code_cell(
        "df_data = clean_missions(df_data)\n"
        "print(f'Shape after cleaning: {df_data.shape}')\n"
        "df_data.isna().sum()"
    ),
    new_code_cell("df_data.head()"),
    step(
        "03-descriptive-statistics",
        "## Descriptive Statistics",
    ),
    new_code_cell("df_data.describe(include='all')"),
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
