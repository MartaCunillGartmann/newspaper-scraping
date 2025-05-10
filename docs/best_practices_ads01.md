
# Best Practices für dein ADS-01 Newspaper Scraping Projekt

## 📁 Projektstruktur

- `input/` – Eingabedaten (z. B. HTML-Dateien, CSVs)
- `output/` – Zwischenergebnisse, bereinigte Daten etc.
- `scripts/` – Python-Skripte (z. B. `merge.py`, `cleaning.py`)
- `lib_py/` – ausgelagerte Funktionen, Hilfsfunktionen
- `tests/` – Unit Tests mit `pytest`
- `docs/` – Dokumentation (z. B. README, Markdown-Notizen)
- `notebooks/` – Jupyter Notebooks für Exploratives

## 🧪 Testing mit `pytest`

- Test-Dateien z. B. `test_merge.py`
- Testfunktionen beginnen mit `test_`
- Verwende `assert`, um Verhalten zu testen
- Optional: `tests/input/` für kleine Test-Daten

## 📓 Jupyter Notebooks

- **Zelle 1**: Imports
- **Zelle 2**: Pfad-Konstanten, z. B.:

```python
FILENAME = "input/raw_data.csv"
```

- Danach: Nutzung dieser Konstanten im gesamten Notebook
- Code auslagern in `scripts/` und importieren

## 🧠 Code-Organisation

- `if __name__ == "__main__":` für `.py`-Dateien
- Funktionen mit Docstrings dokumentieren
- Kein Copy-Paste in vielen Dateien

## 🧰 Technisches Setup

- Nutzung von `pipenv`
- virtuelle Umgebung über `Pipfile`, `Pipfile.lock`
- `pipenv shell` zum Aktivieren
- `.gitignore` enthält `.venv/`, `__pycache__/`, `*.pyc`

## 🌐 Webscraping

- HTML-Struktur analysieren mit Rechtsklick → „Untersuchen“
- Relevante Tags: `<h1>`, `<h2>`, `<p>`, `<a>`, `<div>`
- Nutze `BeautifulSoup`, um gezielt Elemente zu finden
- Clean Code: Trennung von Parsing und Speicherung

