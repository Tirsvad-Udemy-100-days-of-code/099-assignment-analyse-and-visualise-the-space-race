[English](Step-09-Over-Time) · **Dansk** · [Bahasa Malaysia](Step-09-Over-Time-ms)

# Trin 9: Organisationer og lande over tid

![Trin 9: Organisationer og lande over tid](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/raw/branch/main/docs/images/09-organisations-and-countries-over-time.png)

## Hvad trinnet gør

Et stablet søjlediagram navngiver årets travleste organisation, og grupperede søjlediagrammer sammenligner USA og USSR under Rumkapløbet (1957 til 1991).

## Hvad vi fik ud af det

- USSR opsendte 1.770 gange mod 662 for USA, men USA havde flere fejl i de første år.
- Bajkonur ligger i Kasakhstan, så sammenligningen tæller Kasakhstan med til USSR. Den vurdering står i `constants.py`.
- Uafgjort om den travleste organisation afgøres alfabetisk, så resultatet er det samme ved hver kørsel.

## Kode i `src/space_race/`

`top_organisation_per_year`, `cold_war_launches`, `grouped_bar_chart`
