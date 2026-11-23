"""@file conftest.py
@brief Shared test data: a small, hand-made clean data set.
"""

import pytest

pytest.importorskip("pandas")

import pandas as pd  # noqa: E402

ROWS = [
    # organisation, country, year, month, price, rocket status, mission status
    ("NASA", "United States of America", 1960, 12, 100.0, "StatusRetired", "Success"),
    ("NASA", "United States of America", 1960, 12, 300.0, "StatusRetired", "Failure"),
    ("NASA", "United States of America", 1961, 3, None, "StatusRetired", "Success"),
    ("RVSN USSR", "Kazakhstan", 1960, 12, None, "StatusRetired", "Success"),
    ("RVSN USSR", "Russian Federation", 1961, 4, None, "StatusRetired", "Failure"),
    ("RVSN USSR", "Kazakhstan", 1963, 4, 50.0, "StatusRetired", "Success"),
    ("CASC", "China", 1963, 9, 30.0, "StatusActive", "Partial Failure"),
    ("CASC", "China", 1995, 9, 70.0, "StatusActive", "Success"),
]
COLUMNS = [
    "Organisation",
    "Country",
    "Year",
    "Month",
    "Price",
    "Rocket_Status",
    "Mission_Status",
]


@pytest.fixture
def df_data() -> pd.DataFrame:
    """@brief Eight launches by three organisations."""
    return pd.DataFrame(ROWS, columns=COLUMNS)
