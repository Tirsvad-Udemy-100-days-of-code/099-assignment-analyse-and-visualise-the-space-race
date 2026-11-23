[English](Step-06-Time) · **Dansk** · [Bahasa Malaysia](Step-06-Time-ms)

# Trin 6: Opsendelser pr. år, måned og over tid

![Trin 6: Opsendelser pr. år, måned og over tid](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/raw/branch/main/docs/images/06-launches-per-year-month-and-over-time.png)

## Hvad trinnet gør

Et kurvediagram tæller opsendelser pr. år, et søjlediagram tæller dem pr. kalendermåned, og et andet kurvediagram følger gennemsnitsprisen over årene.

## Hvad vi fik ud af det

- Det travleste år var 1971 med 119 opsendelser; aktiviteten faldt derefter og steg igen i 2010'erne.
- December er den mest populære måned (450 opsendelser) og januar den mindst populære (268).
- At genindeksere til alle år og alle måneder får huller til at vise som nul i stedet for at forsvinde lydløst.

## Kode i `src/space_race/`

`launches_per_year`, `launches_per_month`, `most_popular_month`, `average_price_per_year`, `line_chart`
