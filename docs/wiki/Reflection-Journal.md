**English** · [Dansk](Reflection-Journal-da) · [Bahasa Malaysia](Reflection-Journal-ms)

# Reflection journal

## Approach

I built the project in four steps, each reviewed before the next: a plan, the repository baseline, the data preparation and the analysis, then the documentation. The logic lives in small tested functions and the notebook only calls them, so every answer can be checked without running a chart.

## What was easy

Counting and grouping with pandas (`value_counts`, `groupby`) answered most questions in one or two lines, and plotly turned the results into charts with little code.

## What was hard

The data. Only a fifth of the launches have a price, one price is a huge outlier, launch sites at sea have no country, and the USSR launched from Kazakhstan. Each of these needed a decision that I wrote down in `constants.py` or in the step's wiki page.

## Biggest learning

Look at the data before changing it, and never replace missing values with a guess unless you can defend it. A rate or an average without its count beside it can mislead, as the 1950s failure rate shows.

## What I would do differently

I would check the licence of the data file first so the data could be part of the repository, and I would add a small table of the price outliers so the average chart is easier to read.
