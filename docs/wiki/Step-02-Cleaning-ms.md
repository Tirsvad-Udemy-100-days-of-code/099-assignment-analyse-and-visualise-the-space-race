[English](Step-02-Cleaning) · [Dansk](Step-02-Cleaning-da) · **Bahasa Malaysia**

# Langkah 2: Pembersihan data

![Langkah 2: Pembersihan data](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/raw/branch/main/docs/images/02-data-cleaning.png)

## Apa yang dilakukan langkah ini

Lajur sampah dan pendua dibuang, harga menjadi nombor, tarikh diuraikan dan negara pelancar diambil daripada tapak pelancaran.

## Apa yang diperoleh

- Harga yang hilang kekal hilang dan tidak diganti dengan tekaan, kerana tekaan akan mengubah semua statistik harga.
- Tarikh datang dalam dua format (dengan dan tanpa masa), jadi penguraian mencuba kedua-duanya dan gagal dengan jelas pada yang lain.
- Tapak pelancaran di laut atau udara memerlukan peraturan untuk menjadi negara. Peraturan itu ialah jadual yang kelihatan dalam `constants.py`, bukan kod tersembunyi.

## Kod dalam `src/space_race/`

`clean_missions`, `drop_duplicates`, `convert_price`, `parse_dates`, `add_country`
