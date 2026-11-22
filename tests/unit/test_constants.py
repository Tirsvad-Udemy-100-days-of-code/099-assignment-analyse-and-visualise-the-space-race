"""@file test_constants.py
@brief Tests for the project constants.
"""

from pathlib import Path

from space_race import constants


def test_start_year_is_first_launch_year() -> None:
    """@brief The Space Race data starts in 1957."""
    assert constants.SPACE_RACE_START_YEAR == 1957


def test_raw_data_path_is_relative() -> None:
    """@brief Paths are relative to the repository root, never absolute."""
    assert not constants.RAW_DATA_DIRECTORY.is_absolute()
    assert not constants.IMAGE_DIRECTORY.is_absolute()


def test_missions_file_is_csv() -> None:
    """@brief The missions data set is a CSV file."""
    assert Path(constants.MISSIONS_FILE_NAME).suffix == ".csv"
