**English** · [Dansk](Step-08-Sunburst-da) · [Bahasa Malaysia](Step-08-Sunburst-ms)

# Step 8: Sunburst chart

![Step 8: Sunburst chart](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/raw/branch/main/docs/images/08-sunburst-chart.png)

## What the step does

A ring chart shows country, then organisation, then mission status.

## What was gained

- Three levels of a hierarchy fit in one picture, so the share of failures inside one organisation inside one country is visible at once.
- The data is grouped once into counts per country, organisation and status; the chart only draws it.
- Small slices are unreadable in a static picture, which is a reason to keep the chart interactive when exploring.

## Code in `src/space_race/`

`sunburst_data`, `sunburst_chart`
