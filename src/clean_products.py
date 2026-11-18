"""Clean and standardise raw ASOS product data."""

from pathlib import Path

import pandas as pd

RAW_FILE = Path("data/products_raw.csv")
CLEAN_FILE = Path("data/products_clean.csv")


def clean_products(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Trim whitespace in text columns
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

    df = df.drop_duplicates()
    return df


def main() -> None:
    df = pd.read_csv(RAW_FILE)
    cleaned = clean_products(df)
    cleaned.to_csv(CLEAN_FILE, index=False)
    print(f"Cleaned {len(df):,} -> {len(cleaned):,} rows")


if __name__ == "__main__":
    main()
