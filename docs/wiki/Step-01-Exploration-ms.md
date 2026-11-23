[English](Step-01-Exploration) · [Dansk](Step-01-Exploration-da) · **Bahasa Malaysia**

# Langkah 1: Penerokaan data awal

![Langkah 1: Penerokaan data awal](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/raw/branch/main/docs/images/01-preliminary-data-exploration.png)

## Apa yang dilakukan langkah ini

Buku nota memuatkan fail dan bertanya soalan pertama: berapa banyak baris dan lajur, apakah nama lajur, dan adakah nilai yang hilang atau pendua?

## Apa yang diperoleh

- Fail itu mempunyai 4,324 baris dan 9 lajur, dua daripadanya hanya mengandungi nombor baris.
- `Price` ialah satu-satunya lajur dengan nilai hilang (3,360 daripada 4,324), jadi kebanyakan pelancaran tiada harga diterbitkan.
- Satu baris ialah pendua yang tepat. Melihat sebelum mengubah apa-apa menunjukkan apa yang perlu dibuat oleh langkah pembersihan.

## Kod dalam `src/space_race/`

`load_missions`, `explore`
