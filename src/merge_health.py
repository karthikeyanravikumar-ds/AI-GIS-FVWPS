import pandas as pd
import numpy as np

from .config import DATA_DIR


# =========================================================
# FILES
# =========================================================

VILLAGE_FILE = DATA_DIR / "village_ai_ml_final.csv"
HEALTH_FILE = DATA_DIR / "health.csv"

OUTPUT_FILE = DATA_DIR / "village_ai_ml_health.csv"


# =========================================================
# LOAD DATA
# =========================================================

def load_files():

    print("\n========================================")
    print("LOADING VILLAGE + HEALTH DATA")
    print("========================================")

    village_df = pd.read_csv(VILLAGE_FILE)

    health_df = pd.read_csv(HEALTH_FILE)

    print(
        f"Village dataset : {len(village_df):,} rows"
    )

    print(
        f"Health dataset  : {len(health_df):,} rows"
    )

    return village_df, health_df


# =========================================================
# CLEAN COLUMN NAMES
# =========================================================

def clean_columns(df):

    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df


# =========================================================
# NUMERIC CONVERSION
# =========================================================

def numeric_columns(df):

    columns = [
        "distance",
        "feature_x",
        "feature_y",
        "nearest_x",
        "nearest_y"
    ]

    for column in columns:

        if column in df.columns:

            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    return df


# =========================================================
# HAVERSINE DISTANCE
# =========================================================

def haversine_distance(
    lon1,
    lat1,
    lon2,
    lat2
):

    lon1 = np.radians(lon1)
    lat1 = np.radians(lat1)

    lon2 = np.radians(lon2)
    lat2 = np.radians(lat2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = (
        np.sin(dlat / 2) ** 2
        +
        np.cos(lat1)
        *
        np.cos(lat2)
        *
        np.sin(dlon / 2) ** 2
    )

    c = 2 * np.arctan2(
        np.sqrt(a),
        np.sqrt(1 - a)
    )

    return 6371.0 * c


# =========================================================
# CALCULATE HOSPITAL DISTANCE
# =========================================================

def calculate_hospital_distance(health_df):

    print("\nCalculating hospital distances...")

    health_df = health_df.copy()

    # -----------------------------------------------------
    # Preferred method:
    # calculate distance from village coordinate
    # to nearest hospital coordinate
    # -----------------------------------------------------

    coordinate_columns = [
        "feature_x",
        "feature_y",
        "nearest_x",
        "nearest_y"
    ]

    if all(
        column in health_df.columns
        for column in coordinate_columns
    ):

        health_df["hospital_dist_km"] = haversine_distance(

            health_df["feature_x"],

            health_df["feature_y"],

            health_df["nearest_x"],

            health_df["nearest_y"]
        )

    # -----------------------------------------------------
    # Fallback:
    # existing distance field
    # -----------------------------------------------------

    elif "distance" in health_df.columns:

        health_df["hospital_dist_km"] = (

            pd.to_numeric(
                health_df["distance"],
                errors="coerce"
            )

            * 111.32

        )

    else:

        health_df["hospital_dist_km"] = np.nan


    # -----------------------------------------------------
    # Remove impossible values
    # -----------------------------------------------------

    health_df.loc[
        health_df["hospital_dist_km"] < 0,
        "hospital_dist_km"
    ] = np.nan


    return health_df


# =========================================================
# FIND BEST MATCHING ID
# =========================================================

def find_matching_id(village_df, health_df):

    possible_ids = [
        "village_id",
        "id",
        "objectid",
        "objectid_1",
        "fid"
    ]

    print("\nSearching for common village identifier...")

    for column in possible_ids:

        if (
            column in village_df.columns
            and column in health_df.columns
        ):

            village_values = set(
                village_df[column]
                .dropna()
                .astype(str)
            )

            health_values = set(
                health_df[column]
                .dropna()
                .astype(str)
            )

            overlap = (
                village_values
                .intersection(health_values)
            )

            print(
                f"{column}: "
                f"{len(overlap):,} matching IDs"
            )

            if len(overlap) > 0:

                return column

    return None


def merge_health(village_df, health_df):

    print("\nMatching villages using village + district...")

    # -----------------------------------------------------
    # Clean village names
    # -----------------------------------------------------

    village_df["_village_match"] = (
        village_df["village"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    health_df["_village_match"] = (
        health_df["village"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    # -----------------------------------------------------
    # Clean district names
    # -----------------------------------------------------

    village_df["_district_match"] = (
        village_df["district"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    health_df["_district_match"] = (
        health_df["district"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    # -----------------------------------------------------
    # Keep nearest hospital for each village
    # -----------------------------------------------------

    health_best = (

        health_df
        .sort_values(
            "hospital_dist_km"
        )
        .drop_duplicates(
            subset=[
                "_village_match",
                "_district_match"
            ],
            keep="first"
        )
    )

    # -----------------------------------------------------
    # Select hospital information
    # -----------------------------------------------------

    hospital_columns = [
        "_village_match",
        "_district_match",
        "hospital_dist_km"
    ]

    if "name" in health_best.columns:
        hospital_columns.append("name")

    if "amenity" in health_best.columns:
        hospital_columns.append("amenity")

    # -----------------------------------------------------
    # Merge
    # -----------------------------------------------------

    merged = village_df.merge(

        health_best[hospital_columns],

        on=[
            "_village_match",
            "_district_match"
        ],

        how="left",

        suffixes=(
            "",
            "_hospital"
        )
    )

    # -----------------------------------------------------
    # Remove temporary columns
    # -----------------------------------------------------

    merged = merged.drop(
        columns=[
            "_village_match",
            "_district_match"
        ],
        errors="ignore"
    )

    return merged


# =========================================================
# MAIN
# =========================================================

def main():

    village_df, health_df = load_files()

    village_df = clean_columns(
        village_df
    )

    health_df = clean_columns(
        health_df
    )

    health_df = numeric_columns(
        health_df
    )

    health_df = calculate_hospital_distance(
        health_df
    )

    print("\nHospital distance statistics:")

    print(
        health_df[
            "hospital_dist_km"
        ].describe()
    )

    merged = merge_health(
        village_df,
        health_df
    )

    # -----------------------------------------------------
    # Final cleaning
    # -----------------------------------------------------

    merged["hospital_dist_km"] = (

        pd.to_numeric(
            merged["hospital_dist_km"],
            errors="coerce"
        )

    )

    # -----------------------------------------------------
    # Check merge
    # -----------------------------------------------------

    matched = (
        merged["hospital_dist_km"]
        .notna()
        .sum()
    )

    total = len(merged)

    percentage = (
        matched / total * 100
        if total > 0
        else 0
    )

    print("\n========================================")
    print("HEALTH MERGE RESULTS")
    print("========================================")

    print(
        f"Total villages : {total:,}"
    )

    print(
        f"Matched        : {matched:,}"
    )

    print(
        f"Unmatched      : {total - matched:,}"
    )

    print(
        f"Match rate     : {percentage:.2f}%"
    )

    print(
        "\nHospital distance range:"
    )

    print(
        f"Minimum: "
        f"{merged['hospital_dist_km'].min():.2f} km"
    )

    print(
        f"Maximum: "
        f"{merged['hospital_dist_km'].max():.2f} km"
    )

    print(
        f"Mean: "
        f"{merged['hospital_dist_km'].mean():.2f} km"
    )

    # -----------------------------------------------------
    # Save
    # -----------------------------------------------------

    merged.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"\nSaved merged dataset:"
    )

    print(
        OUTPUT_FILE
    )


if __name__ == "__main__":

    main()