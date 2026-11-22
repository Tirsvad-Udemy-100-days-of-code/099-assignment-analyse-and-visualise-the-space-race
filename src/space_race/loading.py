"""@file loading.py
@brief Load the raw space missions data set.
"""

import hashlib
from pathlib import Path

import pandas as pd

from space_race.constants import MISSIONS_FILE_NAME, RAW_DATA_DIRECTORY

## Number of bytes read at a time when a checksum is computed.
_CHUNK_BYTES = 1 << 20


def default_missions_path() -> Path:
    """!
    @brief Give the default location of the raw missions file.

    @return Path of the file, relative to the repository root.
    """
    return RAW_DATA_DIRECTORY / MISSIONS_FILE_NAME


def file_sha256(path: Path) -> str:
    """!
    @brief Compute the SHA-256 checksum of a file.

    @param path File to read.
    @return The checksum as lowercase hexadecimal text.
    """
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(_CHUNK_BYTES):
            digest.update(chunk)
    return digest.hexdigest()


def load_missions(path: Path | None = None) -> pd.DataFrame:
    """!
    @brief Read the missions CSV file into a data frame.

    @param path CSV file; the default location when omitted.
    @return The raw data, one row per launch, with no cleaning applied.
    @throws FileNotFoundError When the file does not exist.
    """
    source = path if path is not None else default_missions_path()
    if not source.is_file():
        message = f"Missions file not found: {source}. See the README, section Data."
        raise FileNotFoundError(message)
    return pd.read_csv(source)
