**English** · [Dansk](Step-07-Countries-da) · [Bahasa Malaysia](Step-07-Countries-ms)

# Step 7: Country analysis with choropleth maps

![Step 7: Country analysis with choropleth maps](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/raw/branch/main/docs/images/07-country-analysis-with-choropleth-maps.png)

## What the step does

Two world maps shade each country by its launches and by its failed launches.

## What was gained

- Russia (1,398) and the USA (1,387) lead, with Kazakhstan (701) third because of the Baikonur site.
- A map needs standard ISO 3166 codes, so the country names had to be mapped carefully; an unknown name raises an error instead of an empty spot on the map.
- Every status except Success counts as a failure; the USA has the most failures (166).

## Code in `src/space_race/`

`launches_per_country`, `failures_per_country`, `add_country_code`, `choropleth`
