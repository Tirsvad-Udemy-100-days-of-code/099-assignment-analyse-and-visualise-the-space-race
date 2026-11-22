"""@file exploration.py
@brief Preliminary data exploration: shape, columns, missing values, duplicates.
"""

from dataclasses import dataclass

import pandas as pd

from space_race.constants import JUNK_COLUMNS


@dataclass(frozen=True)
class DataExploration:
    """!
    @brief Facts about a data frame found by the preliminary exploration.
    """

    ## Number of rows.
    row_count: int
    ## Number of columns.
    column_count: int
    ## Column names, in file order.
    column_names: tuple[str, ...]
    ## Number of missing values per column, only for columns that have any.
    missing_by_column: dict[str, int]
    ## Number of rows that repeat an earlier row, not counting the index columns.
    duplicate_count: int


def explore(df_data: pd.DataFrame) -> DataExploration:
    """!
    @brief Answer the questions of the preliminary exploration step.

    @param df_data The data frame to describe.
    The row-index columns differ in every row, so they are left out when
    duplicates are counted.

    @return Shape, column names, missing values and duplicate rows.
    """
    missing = df_data.isna().sum()
    return DataExploration(
        row_count=int(df_data.shape[0]),
        column_count=int(df_data.shape[1]),
        column_names=tuple(str(name) for name in df_data.columns),
        missing_by_column={
            str(name): int(count) for name, count in missing.items() if count > 0
        },
        duplicate_count=int(
            df_data.drop(columns=list(JUNK_COLUMNS), errors="ignore").duplicated().sum()
        ),
    )
