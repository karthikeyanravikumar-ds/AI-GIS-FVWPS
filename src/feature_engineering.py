import numpy as np
import pandas as pd


def convert_numeric(df):
    """
    Convert GIS attributes to numeric values.
    """

    numeric_columns = [
        "total_popu",
        "total_hous",
        "village_area_km2",
        "flood_area_km2",
        "flood_exposure_pct",
        "hospital_dist_km",
        "river_distance_km",
        "river_distance_m",
        "tapwater_t",
        "tapwater_u",
        "open_drain",
        "covered_we",
        "handpump_s",
        "tubewell_b",
        "wells_tub",
        "tanks_lake",
        "area_irrig",
        "culturable",
    ]

    for column in numeric_columns:

        if column in df.columns:

            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    return df


def minmax_score(series):
    """
    Convert a variable to a 0-100 score.

    Higher value = higher vulnerability,
    unless explicitly reversed later.
    """

    series = pd.to_numeric(
        series,
        errors="coerce"
    )

    series = series.replace(
        [np.inf, -np.inf],
        np.nan
    )

    # Replace missing values with median
    median = series.median()

    if pd.isna(median):
        median = 0

    series = series.fillna(median)

    minimum = series.min()
    maximum = series.max()

    # Avoid division by zero
    if maximum == minimum:

        return pd.Series(
            50.0,
            index=series.index
        )

    return (
        (series - minimum)
        /
        (maximum - minimum)
    ) * 100


def engineer_features(df):

    print("\n========================================")
    print("PRD FEATURE ENGINEERING")
    print("========================================")

    # ---------------------------------------------------------
    # Convert GIS data
    # ---------------------------------------------------------

    df = convert_numeric(df)

    # ---------------------------------------------------------
    # 1. POPULATION DENSITY
    # ---------------------------------------------------------

    if (
        "total_popu" in df.columns
        and
        "village_area_km2" in df.columns
    ):

        df["population_density"] = np.where(

            df["village_area_km2"] > 0,

            df["total_popu"]
            /
            df["village_area_km2"],

            0
        )

    else:

        df["population_density"] = 0


    # ---------------------------------------------------------
    # 2. WATER AVAILABILITY
    # ---------------------------------------------------------

    water_columns = [
        column

        for column in [
            "tapwater_t",
            "tapwater_u",
            "handpump_s",
            "tubewell_b",
            "wells_tub",
            "tanks_lake"
        ]

        if column in df.columns
    ]

    if water_columns:

        df["water_availability"] = (
            df[water_columns]
            .fillna(0)
            .sum(axis=1)
        )

    else:

        df["water_availability"] = 0


    # ---------------------------------------------------------
    # 3. DRAINAGE AVAILABILITY
    # ---------------------------------------------------------

    drainage_columns = [
        column

        for column in [
            "open_drain",
            "covered_we"
        ]

        if column in df.columns
    ]

    if drainage_columns:

        df["drainage_availability"] = (
            df[drainage_columns]
            .fillna(0)
            .sum(axis=1)
        )

    else:

        df["drainage_availability"] = 0


    # ---------------------------------------------------------
    # 4. HOSPITAL DISTANCE
    # ---------------------------------------------------------

    if "hospital_dist_km" not in df.columns:

        df["hospital_dist_km"] = np.nan

    df["hospital_dist_km"] = pd.to_numeric(
        df["hospital_dist_km"],
        errors="coerce"
    )

    valid_hospital = df["hospital_dist_km"].notna().sum()

    print(
        f"Hospital distance available for "
        f"{valid_hospital}/{len(df)} villages."
    )

    # ---------------------------------------------------------
    # Healthcare accessibility score
    # ---------------------------------------------------------

    if valid_hospital > 0:

        df["healthcare_gap_score"] = minmax_score(
            df["hospital_dist_km"]
        )

    else:

        # No hospital data for current study area.
        # Do NOT create fake values.
        df["healthcare_gap_score"] = np.nan


    # ---------------------------------------------------------
    # 5. RIVER DISTANCE
    # ---------------------------------------------------------

    if (
        "river_distance_km" not in df.columns
        and
        "river_distance_m" in df.columns
    ):

        df["river_distance_km"] = (
            df["river_distance_m"] / 1000
        )

    elif "river_distance_km" not in df.columns:

        print(
            "WARNING: river distance not found."
        )

        df["river_distance_km"] = 0


    # =========================================================
    # VULNERABILITY FEATURES
    # =========================================================

    # ---------------------------------------------------------
    # FLOOD VULNERABILITY
    # ---------------------------------------------------------

    df["flood_score"] = minmax_score(
        df["flood_exposure_pct"]
    )


    # ---------------------------------------------------------
    # POPULATION EXPOSURE
    # ---------------------------------------------------------

    df["population_score"] = minmax_score(
        df["population_density"]
    )


    # ---------------------------------------------------------
    # HEALTHCARE ACCESS GAP
    #
    # Greater hospital distance = greater vulnerability
    # ---------------------------------------------------------

    df["healthcare_gap_score"] = minmax_score(
        df["hospital_dist_km"]
    )


    # ---------------------------------------------------------
    # WATER ACCESS GAP
    #
    # Greater water infrastructure =
    # lower vulnerability.
    # ---------------------------------------------------------

    water_score = minmax_score(
        df["water_availability"]
    )

    df["water_gap_score"] = (
        100 - water_score
    )


    # ---------------------------------------------------------
    # DRAINAGE GAP
    # ---------------------------------------------------------

    drainage_score = minmax_score(
        df["drainage_availability"]
    )

    df["drainage_gap_score"] = (
        100 - drainage_score
    )


    # ---------------------------------------------------------
    # ESSENTIAL SERVICE GAP
    # Dynamic weighting when a service dataset is unavailable
    # ---------------------------------------------------------

    service_data = {}

    if df["healthcare_gap_score"].notna().any():

        service_data["healthcare"] = (
            df["healthcare_gap_score"]
        )

    if df["water_gap_score"].notna().any():

        service_data["water"] = (
            df["water_gap_score"]
        )

    if df["drainage_gap_score"].notna().any():

        service_data["drainage"] = (
            df["drainage_gap_score"]
        )

    if service_data:

        service_df = pd.DataFrame(
            service_data
        )

        df["service_gap_score"] = (
            service_df
            .mean(axis=1)
            .fillna(0)
        )

    else:

        df["service_gap_score"] = 0

    # ---------------------------------------------------------
    # RIVER VULNERABILITY
    #
    # Smaller distance = higher vulnerability
    # ---------------------------------------------------------

    river_score = minmax_score(
        df["river_distance_km"]
    )

    df["river_vulnerability_score"] = (
        100 - river_score
    )

    # ---------------------------------------------------------
    # SHOW CREATED FEATURES
    # ---------------------------------------------------------

    created_features = [
        "population_density",
        "water_availability",
        "drainage_availability",
        "flood_score",
        "population_score",
        "healthcare_gap_score",
        "water_gap_score",
        "drainage_gap_score",
        "service_gap_score",
        "river_vulnerability_score",
    ]

    print("\nCreated features:")

    for feature in created_features:

        if feature in df.columns:

            print(f"  ✓ {feature}")

    return df