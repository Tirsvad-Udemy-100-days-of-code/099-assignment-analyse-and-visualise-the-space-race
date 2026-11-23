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

## SHA-256 checksum of the supplied missions file (4,324 data rows).
MISSIONS_FILE_SHA256: str = (
    "ae8097c187d910380a92c5258582981246856766e31541687f04909e78888084"
)

## Raw column: the organisation that ran the launch.
COL_ORGANISATION: str = "Organisation"
## Raw column: launch site, ending in the country or region.
COL_LOCATION: str = "Location"
## Raw column: launch date as text.
COL_DATE: str = "Date"
## Raw column: rocket and payload.
COL_DETAIL: str = "Detail"
## Raw column: StatusActive or StatusRetired.
COL_ROCKET_STATUS: str = "Rocket_Status"
## Raw column: price in USD millions, as text.
COL_PRICE: str = "Price"
## Raw column: Success, Failure, Partial Failure or Prelaunch Failure.
COL_MISSION_STATUS: str = "Mission_Status"

## Columns of the raw file that only hold a row index and are dropped.
JUNK_COLUMNS: tuple[str, ...] = ("Unnamed: 0.1", "Unnamed: 0")

## Added column: the launching country.
COL_COUNTRY: str = "Country"
## Added column: launch date and time as a timestamp.
COL_LAUNCH_TIME: str = "Launch_Time"
## Added column: launch year.
COL_YEAR: str = "Year"
## Added column: launch month, 1 to 12.
COL_MONTH: str = "Month"

## Format of the Date column when it carries a time.
DATE_FORMAT_WITH_TIME: str = "%a %b %d, %Y %H:%M UTC"
## Format of the Date column when it has no time.
DATE_FORMAT_DATE_ONLY: str = "%a %b %d, %Y"

## Last part of a Location that is not a country, mapped to the launching
## country. Sea Launch (Pacific Ocean) and the air launches from Gran Canaria
## and the Pacific Missile Range Facility were run by United States companies.
LOCATION_COUNTRY_FIXES: dict[str, str] = {
    "Russia": "Russian Federation",
    "USA": "United States of America",
    "New Mexico": "United States of America",
    "Pacific Ocean": "United States of America",
    "Gran Canaria": "United States of America",
    "Pacific Missile Range Facility": "United States of America",
    "Barents Sea": "Russian Federation",
    "Yellow Sea": "China",
    "Shahrud Missile Test Site": "Iran, Islamic Republic of",
    "Iran": "Iran, Islamic Republic of",
    "North Korea": "Korea, Democratic People's Republic of",
    "South Korea": "Korea, Republic of",
}

## Added column: the ISO 3166 alpha-3 code of the launching country.
COL_COUNTRY_CODE: str = "Country_Code"

## Mission status of a launch that reached its goal; every other status counts
## as a failure (Failure, Partial Failure, Prelaunch Failure).
STATUS_SUCCESS: str = "Success"

## Last year of the Cold War comparison (the Soviet Union ended in 1991).
COLD_WAR_END_YEAR: int = 1991
## Label of the United States in the Cold War comparison.
SIDE_USA: str = "USA"
## Label of the Soviet Union in the Cold War comparison.
SIDE_USSR: str = "USSR"
## Countries whose launch sites were Soviet before 1992 (Baikonur is in
## Kazakhstan), mapped to the side they belong to.
COLD_WAR_SIDES: dict[str, str] = {
    "United States of America": SIDE_USA,
    "Russian Federation": SIDE_USSR,
    "Kazakhstan": SIDE_USSR,
}
