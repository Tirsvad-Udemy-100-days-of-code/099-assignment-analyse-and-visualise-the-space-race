[English](Step-02-Cleaning) · **Dansk** · [Bahasa Malaysia](Step-02-Cleaning-ms)

# Trin 2: Datarensning

![Trin 2: Datarensning](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/raw/branch/main/docs/images/02-data-cleaning.png)

## Hvad trinnet gør

Fyldkolonnerne og dubletten fjernes, prisen bliver til et tal, datoerne fortolkes, og opsendelseslandet udledes af opsendelsesstedet.

## Hvad vi fik ud af det

- En manglende pris forbliver manglende i stedet for at blive erstattet med et gæt, fordi et gæt ville ændre al prisstatistik.
- Datoer findes i to formater (med og uden klokkeslæt), så fortolkningen prøver begge og fejler tydeligt ved alt andet.
- Opsendelsessteder på havet eller i luften har brug for en regel for at blive til et land. Reglen er en synlig tabel i `constants.py`, ikke skjult kode.

## Kode i `src/space_race/`

`clean_missions`, `drop_duplicates`, `convert_price`, `parse_dates`, `add_country`
