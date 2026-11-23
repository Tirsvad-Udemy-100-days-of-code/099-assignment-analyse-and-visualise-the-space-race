[English](Step-08-Sunburst) · **Dansk** · [Bahasa Malaysia](Step-08-Sunburst-ms)

# Trin 8: Sunburst-diagram

![Trin 8: Sunburst-diagram](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/raw/branch/main/docs/images/08-sunburst-chart.png)

## Hvad trinnet gør

Et ringdiagram viser land, derefter organisation, derefter missionsstatus.

## Hvad vi fik ud af det

- Tre niveauer af et hierarki er i ét billede, så andelen af fejl i én organisation i ét land ses med det samme.
- Data grupperes én gang til antal pr. land, organisation og status; diagrammet tegner det kun.
- Små udsnit er ulæselige i et statisk billede, hvilket er en grund til at beholde diagrammet interaktivt under udforskning.

## Kode i `src/space_race/`

`sunburst_data`, `sunburst_chart`
