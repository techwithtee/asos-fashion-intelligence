# Architecture

## Flow

```
Raw CSV  ->  load_products.py  ->  Azure SQL (raw table)
                                        |
                          01_exploration.sql / 02_data_quality.sql
                                        |
                              clean_products.py
                                        |
                             validate_products.py
                                        |
                      03_transformations.sql -> 04_analytics.sql
```

## Components
| Layer | Tooling | Notes |
|-------|---------|-------|
| Ingestion | Python, SQLAlchemy, pyodbc | Loads raw file to a staging table |
| Storage | Azure SQL Database | Raw, clean and analytics schemas |
| Cleaning | Python, pandas | Standardise types, text, nulls |
| Validation | Python | Rule-based checks, fail loudly |
| Transformation | SQL | Views/tables for analytics |

## Configuration
Connection details come from environment variables in `.env` (never committed).
