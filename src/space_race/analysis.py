"""@file analysis.py
@brief Analysis steps: counts, prices, time series, countries and safety.

Every function takes the clean data from `clean_missions` and returns a pandas
object; drawing is left to `charts.py`.
"""

import iso3166
import pandas as pd

from space_race.constants import (
    COL_COUNTRY,
    COL_COUNTRY_CODE,
    COL_MISSION_STATUS,
    COL_MONTH,
    COL_ORGANISATION,
    COL_PRICE,
    COL_ROCKET_STATUS,
    COL_YEAR,
    COLD_WAR_END_YEAR,
    COLD_WAR_SIDES,
    STATUS_SUCCESS,
)

## Name of the count column in the tables below.
LAUNCHES: str = "Launches"
## Name of the side column of the Cold War table.
SIDE: str = "Side"
## Name of the decade column of the safety table.
DECADE: str = "Decade"
## Name of the failure rate column of the safety tables.
FAILURE_RATE: str = "Failure_Rate"
## Years in one decade.
YEARS_PER_DECADE: int = 10


def launches_per_organisation(df_data: pd.DataFrame) -> pd.Series:
    """!
    @brief Count the launches of each organisation.

    @param df_data Clean data.
    @return Launch counts, the busiest organisation first.
    """
    return df_data[COL_ORGANISATION].value_counts().rename(LAUNCHES)


def rocket_status_counts(df_data: pd.DataFrame) -> pd.Series:
    """!
    @brief Count the launches by rocket status (active or retired).

    @param df_data Clean data.
    @return Counts per rocket status.
    """
    return df_data[COL_ROCKET_STATUS].value_counts().rename(LAUNCHES)


def mission_status_counts(df_data: pd.DataFrame) -> pd.Series:
    """!
    @brief Count the launches by mission status.

    @param df_data Clean data.
    @return Counts per mission status (Success, Failure and so on).
    """
    return df_data[COL_MISSION_STATUS].value_counts().rename(LAUNCHES)


def known_prices(df_data: pd.DataFrame) -> pd.Series:
    """!
    @brief Pick the launch prices that are known.

    @param df_data Clean data.
    @return Prices in USD millions, without the missing ones.
    """
    return df_data[COL_PRICE].dropna()


def money_spent_per_organisation(df_data: pd.DataFrame) -> pd.Series:
    """!
    @brief Add up the known launch prices of each organisation.

    @param df_data Clean data.
    @return Total price in USD millions, the largest first; organisations
        with no known price are left out.
    """
    total = df_data.groupby(COL_ORGANISATION)[COL_PRICE].sum(min_count=1)
    return total.dropna().sort_values(ascending=False).rename(COL_PRICE)


def average_price_per_organisation(df_data: pd.DataFrame) -> pd.Series:
    """!
    @brief Average the known launch prices of each organisation.

    @param df_data Clean data.
    @return Average price per launch in USD millions, the largest first.
    """
    mean = df_data.groupby(COL_ORGANISATION)[COL_PRICE].mean()
    return mean.dropna().sort_values(ascending=False).rename(COL_PRICE)


def launches_per_year(df_data: pd.DataFrame) -> pd.Series:
    """!
    @brief Count the launches of each year.

    @param df_data Clean data.
    @return Launch counts indexed by year, with zero for a year without launch.
    """
    counts = df_data[COL_YEAR].value_counts().sort_index()
    years = range(int(counts.index.min()), int(counts.index.max()) + 1)
    return counts.reindex(years, fill_value=0).rename(LAUNCHES)


def launches_per_month(df_data: pd.DataFrame) -> pd.Series:
    """!
    @brief Count the launches of each calendar month over all years.

    @param df_data Clean data.
    @return Launch counts indexed by month number 1 to 12.
    """
    counts = df_data[COL_MONTH].value_counts()
    return counts.reindex(range(1, 13), fill_value=0).rename(LAUNCHES)


def most_popular_month(df_data: pd.DataFrame) -> int:
    """!
    @brief Find the calendar month with the most launches.

    @param df_data Clean data.
    @return The month number, 1 to 12.
    """
    busiest = launches_per_month(df_data).idxmax()
    return int(str(busiest))


def average_price_per_year(df_data: pd.DataFrame) -> pd.Series:
    """!
    @brief Average the known launch prices of each year.

    @param df_data Clean data.
    @return Average price in USD millions indexed by year; years with no
        known price are left out.
    """
    return df_data.groupby(COL_YEAR)[COL_PRICE].mean().dropna().rename(COL_PRICE)


