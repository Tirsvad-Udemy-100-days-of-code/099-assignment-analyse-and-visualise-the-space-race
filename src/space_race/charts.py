"""@file charts.py
@brief Plotly figures for the analysis steps.

Needs the optional `notebook` extra (plotly). The functions only build a figure;
the notebook shows it.
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from space_race.analysis import LAUNCHES
from space_race.constants import (
    COL_COUNTRY,
    COL_COUNTRY_CODE,
    COL_MISSION_STATUS,
    COL_ORGANISATION,
)

## Default width of a figure in pixels.
FIGURE_WIDTH: int = 1000
## Default height of a figure in pixels.
FIGURE_HEIGHT: int = 500


def _finish(fig: go.Figure, title: str) -> go.Figure:
    """!
    @brief Give a figure its title and the common size.

    @param fig The figure.
    @param title Title shown above the chart.
    @return The same figure.
    """
    fig.update_layout(title=title, width=FIGURE_WIDTH, height=FIGURE_HEIGHT)
    return fig


def bar_chart(
    data: pd.Series, title: str, x_label: str, y_label: str, *, horizontal: bool = False
) -> go.Figure:
    """!
    @brief Draw a bar chart of a series.

    @param data Values indexed by the category.
    @param title Chart title.
    @param x_label Label of the horizontal axis.
    @param y_label Label of the vertical axis.
    @param horizontal Draw horizontal bars, the first value on top.
    @return The figure.
    """
    if horizontal:
        fig = px.bar(x=data.to_numpy(), y=data.index.astype(str), orientation="h")
        fig.update_yaxes(autorange="reversed")
    else:
        fig = px.bar(x=data.index.astype(str), y=data.to_numpy())
    fig.update_layout(xaxis_title=x_label, yaxis_title=y_label)
    return _finish(fig, title)


def line_chart(data: pd.Series, title: str, x_label: str, y_label: str) -> go.Figure:
    """!
    @brief Draw a line chart of a series.

    @param data Values indexed by the x value (for example the year).
    @param title Chart title.
    @param x_label Label of the horizontal axis.
    @param y_label Label of the vertical axis.
    @return The figure.
    """
    fig = px.line(x=data.index, y=data.to_numpy(), markers=True)
    fig.update_layout(xaxis_title=x_label, yaxis_title=y_label)
    return _finish(fig, title)


def pie_chart(data: pd.Series, title: str) -> go.Figure:
    """!
    @brief Draw a donut chart of a series.

    @param data Counts indexed by the category.
    @param title Chart title.
    @return The figure.
    """
    fig = px.pie(names=data.index.astype(str), values=data.to_numpy(), hole=0.4)
    return _finish(fig, title)


def histogram(data: pd.Series, title: str, x_label: str, bins: int = 30) -> go.Figure:
    """!
    @brief Draw a histogram of values.

    @param data The values.
    @param title Chart title.
    @param x_label Label of the horizontal axis.
    @param bins Number of bins.
    @return The figure.
    """
    fig = px.histogram(x=data.to_numpy(), nbins=bins)
    fig.update_layout(xaxis_title=x_label, yaxis_title="Number of launches")
    return _finish(fig, title)


def choropleth(counts: pd.DataFrame, title: str) -> go.Figure:
    """!
    @brief Draw a world map shaded by the launches of each country.

    @param counts Table from `launches_per_country` or `failures_per_country`.
    @param title Chart title.
    @return The figure.
    """
    fig = px.choropleth(
        counts,
        locations=COL_COUNTRY_CODE,
        color=LAUNCHES,
        hover_name=COL_COUNTRY,
        color_continuous_scale="matter",
    )
    return _finish(fig, title)


def sunburst_chart(counts: pd.DataFrame, title: str) -> go.Figure:
    """!
    @brief Draw the ring chart of country, organisation and mission status.

    @param counts Table from `sunburst_data`.
    @param title Chart title.
    @return The figure.
    """
    fig = px.sunburst(
        counts,
        path=[COL_COUNTRY, COL_ORGANISATION, COL_MISSION_STATUS],
        values=LAUNCHES,
    )
    return _finish(fig, title)


def grouped_bar_chart(
    table: pd.DataFrame, x: str, colour: str, title: str, *, stacked: bool = False
) -> go.Figure:
    """!
    @brief Draw bars of the launch counts, split by a second column.

    @param table Table with the x column, the colour column and Launches.
    @param x Column on the horizontal axis.
    @param colour Column that splits each bar (for example the side).
    @param title Chart title.
    @param stacked Stack the parts instead of placing them side by side.
    @return The figure.
    """
    fig = px.bar(table, x=x, y=LAUNCHES, color=colour)
    fig.update_layout(barmode="relative" if stacked else "group")
    return _finish(fig, title)
