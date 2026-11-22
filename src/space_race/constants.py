"""@file constants.py
@brief All constants of the Space Race project, in one place.
"""

from pathlib import Path

## Name of the project package.
PACKAGE_NAME: str = "space_race"

## First year of the Space Race data (launch of Sputnik 1).
SPACE_RACE_START_YEAR: int = 1957

## Directory that holds the raw data file, relative to the repository root.
RAW_DATA_DIRECTORY: Path = Path("data") / "raw"

## File name of the missions data set supplied with the assignment.
MISSIONS_FILE_NAME: str = "mission_launches.csv"

## Directory that holds the screenshots of the lecture steps.
IMAGE_DIRECTORY: Path = Path("docs") / "images"
