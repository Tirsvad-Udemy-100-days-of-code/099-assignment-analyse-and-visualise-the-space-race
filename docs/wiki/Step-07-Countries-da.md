[English](Step-07-Countries) · **Dansk** · [Bahasa Malaysia](Step-07-Countries-ms)

# Trin 7: Landeanalyse med choropleth-kort

![Trin 7: Landeanalyse med choropleth-kort](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/raw/branch/main/docs/images/07-country-analysis-with-choropleth-maps.png)

## Hvad trinnet gør

To verdenskort farver hvert land efter dets opsendelser og dets mislykkede opsendelser.

## Hvad vi fik ud af det

- Rusland (1.398) og USA (1.387) fører, med Kasakhstan (701) på tredjepladsen på grund af Bajkonur.
- Et kort kræver standard ISO 3166-koder, så landenavnene skulle kortlægges omhyggeligt; et ukendt navn giver en fejl i stedet for en tom plet på kortet.
- Alle statusser undtagen Success tæller som en fejl; USA har flest fejl (166).

## Kode i `src/space_race/`

`launches_per_country`, `failures_per_country`, `add_country_code`, `choropleth`
