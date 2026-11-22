"""@file cleaning.py
@brief Data cleaning step: junk columns, duplicates, price, date and country.
"""

import pandas as pd

from space_race.constants import (
    COL_COUNTRY,
    COL_DATE,
    COL_LAUNCH_TIME,
    COL_LOCATION,
    COL_MONTH,
    COL_PRICE,
    COL_YEAR,
    DATE_FORMAT_DATE_ONLY,
    DATE_FORMAT_WITH_TIME,
    JUNK_COLUMNS,
    LOCATION_COUNTRY_FIXES,
)


def drop_junk_columns(df_data: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Remove the columns that only hold a row index.

    @param df_data Raw data.
    @return A copy without the junk columns; absent ones are ignored.
    """
    return df_data.drop(columns=list(JUNK_COLUMNS), errors="ignore")


def drop_duplicates(df_data: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Remove rows that repeat an earlier row.

    @param df_data Data without the index columns.
    @return A copy with the first occurrence of each row kept.
    """
    return df_data.drop_duplicates().reset_index(drop=True)


def convert_price(df_data: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Turn the price text into numbers, in USD millions.

    Thousands separators are removed. A missing price stays missing (NaN):
    most launches have no published price, so it is not replaced by a guess.

    @param df_data Data with a Price column of text.
    @return A copy whose Price column is of type float.
    """
    result = df_data.copy()
    text = result[COL_PRICE].astype("string").str.replace(",", "", regex=False)
    result[COL_PRICE] = pd.to_numeric(text, errors="coerce").astype("float64")
    return result


def parse_dates(df_data: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Parse the Date text and add Launch_Time, Year and Month.

    Some dates have no time of day; they get midnight.

    @param df_data Data with a Date column of text.
    @return A copy with the added columns.
    @throws ValueError When a date has neither supported format.
    """
    result = df_data.copy()
    text = result[COL_DATE].astype("string")
    with_time = pd.to_datetime(text, format=DATE_FORMAT_WITH_TIME, errors="coerce")
    date_only = pd.to_datetime(text, format=DATE_FORMAT_DATE_ONLY, errors="coerce")
    parsed = with_time.fillna(date_only)
    if parsed.isna().any():
        bad = text[parsed.isna()].iloc[0]
        message = f"Unsupported date format: {bad!r}"
        raise ValueError(message)
    result[COL_LAUNCH_TIME] = parsed
    result[COL_YEAR] = parsed.dt.year
    result[COL_MONTH] = parsed.dt.month
    return result


def add_country(df_data: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Add the launching country, taken from the end of Location.

    @param df_data Data with a Location column.
    @return A copy with a Country column using standard ISO 3166 names.
    """
    result = df_data.copy()
    last_part = result[COL_LOCATION].astype("string").str.split(", ").str[-1]
    result[COL_COUNTRY] = last_part.replace(LOCATION_COUNTRY_FIXES)
    return result


def clean_missions(df_data: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Run the whole cleaning step in order.

    @param df_data Raw data from `load_missions`.
    @return Clean data: no junk columns, no duplicates, numeric price,
        parsed dates and a Country column.
    """
    return add_country(
        parse_dates(convert_price(drop_duplicates(drop_junk_columns(df_data))))
    )
