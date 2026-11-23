[English](Step-07-Countries) · [Dansk](Step-07-Countries-da) · **Bahasa Malaysia**

# Langkah 7: Analisis negara dengan peta choropleth

![Langkah 7: Analisis negara dengan peta choropleth](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/raw/branch/main/docs/images/07-country-analysis-with-choropleth-maps.png)

## Apa yang dilakukan langkah ini

Dua peta dunia mewarnakan setiap negara mengikut pelancarannya dan pelancarannya yang gagal.

## Apa yang diperoleh

- Rusia (1,398) dan AS (1,387) mendahului, dengan Kazakhstan (701) ketiga kerana tapak Baikonur.
- Peta memerlukan kod ISO 3166 piawai, jadi nama negara perlu dipetakan dengan teliti; nama yang tidak dikenali menimbulkan ralat dan bukan tompok kosong pada peta.
- Setiap status kecuali Success dikira sebagai kegagalan; AS mempunyai kegagalan terbanyak (166).

## Kod dalam `src/space_race/`

`launches_per_country`, `failures_per_country`, `add_country_code`, `choropleth`
