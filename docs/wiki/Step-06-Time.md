**English** · [Dansk](Step-06-Time-da) · [Bahasa Malaysia](Step-06-Time-ms)

# Step 6: Launches per year, month and over time

![Step 6: Launches per year, month and over time](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/raw/branch/main/docs/images/06-launches-per-year-month-and-over-time.png)

## What the step does

A line chart counts launches per year, a bar chart counts them per calendar month, and a second line chart follows the average price over the years.

## What was gained

- The busiest year was 1971 with 119 launches; activity then fell and rose again in the 2010s.
- December is the most popular month (450 launches) and January the least (268).
- Reindexing to every year and every month makes gaps show up as zero instead of silently disappearing.

## Code in `src/space_race/`

`launches_per_year`, `launches_per_month`, `most_popular_month`, `average_price_per_year`, `line_chart`
