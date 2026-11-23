"""@file test_charts.py
@brief Tests for the figure builders; skipped when plotly is not installed.
"""

import pytest

pytest.importorskip("pandas")
pytest.importorskip("plotly")

import pandas as pd  # noqa: E402

from space_race import analysis, charts  # noqa: E402


def test_bar_chart_has_one_bar_per_category(df_data: pd.DataFrame) -> None:
    """@brief The figure holds the counts and the titles."""
    data = analysis.launches_per_organisation(df_data)
    fig = charts.bar_chart(
        data, "Launches", "Launches", "Organisation", horizontal=True
    )
    assert list(fig.data[0].x) == list(data.to_numpy())
    assert fig.layout.title.text == "Launches"
    vertical = charts.bar_chart(data, "Launches", "Organisation", "Launches")
    assert list(vertical.data[0].x) == list(data.index)


def test_line_pie_and_histogram_are_built(df_data: pd.DataFrame) -> None:
    """@brief Each builder returns a figure with data."""
    years = analysis.launches_per_year(df_data)
    assert len(charts.line_chart(years, "Year", "Year", "Launches").data) == 1
    status = analysis.mission_status_counts(df_data)
    assert charts.pie_chart(status, "Status").data[0].type == "pie"
    prices = analysis.known_prices(df_data)
    assert (
        charts.histogram(prices, "Prices", "USD millions").data[0].type == "histogram"
    )


def test_choropleth_and_sunburst_are_built(df_data: pd.DataFrame) -> None:
    """@brief The map uses the country codes; the sunburst has all launches."""
    world = charts.choropleth(analysis.launches_per_country(df_data), "Map")
    assert set(world.data[0].locations) == {"USA", "KAZ", "RUS", "CHN"}
    ring = charts.sunburst_chart(analysis.sunburst_data(df_data), "Ring")
    assert ring.data[0].type == "sunburst"


def test_grouped_bar_chart_stacks_when_asked(df_data: pd.DataFrame) -> None:
    """@brief Grouped is the default; stacked sets the bar mode."""
    table = analysis.cold_war_launches(df_data)
    assert (
        charts.grouped_bar_chart(table, "Year", "Side", "Cold War").layout.barmode
        == "group"
    )
    stacked = charts.grouped_bar_chart(table, "Year", "Side", "Cold War", stacked=True)
    assert stacked.layout.barmode == "relative"
