"""@file test_analysis.py
@brief Tests for the analysis steps, run on a small hand-made clean data set.
"""

import pytest

pytest.importorskip("pandas")

import pandas as pd  # noqa: E402

from space_race import analysis  # noqa: E402


def test_launches_per_organisation_is_sorted_busiest_first(
    df_data: pd.DataFrame,
) -> None:
    """@brief NASA has three launches, the others have the rest."""
    result = analysis.launches_per_organisation(df_data)
    assert result.iloc[0] == 3
    assert result.index[0] == "NASA"
    assert result.sum() == 8


def test_status_counts(df_data: pd.DataFrame) -> None:
    """@brief Rocket and mission statuses are counted."""
    assert analysis.rocket_status_counts(df_data)["StatusActive"] == 2
    assert analysis.mission_status_counts(df_data)["Success"] == 5


def test_prices_skip_missing_values(df_data: pd.DataFrame) -> None:
    """@brief Money spent and the average only use the known prices."""
    assert len(analysis.known_prices(df_data)) == 5
    spent = analysis.money_spent_per_organisation(df_data)
    assert spent["NASA"] == pytest.approx(400.0)
    assert spent.index[0] == "NASA"
    average = analysis.average_price_per_organisation(df_data)
    assert average["NASA"] == pytest.approx(200.0)
    assert average["CASC"] == pytest.approx(50.0)


def test_organisation_without_price_is_left_out(df_data: pd.DataFrame) -> None:
    """@brief An organisation whose prices are all missing is not listed."""
    df_data.loc[df_data["Organisation"] == "CASC", "Price"] = None
    assert "CASC" not in analysis.money_spent_per_organisation(df_data).index


def test_launches_per_year_fills_the_gap_years(df_data: pd.DataFrame) -> None:
    """@brief Years with no launch show as zero."""
    result = analysis.launches_per_year(df_data)
    assert result[1960] == 3
    assert result[1962] == 0
    assert result.index.min() == 1960
    assert result.index.max() == 1995


def test_month_counts_and_most_popular_month(df_data: pd.DataFrame) -> None:
    """@brief December has three launches and is the most popular."""
    months = analysis.launches_per_month(df_data)
    assert list(months.index) == list(range(1, 13))
    assert months[12] == 3
    assert analysis.most_popular_month(df_data) == 12


def test_average_price_per_year(df_data: pd.DataFrame) -> None:
    """@brief Years with no known price are left out."""
    result = analysis.average_price_per_year(df_data)
    assert result[1960] == pytest.approx(200.0)
    assert 1961 not in result.index


def test_top_organisation_per_year_breaks_ties_alphabetically(
    df_data: pd.DataFrame,
) -> None:
    """@brief 1960 goes to NASA; 1963 is a tie between CASC and RVSN USSR."""
    result = analysis.top_organisation_per_year(df_data).set_index("Year")
    assert result.loc[1960, "Organisation"] == "NASA"
    assert result.loc[1960, "Launches"] == 2
    assert result.loc[1963, "Organisation"] == "CASC"


def test_country_code_and_country_counts(df_data: pd.DataFrame) -> None:
    """@brief Codes follow ISO 3166 and the counts add up."""
    coded = analysis.add_country_code(df_data)
    assert set(coded["Country_Code"]) == {"USA", "KAZ", "RUS", "CHN"}
    per_country = analysis.launches_per_country(df_data)
    assert per_country.iloc[0]["Country_Code"] == "USA"
    assert per_country["Launches"].sum() == 8


def test_failures_per_country_counts_every_non_success(df_data: pd.DataFrame) -> None:
    """@brief Failure and partial failure both count."""
    result = analysis.failures_per_country(df_data).set_index("Country_Code")
    assert result["Launches"].to_dict() == {"USA": 1, "RUS": 1, "CHN": 1}


def test_unknown_country_name_is_rejected(df_data: pd.DataFrame) -> None:
    """@brief A name that is not in ISO 3166 raises KeyError."""
    df_data.loc[0, "Country"] = "Atlantis"
    with pytest.raises(KeyError):
        analysis.add_country_code(df_data)


def test_sunburst_data_keeps_all_launches(df_data: pd.DataFrame) -> None:
    """@brief The three levels add up to the total launches."""
    result = analysis.sunburst_data(df_data)
    assert list(result.columns) == [
        "Country",
        "Organisation",
        "Mission_Status",
        "Launches",
    ]
    assert result["Launches"].sum() == 8


def test_cold_war_counts_kazakhstan_for_the_ussr(df_data: pd.DataFrame) -> None:
    """@brief 1960: USA 2 launches, USSR 1; 1995 is after the Cold War."""
    result = analysis.cold_war_launches(df_data).set_index(["Year", "Side"])
    assert result.loc[(1960, "USA"), "Launches"] == 2
    assert result.loc[(1960, "USSR"), "Launches"] == 1
    assert result.loc[(1963, "USSR"), "Launches"] == 1
    assert 1995 not in result.index.get_level_values("Year")
    assert "China" not in result.index.get_level_values("Side")


def test_cold_war_failures_only(df_data: pd.DataFrame) -> None:
    """@brief Only the failed launches are counted."""
    result = analysis.cold_war_launches(df_data, failures_only=True)
    assert result["Launches"].sum() == 2


def test_failure_rate_per_year_and_decade(df_data: pd.DataFrame) -> None:
    """@brief 1960 had one failure in three launches."""
    per_year = analysis.failure_rate_per_year(df_data)
    assert per_year[1960] == pytest.approx(1 / 3)
    assert per_year[1995] == 0
    per_decade = analysis.failure_rate_per_decade(df_data).set_index("Decade")
    assert per_decade.loc[1960, "Launches"] == 7
    assert per_decade.loc[1960, "Failure_Rate"] == pytest.approx(3 / 7)
    assert per_decade.loc[1990, "Failure_Rate"] == 0
