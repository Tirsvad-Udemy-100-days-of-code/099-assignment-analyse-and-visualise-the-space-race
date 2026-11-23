[English](Step-05-Prices) · **Dansk** · [Bahasa Malaysia](Step-05-Prices-ms)

# Trin 5: Opsendelsespriser og brugte penge

![Trin 5: Opsendelsespriser og brugte penge](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/raw/branch/main/docs/images/05-launch-prices-and-money-spent.png)

## Hvad trinnet gør

Et histogram viser spredningen af opsendelsespriser, og to søjlediagrammer viser de brugte penge og gennemsnitsprisen pr. opsendelse for hver organisation.

## Hvad vi fik ud af det

- Medianprisen er 62 mio. USD, men én organisation (RVSN USSR) har et gennemsnit på 5.000 mio., en outlier der dominerer gennemsnitsdiagrammet.
- NASA brugte flest penge i alt (cirka 76.280 mio. USD), fordi den har mange opsendelser med pris.
- Sum og gennemsnit besvarer forskellige spørgsmål; at vise begge undgår et misvisende billede.

## Kode i `src/space_race/`

`known_prices`, `money_spent_per_organisation`, `average_price_per_organisation`, `histogram`
