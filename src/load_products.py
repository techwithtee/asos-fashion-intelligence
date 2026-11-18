"""Load raw ASOS product data into Azure SQL."""

import os
import sys
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

load_dotenv()

RAW_FILE = Path("data/products_raw.csv")
TARGET_TABLE = "products_raw"


def get_engine():
    url = URL.create(
        "mssql+pyodbc",
        username=os.environ["AZURE_SQL_USER"],
        password=os.environ["AZURE_SQL_PASSWORD"],
        host=os.environ["AZURE_SQL_SERVER"],
        database=os.environ["AZURE_SQL_DATABASE"],
        query={"driver": "ODBC Driver 18 for SQL Server"},
    )
    return create_engine(url, fast_executemany=True)


def main(path: Path = RAW_FILE) -> None:
    df = pd.read_csv(path)
    engine = get_engine()
    df.to_sql(TARGET_TABLE, engine, if_exists="replace", index=False, chunksize=1000)
    print(f"Loaded {len(df):,} rows into {TARGET_TABLE}")


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else RAW_FILE)
