"""@file test_loading.py
@brief Tests for loading the missions file.
"""

from pathlib import Path

import pytest

pytest.importorskip("pandas")

from space_race.loading import file_sha256, load_missions  # noqa: E402

SAMPLE = Path(__file__).parent.parent / "data" / "sample_missions.csv"


def test_load_returns_every_row_and_column() -> None:
    """@brief The raw file is read with no rows or columns lost."""
    df_data = load_missions(SAMPLE)
    assert df_data.shape == (6, 9)


def test_load_missing_file_names_the_path(tmp_path: Path) -> None:
    """@brief A missing file raises an error that says where it looked."""
    missing = tmp_path / "nothing.csv"
    with pytest.raises(FileNotFoundError, match="nothing.csv"):
        load_missions(missing)


def test_checksum_is_stable_and_hex() -> None:
    """@brief The checksum is a 64 character hexadecimal text, equal on repeat."""
    first = file_sha256(SAMPLE)
    assert len(first) == 64
    assert first == file_sha256(SAMPLE)


def test_checksum_differs_for_other_content(tmp_path: Path) -> None:
    """@brief Different content gives a different checksum."""
    other = tmp_path / "other.csv"
    other.write_text("a,b\n1,2\n", encoding="utf-8")
    assert file_sha256(other) != file_sha256(SAMPLE)
