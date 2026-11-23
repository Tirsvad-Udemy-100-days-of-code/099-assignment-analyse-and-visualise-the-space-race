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
        "import plotly.io as pio",
        "",
        "from space_race import analysis, charts",
        "from space_race.cleaning import clean_missions",
        "from space_race.exploration import explore",
        "from space_race.loading import load_missions",
    ),
    md("### Notebook Presentation"),
    md(
        "Charts are shown as pictures so they appear the same everywhere.",
        "Use `pio.renderers.default = 'browser'` to get interactive charts.",
    ),
    code(
        "pd.options.display.float_format = '{:,.2f}'.format",
        "pio.renderers.default = 'png'",
    ),
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
    step(
        "04-launches-per-organisation-and-rocket-status",
        "## Number of Launches per Organisation",
        "",
        "Which organisations launched the most, how many of the rockets are",
        "still active, and how did the missions end?",
    ),
    code(
        "per_organisation = analysis.launches_per_organisation(df_data)",
        "charts.bar_chart(",
        "    per_organisation.head(15),",
        "    'Launches per organisation (top 15)',",
        "    'Launches',",
        "    'Organisation',",
        "    horizontal=True,",
        ").show()",
    ),
    code(
        "rocket_status = analysis.rocket_status_counts(df_data)",
        "charts.pie_chart(rocket_status, 'Rocket status').show()",
        "mission_status = analysis.mission_status_counts(df_data)",
        "charts.pie_chart(mission_status, 'Mission status').show()",
    ),
    step(
        "05-launch-prices-and-money-spent",
        "## Launch Prices and Money Spent",
        "",
        "Only a fifth of the launches have a published price, so these",
        "figures cover the known prices only (USD millions).",
    ),
    code(
        "prices = analysis.known_prices(df_data)",
        "print(f'Launches with a known price: {len(prices)} of {len(df_data)}')",
        "charts.histogram(",
        "    prices, 'Distribution of launch prices', 'Price (USD millions)'",
        ").show()",
    ),
    code(
        "spent = analysis.money_spent_per_organisation(df_data)",
        "charts.bar_chart(",
        "    spent.head(10),",
        "    'Money spent per organisation',",
        "    'USD millions',",
        "    'Organisation',",
        "    horizontal=True,",
        ").show()",
    ),
    code(
        "average = analysis.average_price_per_organisation(df_data)",
        "charts.bar_chart(",
        "    average.head(10),",
        "    'Average price per launch',",
        "    'USD millions',",
        "    'Organisation',",
        "    horizontal=True,",
        ").show()",
    ),
    step(
        "06-launches-per-year-month-and-over-time",
        "## Launches per Year and per Month",
        "",
        "How did the number of launches change, which month is the most",
        "popular, and did launches become cheaper?",
    ),
    code(
        "per_year = analysis.launches_per_year(df_data)",
        "print(f'Most launches in one year: {per_year.idxmax()} ({per_year.max()})')",
        "charts.line_chart(per_year, 'Launches per year', 'Year', 'Launches').show()",
    ),
    code(
        "per_month = analysis.launches_per_month(df_data)",
        "print(f'Most popular month: {analysis.most_popular_month(df_data)}')",
        "charts.bar_chart(",
        "    per_month, 'Launches per month', 'Month', 'Launches'",
        ").show()",
    ),
    code(
        "price_over_time = analysis.average_price_per_year(df_data)",
        "charts.line_chart(",
        "    price_over_time, 'Average launch price per year', 'Year', 'USD millions'",
        ").show()",
    ),
    step(
        "07-country-analysis-with-choropleth-maps",
        "## Launches and Failures per Country",
        "",
        "Countries are shaded by the number of launches, using ISO 3166 codes.",
    ),
    code(
        "per_country = analysis.launches_per_country(df_data)",
        "charts.choropleth(per_country, 'Launches per country').show()",
    ),
    code(
        "failed_per_country = analysis.failures_per_country(df_data)",
        "charts.choropleth(",
        "    failed_per_country, 'Failed launches per country'",
        ").show()",
    ),
    step(
        "08-sunburst-chart",
        "## Sunburst Chart: Country, Organisation and Mission Status",
    ),
    code(
        "charts.sunburst_chart(",
        "    analysis.sunburst_data(df_data), 'Country, organisation, status'",
        ").show()",
    ),
    step(
        "09-organisations-and-countries-over-time",
        "## Organisations and Countries over Time",
        "",
        "Which organisation launched the most in each year, and how did the",
        "USA and the USSR compare during the Space Race (1957 to 1991)?",
    ),
    code(
        "top_per_year = analysis.top_organisation_per_year(df_data)",
        "charts.grouped_bar_chart(",
        "    top_per_year,",
        "    'Year',",
        "    'Organisation',",
        "    'Organisation with most launches per year',",
        "    stacked=True,",
        ").show()",
    ),
    code(
        "cold_war = analysis.cold_war_launches(df_data)",
        "print(cold_war.groupby('Side')['Launches'].sum())",
        "charts.grouped_bar_chart(",
        "    cold_war, 'Year', 'Side', 'USA against USSR: launches per year'",
        ").show()",
    ),
    code(
        "cold_war_failures = analysis.cold_war_launches(df_data, failures_only=True)",
        "charts.grouped_bar_chart(",
        "    cold_war_failures, 'Year', 'Side', 'USA against USSR: failures per year'",
        ").show()",
    ),
    step(
        "10-mission-safety-over-time",
        "## Have Missions Become Safer?",
        "",
        "The failure rate is the share of launches that did not end in Success.",
    ),
    code(
        "failure_rate = analysis.failure_rate_per_year(df_data)",
        "charts.line_chart(",
        "    failure_rate, 'Failure rate per year', 'Year', 'Share of launches'",
        ").show()",
        "analysis.failure_rate_per_decade(df_data)",
    ),
    md(
        "**Answer:** yes. About two thirds of the launches of the 1950s did not",
        "succeed, a fifth in the 1960s, and since the 1970s fewer than one in",
        "ten fail.",
    ),
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
