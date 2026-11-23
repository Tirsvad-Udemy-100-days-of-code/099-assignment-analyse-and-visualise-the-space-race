"""@file test_exploration_and_cleaning.py
@brief Tests for the exploration and cleaning steps.
"""

from pathlib import Path

import pytest

pytest.importorskip("pandas")

import pandas as pd  # noqa: E402

from space_race import cleaning, constants  # noqa: E402
from space_race.exploration import explore  # noqa: E402
from space_race.loading import load_missions  # noqa: E402

SAMPLE = Path(__file__).parent.parent / "data" / "sample_missions.csv"


@pytest.fixture
def df_data() -> pd.DataFrame:
    """@brief The raw sample data."""
    return load_missions(SAMPLE)


def test_explore_reports_shape_missing_and_duplicates(df_data: pd.DataFrame) -> None:
    """@brief The exploration answers the questions of the lecture step."""
    result = explore(df_data)
    assert (result.row_count, result.column_count) == (6, 9)
    assert result.missing_by_column == {"Price": 3}
    assert result.duplicate_count == 1
    assert result.column_names[2] == "Organisation"


def test_drop_junk_columns_removes_index_columns(df_data: pd.DataFrame) -> None:
    """@brief Both row-index columns are removed."""
    result = cleaning.drop_junk_columns(df_data)
    assert not set(constants.JUNK_COLUMNS) & set(result.columns)
    assert "Organisation" in result.columns


def test_drop_duplicates_keeps_first(df_data: pd.DataFrame) -> None:
    """@brief The repeated launch is kept once."""
    result = cleaning.drop_duplicates(cleaning.drop_junk_columns(df_data))
    assert len(result) == 5


def test_convert_price_handles_separator_and_missing(df_data: pd.DataFrame) -> None:
    """@brief Thousands separators go, missing prices stay NaN."""
    result = cleaning.convert_price(df_data)
    assert result["Price"].dtype == "float64"
    assert result["Price"].iloc[2] == pytest.approx(1160.0)
    assert result["Price"].isna().sum() == 3


def test_parse_dates_with_and_without_time(df_data: pd.DataFrame) -> None:
    """@brief Both date formats parse; a date without time gets midnight."""
    result = cleaning.parse_dates(df_data)
    assert result["Year"].tolist() == [2020, 2020, 2019, 2006, 1964, 1964]
    assert result["Launch_Time"].iloc[2].hour == 0
    assert result["Month"].iloc[0] == 8


def test_parse_dates_rejects_unknown_format() -> None:
    """@brief An unsupported date raises ValueError that names the text."""
    df_data = pd.DataFrame({"Date": ["not a date"]})
    with pytest.raises(ValueError, match="not a date"):
        cleaning.parse_dates(df_data)


def test_add_country_uses_standard_names(df_data: pd.DataFrame) -> None:
    """@brief Country names are mapped to ISO 3166 names."""
    result = cleaning.add_country(df_data)
    assert result["Country"].tolist() == [
        "United States of America",
        "China",
        "Kazakhstan",
        "United States of America",
        "Russian Federation",
        "Russian Federation",
    ]


def test_clean_missions_runs_every_step(df_data: pd.DataFrame) -> None:
    """@brief The pipeline gives one row fewer and all new columns."""
    result = cleaning.clean_missions(df_data)
    assert len(result) == 5
    assert {"Country", "Launch_Time", "Year", "Month"} <= set(result.columns)
    assert "Unnamed: 0" not in result.columns
