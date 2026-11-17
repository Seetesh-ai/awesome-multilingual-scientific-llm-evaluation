"""End-to-end reproducible entrypoint for MIRAGE-Bench ranking stability experiments."""

import argparse
from pathlib import Path
import sys
import matplotlib.pyplot as plt
import pandas as pd
import yaml
from datasets import load_dataset

sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.ranking_utils import (
    calculate_model_ranking,
    compute_cross_lingual_correlations,
    run_bootstrap_stability,
    run_individual_model_stability,
    run_query_subsampling,
    validate_pairwise_df,
)


def main():
    parser = argparse.ArgumentParser(description="Run MIRAGE-Bench pairwise stability study.")
    parser.add_argument("--config", type=str, default="configs/experiment_config.yaml")
    parser.add_argument("--output_dir", type=str, default="results")
    args = parser.parse_args()

    with open(args.config, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    out_dir = Path(args.output_dir)
    tables_dir = out_dir / "tables"
    figures_dir = out_dir / "figures"
    tables_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    dataset_id = cfg["dataset"]["id"]
    primary_lang = cfg["dataset"]["primary_language"]
    split = cfg["dataset"]["split"]

    print(f"Loading primary dataset: {dataset_id} ({primary_lang}/{split})...")
    en_raw = load_dataset(dataset_id, primary_lang)[split].to_pandas()
    en_df = validate_pairwise_df(en_raw)

    # 1. Baseline ranking (M1)
    ranking = calculate_model_ranking(en_df, tie_weight=cfg["evaluation"]["tie_weight"])
    ranking.to_csv(tables_dir / "model_ranking.csv")

    # 2. Bootstrap & Query-sample sensitivity (M2)
    boot_df = run_bootstrap_stability(
        en_df,
        n_bootstraps=cfg["evaluation"]["n_bootstraps"],
        seed=cfg["seeds"]["bootstrap_seed"],
    )
    boot_df.to_csv(tables_dir / "bootstrap_stability.csv", index=False)

    repeated_df = run_query_subsampling(
        en_df,
        fractions=cfg["evaluation"]["sample_fractions"],
        n_repeats=cfg["evaluation"]["n_repeats"],
        seed=cfg["seeds"]["subsample_seed"],
    )
    repeated_df.to_csv(tables_dir / "repeated_sampling.csv", index=False)

    summary_df = (
        repeated_df.groupby("fraction")["kendall_tau"]
        .agg(["mean", "std", "min", "max"])
        .reset_index()
    )
    summary_df.to_csv(tables_dir / "stability_summary.csv", index=False)

    confidence_df = (
        repeated_df[repeated_df["fraction"] < 1.0]
        .groupby("fraction")["kendall_tau"]
        .agg(
            mean="mean",
            lower_95=lambda x: x.quantile(0.025),
            upper_95=lambda x: x.quantile(0.975),
        )
        .reset_index()
    )
    confidence_df.to_csv(tables_dir / "confidence_intervals.csv", index=False)

    fig, ax = plt.subplots(figsize=(7.5, 4.3))
    frac_pct = summary_df["fraction"] * 100
    ax.fill_between(
        confidence_df["fraction"] * 100,
        confidence_df["lower_95"],
        confidence_df["upper_95"],
        color="#1f77b4",
        alpha=0.15,
        label="95% Empirical Percentile Interval",
    )
    ax.errorbar(
        frac_pct,
        summary_df["mean"],
        yerr=summary_df["std"],
        fmt="-o",
        color="#1f77b4",
        linewidth=2,
        capsize=5,
        label="Mean Kendall's tau-b +/- 1 SD",
    )
    ax.set_xlabel("Evaluation Query Budget (% of 100 dev queries)")
    ax.set_ylabel("Kendall's tau-b vs. Full Ranking")
    ax.set_title("Query-Sample Sensitivity Across 100 Repeated Subsamples")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig(figures_dir / "fig2_ranking_stability.png", dpi=300)
    plt.close()

    # 3. Individual model tier stability
    indiv_df = run_individual_model_stability(
        en_df,
        fractions=[0.25, 0.50, 0.75],
        n_repeats=cfg["evaluation"]["n_repeats"],
        seed=cfg["seeds"]["individual_rank_seed"],
    )
    indiv_df.to_csv(tables_dir / "individual_model_stability.csv", index=False)

    # 4. Cross-lingual ranking transfer (M3)
    language_rankings = {}
    language_rows = []
    for lang in cfg["dataset"]["multilingual_languages"]:
        ds = load_dataset(dataset_id, lang)
        if split in ds:
            lang_df = validate_pairwise_df(ds[split].to_pandas())
            lang_rank = calculate_model_ranking(lang_df, tie_weight=cfg["evaluation"]["tie_weight"])
            language_rankings[lang] = lang_rank
            language_rows.append(
                {
                    "language": lang,
                    "records": len(lang_df),
                    "queries": lang_df["query_id"].nunique(),
                    "models": len(lang_rank),
                    "top_model": lang_rank.index[0],
                    "top_model_win_rate": lang_rank.iloc[0]["win_rate"],
                }
            )

    pd.DataFrame(language_rows).to_csv(tables_dir / "language_summary.csv", index=False)
    corr_df = compute_cross_lingual_correlations(
        language_rankings,
        min_common_models=cfg["evaluation"]["min_common_models_cross_lingual"],
    )
    corr_df.to_csv(tables_dir / "language_correlations.csv", index=False)
    print("All experiments completed and saved to:", out_dir)


if __name__ == "__main__":
    main()
