**English** · [Dansk](Step-09-Over-Time-da) · [Bahasa Malaysia](Step-09-Over-Time-ms)

# Step 9: Organisations and countries over time

![Step 9: Organisations and countries over time](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/raw/branch/main/docs/images/09-organisations-and-countries-over-time.png)

## What the step does

A stacked bar chart names the busiest organisation of each year, and grouped bar charts compare the USA and the USSR during the Space Race (1957 to 1991).

## What was gained

- The USSR launched 1,770 times against 662 for the USA, but the USA had more failures in the early years.
- Baikonur lies in Kazakhstan, so the comparison counts Kazakhstan with the USSR. That judgement is written down in `constants.py`.
- Ties for busiest organisation are broken alphabetically, so the result is the same on every run.

## Code in `src/space_race/`

`top_organisation_per_year`, `cold_war_launches`, `grouped_bar_chart`
