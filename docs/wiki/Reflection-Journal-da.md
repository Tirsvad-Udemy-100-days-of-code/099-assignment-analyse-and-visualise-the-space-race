[English](Reflection-Journal) · **Dansk** · [Bahasa Malaysia](Reflection-Journal-ms)

# Refleksionsjournal

## Fremgangsmåde

Jeg byggede projektet i fire trin, hvert gennemgået før det næste: en plan, repositoriets grundlag, dataforberedelsen og analysen og til sidst dokumentationen. Logikken ligger i små testede funktioner, og notebooken kalder dem kun, så hvert svar kan kontrolleres uden at køre et diagram.

## Hvad var nemt

At tælle og gruppere med pandas (`value_counts`, `groupby`) besvarede de fleste spørgsmål på en eller to linjer, og plotly gjorde resultaterne til diagrammer med lidt kode.

## Hvad var svært

Dataene. Kun en femtedel af opsendelserne har en pris, én pris er en enorm outlier, opsendelsessteder på havet har intet land, og USSR opsendte fra Kasakhstan. Hver af dem krævede en beslutning, som jeg skrev ned i `constants.py` eller på trinnets wikiside.

## Største læring

Kig på dataene, før du ændrer dem, og erstat aldrig manglende værdier med et gæt, medmindre du kan forsvare det. En rate eller et gennemsnit uden sit antal ved siden af kan vildlede, som fejlraten for 1950'erne viser.

## Hvad jeg ville gøre anderledes

Jeg ville tjekke licensen på datafilen først, så dataene kunne være en del af repositoriet, og jeg ville tilføje en lille tabel over prisoutlierne, så gennemsnitsdiagrammet er lettere at læse.
