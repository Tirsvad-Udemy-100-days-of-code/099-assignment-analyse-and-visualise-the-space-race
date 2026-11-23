[English](Step-01-Exploration) · **Dansk** · [Bahasa Malaysia](Step-01-Exploration-ms)

# Trin 1: Indledende dataudforskning

![Trin 1: Indledende dataudforskning](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/099-assignment-analyse-and-visualise-the-space-race/raw/branch/main/docs/images/01-preliminary-data-exploration.png)

## Hvad trinnet gør

Notebooken indlæser filen og stiller de første spørgsmål: hvor mange rækker og kolonner, hvad hedder kolonnerne, og er der manglende værdier eller dubletter?

## Hvad vi fik ud af det

- Filen har 4.324 rækker og 9 kolonner, hvoraf to kun indeholder et rækkenummer.
- `Price` er den eneste kolonne med manglende værdier (3.360 af 4.324), så de fleste opsendelser har ingen offentliggjort pris.
- Én række er en nøjagtig dublet. At kigge før man ændrer noget viser, hvad rensningen skal gøre.

## Kode i `src/space_race/`

`load_missions`, `explore`
