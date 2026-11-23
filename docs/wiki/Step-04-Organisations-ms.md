[English](Step-04-Organisations) · [Dansk](Step-04-Organisations-da) · **Bahasa Malaysia**

# Langkah 4: Pelancaran setiap organisasi dan status roket

![Langkah 4: Pelancaran setiap organisasi dan status roket](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/raw/branch/main/docs/images/04-launches-per-organisation-and-rocket-status.png)

## Apa yang dilakukan langkah ini

Carta bar menyusun organisasi mengikut pelancaran, dan dua carta donat menunjukkan roket aktif berbanding bersara dan bagaimana misi berakhir.

## Apa yang diperoleh

- RVSN USSR melancarkan 1,777 kali, jauh mendahului Arianespace (279) dan General Dynamics (251).
- 3,534 pelancaran menggunakan roket yang kini bersara; 789 menggunakan yang aktif.
- 3,878 misi berjaya. Mengira nilai dengan `value_counts` ialah alat pertama untuk setiap lajur kategori.

## Kod dalam `src/space_race/`

`launches_per_organisation`, `rocket_status_counts`, `mission_status_counts`, `bar_chart`, `pie_chart`
