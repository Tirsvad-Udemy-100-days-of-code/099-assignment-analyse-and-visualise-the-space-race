[English](Step-04-Organisations) · **Dansk** · [Bahasa Malaysia](Step-04-Organisations-ms)

# Trin 4: Opsendelser pr. organisation og raketstatus

![Trin 4: Opsendelser pr. organisation og raketstatus](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/raw/branch/main/docs/images/04-launches-per-organisation-and-rocket-status.png)

## Hvad trinnet gør

Et søjlediagram rangerer organisationerne efter opsendelser, og to ringdiagrammer viser aktive mod udgåede raketter og hvordan missionerne endte.

## Hvad vi fik ud af det

- RVSN USSR opsendte 1.777 gange, langt foran Arianespace (279) og General Dynamics (251).
- 3.534 opsendelser brugte raketter, der nu er udgået; 789 brugte aktive.
- 3.878 missioner lykkedes. At tælle værdier med `value_counts` er det første værktøj til hver kategorikolonne.

## Kode i `src/space_race/`

`launches_per_organisation`, `rocket_status_counts`, `mission_status_counts`, `bar_chart`, `pie_chart`
