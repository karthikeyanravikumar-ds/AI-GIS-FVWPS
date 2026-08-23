from .data_loader import load_data
from .feature_engineering import engineer_features
from .vulnerability_model import run_vulnerability_model
from .welfare_priority import run_welfare_prioritization

from .config import (
    FINAL_OUTPUT,
    TOP_PRIORITY_OUTPUT,
    CLUSTER_OUTPUT
)


def main():

    print("\n")
    print("=" * 70)
    print("AI-GIS BASED FLOOD VULNERABILITY")
    print("AND PUBLIC WELFARE PRIORITIZATION")
    print("=" * 70)

    # =====================================================
    # STEP 1
    # Load data
    # =====================================================

    df = load_data()

    # =====================================================
    # STEP 2
    # Feature engineering
    # =====================================================

    df = engineer_features(
        df
    )

    # =====================================================
    # STEP 3
    # ML vulnerability model
    # =====================================================

    (
        df,
        model,
        scaler,
        best_k
    ) = run_vulnerability_model(
        df
    )

    # =====================================================
    # STEP 4
    # Welfare prioritization
    # =====================================================

    df = run_welfare_prioritization(
        df
    )

    # =====================================================
    # STEP 5
    # Save final dataset
    # =====================================================

    df.to_csv(
        FINAL_OUTPUT,
        index=False
    )

    # =====================================================
    # STEP 6
    # Save top priority villages
    # =====================================================

    top_priority = (

        df.sort_values(
            "welfare_priority_score",
            ascending=False
        )

        .head(25)
    )

    top_priority.to_csv(
        TOP_PRIORITY_OUTPUT,
        index=False
    )

    # =====================================================
    # STEP 7
    # Cluster summary
    # =====================================================

    cluster_summary = (

        df.groupby(
            [
                "ml_cluster",
                "ml_risk_group"
            ]
        )

        .agg(

            villages=(
                "village",
                "count"
            ),

            average_vulnerability=(
                "vulnerability_score",
                "mean"
            ),

            average_service_gap=(
                "service_gap_score",
                "mean"
            ),

            average_welfare_priority=(
                "welfare_priority_score",
                "mean"
            )
        )

        .reset_index()
    )

    cluster_summary.to_csv(
        CLUSTER_OUTPUT,
        index=False
    )

    # =====================================================
    # FINAL OUTPUT
    # =====================================================

    print("\n")
    print("=" * 70)
    print("FINAL MODEL COMPLETE")
    print("=" * 70)

    print(
        f"\nML clusters selected: {best_k}"
    )

    print(
        "\nVulnerability distribution:"
    )

    print(
        df[
            "vulnerability_class"
        ]
        .value_counts()
    )

    print(
        "\nWelfare priority distribution:"
    )

    print(
        df[
            "welfare_priority"
        ]
        .value_counts()
    )

    print("\nOutput files:")

    print(
        f"\n✓ {FINAL_OUTPUT}"
    )

    print(
        f"✓ {TOP_PRIORITY_OUTPUT}"
    )

    print(
        f"✓ {CLUSTER_OUTPUT}"
    )

    print("\n")
    print("=" * 70)
    print("READY FOR GEMINI AI")
    print("=" * 70)


if __name__ == "__main__":

    main()