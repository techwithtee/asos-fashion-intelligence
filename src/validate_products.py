"""Validate cleaned ASOS product data."""

import sys
from pathlib import Path

import pandas as pd

CLEAN_FILE = Path("data/products_clean.csv")


def validate_products(df: pd.DataFrame) -> list[str]:
    """Return a list of validation error messages (empty means valid)."""
    errors: list[str] = []

    if df.empty:
        errors.append("Dataset is empty")

    if df.duplicated().any():
        errors.append(f"{int(df.duplicated().sum())} duplicate rows found")

    null_counts = df.isna().sum()
    for col, n in null_counts[null_counts > 0].items():
        errors.append(f"Column '{col}' has {n} null values")

    return errors


def main() -> int:
    df = pd.read_csv(CLEAN_FILE)
    errors = validate_products(df)
    if errors:
        print("Validation failed:")
        for e in errors:
            print(f" - {e}")
        return 1
    print("Validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
