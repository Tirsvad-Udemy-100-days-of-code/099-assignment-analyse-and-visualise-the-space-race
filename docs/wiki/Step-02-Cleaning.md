**English** · [Dansk](Step-02-Cleaning-da) · [Bahasa Malaysia](Step-02-Cleaning-ms)

# Step 2: Data cleaning

![Step 2: Data cleaning](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/raw/branch/main/docs/images/02-data-cleaning.png)

## What the step does

The junk columns and the duplicate are removed, the price becomes a number, the dates are parsed and the launching country is taken from the launch site.

## What was gained

- A missing price stays missing instead of being replaced by a guess, because a guess would change every price statistic.
- Dates come in two formats (with and without a time), so parsing tries both and fails loudly on anything else.
- Launch sites at sea or in the air need a rule to become a country. The rule is a visible table in `constants.py`, not hidden code.

## Code in `src/space_race/`

`clean_missions`, `drop_duplicates`, `convert_price`, `parse_dates`, `add_country`
