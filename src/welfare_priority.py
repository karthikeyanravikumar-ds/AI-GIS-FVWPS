import pandas as pd


# =========================================================
# PUBLIC WELFARE PRIORITIZATION
# =========================================================
#
# PRD objective:
#
# Identify communities where:
#
#   1. Flood vulnerability is high
#   2. Population exposure is high
#   3. Essential-service access is poor
#   4. Community is underserved
#
# Output:
#
#   Welfare Priority Score
#   Priority Level
#   Priority Rank
#   Recommended Services
# =========================================================


def calculate_underserved_score(df):

    print("\nCalculating underserved-community score...")

    # -----------------------------------------------------
    # Underserved Score
    #
    # Service gap       = 50%
    # Population        = 30%
    # Flood exposure    = 20%
    # -----------------------------------------------------

    df["underserved_score"] = (

        df["service_gap_score"] * 0.50

        +

        df["population_score"] * 0.30

        +

        df["flood_score"] * 0.20
    )

    df["underserved_score"] = (

        df["underserved_score"]

        .clip(0, 100)

        .round(2)
    )

    return df


# =========================================================
# WELFARE PRIORITY SCORE
# =========================================================

def calculate_welfare_score(df):

    print(
        "\nCalculating public welfare priority score..."
    )

    # -----------------------------------------------------
    # PRD WEIGHTS
    #
    # Flood vulnerability       = 40%
    # Essential service gap     = 30%
    # Population exposure       = 20%
    # Underserved condition     = 10%
    # -----------------------------------------------------

    df["welfare_priority_score"] = (

        df["flood_score"] * 0.40

        +

        df["service_gap_score"] * 0.30

        +

        df["population_score"] * 0.20

        +

        df["underserved_score"] * 0.10
    )

    df["welfare_priority_score"] = (

        df["welfare_priority_score"]

        .clip(0, 100)

        .round(2)
    )

    return df


# =========================================================
# PRIORITY CLASSIFICATION
# =========================================================

def classify_priority(score):

    if score >= 75:

        return "Critical"

    elif score >= 50:

        return "High"

    elif score >= 25:

        return "Moderate"

    else:

        return "Low"


def classify_welfare_priority(df):

    df["welfare_priority"] = (

        df["welfare_priority_score"]

        .apply(
            classify_priority
        )
    )

    return df


# =========================================================
# PRIORITY RANK
# =========================================================

def calculate_priority_rank(df):

    df["priority_rank"] = (

        df["welfare_priority_score"]

        .rank(
            method="min",
            ascending=False
        )

        .astype(int)
    )

    return df


# =========================================================
# IDENTIFY PRIORITY SERVICES
# =========================================================

def identify_priority_services(df):

    print(
        "\nIdentifying priority services..."
    )

    def determine_services(row):

        services = []

        # -------------------------------------------------
        # HEALTHCARE
        # -------------------------------------------------

        if (
            row.get(
                "healthcare_gap_score",
                0
            ) >= 50
        ):

            services.append(
                "Healthcare"
            )

        # -------------------------------------------------
        # DRINKING WATER
        # -------------------------------------------------

        if (
            row.get(
                "water_gap_score",
                0
            ) >= 50
        ):

            services.append(
                "Drinking Water"
            )

        # -------------------------------------------------
        # DRAINAGE
        # -------------------------------------------------

        if (
            row.get(
                "drainage_gap_score",
                0
            ) >= 50
        ):

            services.append(
                "Drainage"
            )

        # -------------------------------------------------
        # EVACUATION
        # -------------------------------------------------

        if (
            row.get(
                "river_vulnerability_score",
                0
            ) >= 50
        ):

            services.append(
                "Evacuation Preparedness"
            )

        # -------------------------------------------------
        # FLOOD RESPONSE
        # -------------------------------------------------

        if (
            row.get(
                "flood_score",
                0
            ) >= 50
        ):

            services.append(
                "Emergency Flood Response"
            )

        # -------------------------------------------------
        # FALLBACK
        # -------------------------------------------------

        if not services:

            services.append(
                "General Preparedness"
            )

        return ", ".join(
            services
        )

    df["priority_services"] = (

        df.apply(
            determine_services,
            axis=1
        )
    )

    return df


# =========================================================
# GENERATE PRIORITY EXPLANATION
# =========================================================

def generate_priority_reason(df):

    def explain(row):

        reasons = []

        if row.get(
            "flood_score",
            0
        ) >= 50:

            reasons.append(
                "high flood exposure"
            )

        if row.get(
            "population_score",
            0
        ) >= 50:

            reasons.append(
                "high population exposure"
            )

        if row.get(
            "healthcare_gap_score",
            0
        ) >= 50:

            reasons.append(
                "limited healthcare accessibility"
            )

        if row.get(
            "water_gap_score",
            0
        ) >= 50:

            reasons.append(
                "water-service gap"
            )

        if row.get(
            "drainage_gap_score",
            0
        ) >= 50:

            reasons.append(
                "drainage-service gap"
            )

        if not reasons:

            return (
                "No major vulnerability factor "
                "crossed the priority threshold."
            )

        return (
            "Priority is influenced by "
            + ", ".join(reasons)
            + "."
        )

    df["priority_reason"] = (

        df.apply(
            explain,
            axis=1
        )
    )

    return df


# =========================================================
# COMPLETE WELFARE PRIORITIZATION
# =========================================================

def run_welfare_prioritization(df):

    print("\n")
    print("=" * 60)
    print("PUBLIC WELFARE PRIORITIZATION")
    print("=" * 60)

    # Step 1
    df = calculate_underserved_score(
        df
    )

    # Step 2
    df = calculate_welfare_score(
        df
    )

    # Step 3
    df = classify_welfare_priority(
        df
    )

    # Step 4
    df = calculate_priority_rank(
        df
    )

    # Step 5
    df = identify_priority_services(
        df
    )

    # Step 6
    df = generate_priority_reason(
        df
    )

    # -----------------------------------------------------
    # DISPLAY
    # -----------------------------------------------------

    print(
        "\nWelfare priority distribution:"
    )

    print(
        df[
            "welfare_priority"
        ]
        .value_counts()
    )

    print(
        "\nTOP 10 PRIORITY VILLAGES:"
    )

    columns = [

        "priority_rank",

        "village",

        "district",

        "flood_exposure_pct",

        "hospital_dist_km",

        "vulnerability_score",

        "underserved_score",

        "welfare_priority_score",

        "welfare_priority",

        "priority_services"
    ]

    columns = [

        column

        for column in columns

        if column in df.columns
    ]

    print(

        df.sort_values(
            "priority_rank"
        )[columns]

        .head(10)

        .to_string(
            index=False
        )
    )

    return df