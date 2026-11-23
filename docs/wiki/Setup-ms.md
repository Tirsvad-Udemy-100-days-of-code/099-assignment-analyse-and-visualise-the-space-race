[English](Setup) · [Dansk](Setup-da) · **Bahasa Malaysia**

# Persediaan

## Keperluan

- Python 3.14 atau lebih baharu dan Git.

## Langkah

1. Klon repositori dan buka dalam terminal.
2. Cipta persekitaran dan naik taraf pip:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

3. Pasang tambahan buku nota dan pembangunan:

```powershell
python -m pip install -e ".[notebook,dev]"
```

4. Letakkan `mission_launches.csv` dalam `data/raw/` (lihat README, bahagian Data), kemudian jalankan buku nota dan ujian:

```powershell
jupyter lab notebooks/space_missions_analysis.ipynb
python -m pytest
```

Pakej itu sendiri tiada kebergantungan masa jalan; pustaka buku nota ialah tambahan pilihan `notebook`.