def top_organisation_per_year(df_data: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Find the organisation with the most launches in each year.

    A tie goes to the organisation that comes first in the alphabet.

    @param df_data Clean data.
    @return One row per year: Year, Organisation and Launches.
    """
    counts = (
        df_data.groupby([COL_YEAR, COL_ORGANISATION]).size().rename(LAUNCHES)
    ).reset_index()
    ordered = counts.sort_values(
        [COL_YEAR, LAUNCHES, COL_ORGANISATION], ascending=[True, False, True]
    )
    return ordered.drop_duplicates(COL_YEAR).reset_index(drop=True)


def add_country_code(df_data: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Add the ISO 3166 alpha-3 code that a map needs.

    @param df_data Clean data with a Country column of ISO 3166 names.
    @return A copy with a Country_Code column.
    @throws KeyError When a country name is not an ISO 3166 name.
    """
    result = df_data.copy()
    codes = {
        name: iso3166.countries.get(name).alpha3
        for name in result[COL_COUNTRY].dropna().unique()
    }
    result[COL_COUNTRY_CODE] = result[COL_COUNTRY].map(codes)
    return result


def launches_per_country(df_data: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Count the launches of each country.

    @param df_data Clean data.
    @return Country, Country_Code and Launches, the busiest country first.
    """
    coded = add_country_code(df_data)
    counts = coded.groupby([COL_COUNTRY, COL_COUNTRY_CODE]).size().rename(LAUNCHES)
    return counts.reset_index().sort_values(
        LAUNCHES, ascending=False, ignore_index=True
    )


def failures_per_country(df_data: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Count the failed launches of each country.

    Every status other than Success counts as a failure.

    @param df_data Clean data.
    @return Country, Country_Code and Launches (the failures), the most first;
        countries without a failure are left out.
    """
    failed = df_data[df_data[COL_MISSION_STATUS] != STATUS_SUCCESS]
    return launches_per_country(failed)


def sunburst_data(df_data: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Count the launches by country, organisation and mission status.

    @param df_data Clean data.
    @return Country, Organisation, Mission_Status and Launches.
    """
    keys = [COL_COUNTRY, COL_ORGANISATION, COL_MISSION_STATUS]
    return df_data.groupby(keys).size().rename(LAUNCHES).reset_index()


def cold_war_launches(
    df_data: pd.DataFrame, *, failures_only: bool = False
) -> pd.DataFrame:
    """!
    @brief Count the launches of the USA and the USSR in each Cold War year.

    Kazakhstan counts for the USSR because Baikonur was Soviet before 1992.

    @param df_data Clean data.
    @param failures_only Count only the launches that did not succeed.
    @return Year, Side and Launches for the years up to 1991.
    """
    wanted = df_data[df_data[COL_YEAR] <= COLD_WAR_END_YEAR].copy()
    if failures_only:
        wanted = wanted[wanted[COL_MISSION_STATUS] != STATUS_SUCCESS]
    wanted[SIDE] = wanted[COL_COUNTRY].map(COLD_WAR_SIDES)
    counts = wanted.groupby([COL_YEAR, SIDE]).size().rename(LAUNCHES)
    return counts.reset_index()


def failure_rate_per_year(df_data: pd.DataFrame) -> pd.Series:
    """!
    @brief Compute the share of launches that did not succeed in each year.

    @param df_data Clean data.
    @return Failure rate from 0 to 1 indexed by year.
    """
    failed = df_data[COL_MISSION_STATUS] != STATUS_SUCCESS
    return failed.groupby(df_data[COL_YEAR]).mean().rename(FAILURE_RATE)


def failure_rate_per_decade(df_data: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Compute the failure rate of each decade.

    @param df_data Clean data.
    @return Decade (its first year), Launches and Failure_Rate.
    """
    decade = df_data[COL_YEAR] // YEARS_PER_DECADE * YEARS_PER_DECADE
    failed = df_data[COL_MISSION_STATUS] != STATUS_SUCCESS
    table = pd.DataFrame({DECADE: decade, FAILURE_RATE: failed})
    grouped = table.groupby(DECADE)[FAILURE_RATE]
    result = pd.DataFrame({LAUNCHES: grouped.size(), FAILURE_RATE: grouped.mean()})
    return result.reset_index()
