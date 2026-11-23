**English** · [Dansk](Step-04-Organisations-da) · [Bahasa Malaysia](Step-04-Organisations-ms)

# Step 4: Launches per organisation and rocket status

![Step 4: Launches per organisation and rocket status](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/raw/branch/main/docs/images/04-launches-per-organisation-and-rocket-status.png)

## What the step does

A bar chart ranks the organisations by launches, and two donut charts show active against retired rockets and how the missions ended.

## What was gained

- RVSN USSR launched 1,777 times, far ahead of Arianespace (279) and General Dynamics (251).
- 3,534 launches used rockets that are now retired; 789 used active ones.
- 3,878 missions succeeded. Counting values with `value_counts` is the first tool for every categorical column.

## Code in `src/space_race/`

`launches_per_organisation`, `rocket_status_counts`, `mission_status_counts`, `bar_chart`, `pie_chart`
