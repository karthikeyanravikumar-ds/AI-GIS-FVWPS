import pandas as pd

from .config import INPUT_FILE


def load_data():

    print("\nLoading GIS dataset...")

    df = pd.read_csv(INPUT_FILE)

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    # Remove completely empty columns
    df = df.dropna(axis=1, how="all")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Standard missing-value representations
    missing_values = [
        "",
        " ",
        "NA",
        "N/A",
        "na",
        "n/a",
        "NULL",
        "null",
        "-",
        "--"
    ]

    df = df.replace(missing_values, pd.NA)

    return df