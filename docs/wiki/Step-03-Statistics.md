**English** · [Dansk](Step-03-Statistics-da) · [Bahasa Malaysia](Step-03-Statistics-ms)

# Step 3: Descriptive statistics

![Step 3: Descriptive statistics](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/raw/branch/main/docs/images/03-descriptive-statistics.png)

## What the step does

`describe` summarises every column of the clean data in one table.

## What was gained

- Only 963 launches have a price, so every price result in later steps rests on about a fifth of the data.
- The data runs from 1957 to 2020 across 56 organisations and 15 countries.
- A summary table is a quick check that the cleaning did what it should.

## Code in `src/space_race/`

`DataFrame.describe`
