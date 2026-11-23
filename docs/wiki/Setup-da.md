[English](Setup) · **Dansk** · [Bahasa Malaysia](Setup-ms)

# Opsætning

## Krav

- Python 3.14 eller nyere og Git.

## Trin

1. Klon repositoryet og åbn det i en terminal.
2. Opret miljøet og opgradér pip:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

3. Installér notebook- og udviklingstilvalgene:

```powershell
python -m pip install -e ".[notebook,dev]"
```

4. Læg `mission_launches.csv` i `data/raw/` (se README, afsnittet Data), og kør derefter notebooken og testene:

```powershell
jupyter lab notebooks/space_missions_analysis.ipynb
python -m pytest
```

Selve pakken har ingen kørselsafhængigheder; notebook-bibliotekerne er tilvalget `notebook`.
