# ASOS Fashion Intelligence

An end-to-end data engineering and analytics project built on ASOS product data. It covers ingestion, cleaning, validation, SQL transformation in Azure SQL, and analytics for fashion-retail insight.

## Goals

- Ingest raw ASOS product data into Azure SQL
- Clean and validate the data with reproducible Python scripts
- Explore, transform and analyse it with SQL
- Document decisions, learning and skills gained along the way

## Repository Structure

| Path | Purpose |
|------|---------|
| `data/` | Local data files (not committed, see `data/README.md`) |
| `docs/` | Project overview, architecture, decisions, learning journal, JD skills tracker |
| `src/` | Python scripts: load, clean and validate products |
| `sql/` | Numbered SQL scripts: exploration, data quality, transformations, analytics |
| `notebooks/` | Exploratory notebooks |
| `tests/` | Automated tests |
| `screenshots/` | Evidence of Azure SQL setup, ingestion and SQL exploration |

## Getting Started

```bash
git clone https://github.com/<your-username>/asos-fashion-intelligence.git
cd asos-fashion-intelligence
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file (never commit it) with your Azure SQL connection details:

```
AZURE_SQL_SERVER=your-server.database.windows.net
AZURE_SQL_DATABASE=your-database
AZURE_SQL_USER=your-user
AZURE_SQL_PASSWORD=your-password
```

## Pipeline

1. `src/load_products.py` loads raw product data into Azure SQL
2. `sql/01_exploration.sql` and `sql/02_data_quality.sql` profile the data
3. `src/clean_products.py` cleans and standardises fields
4. `src/validate_products.py` runs validation checks
5. `sql/03_transformations.sql` and `sql/04_analytics.sql` build analytical outputs

## Status

Work in progress. See `docs/learning-journal.md` for progress notes.
