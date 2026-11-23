**English** · [Dansk](Setup-da) · [Bahasa Malaysia](Setup-ms)

# Setup

## Requirements

- Python 3.14 or newer and Git.

## Steps

1. Clone the repository and open it in a terminal.
2. Create the environment and upgrade pip:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

3. Install the notebook and development extras:

```powershell
python -m pip install -e ".[notebook,dev]"
```

4. Put `mission_launches.csv` in `data/raw/` (see the README, section Data), then run the notebook and the tests:

```powershell
jupyter lab notebooks/space_missions_analysis.ipynb
python -m pytest
```

The package itself has no runtime dependencies; the notebook libraries are the optional extra `notebook`.
