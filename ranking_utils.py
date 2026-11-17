"""Reusable pairwise ranking, stability resampling, and cross-lingual correlation utilities."""

from collections import defaultdict
from typing import Dict, List
import numpy as np
import pandas as pd
from scipy.stats import kendalltau, spearmanr

REQUIRED_COLUMNS = ["query_id", "model_A", "model_B", "verdict"]
VALID_VERDICTS = ["A", "B", "Tie"]


def validate_pairwise_df(df: pd.DataFrame) -> pd.DataFrame:
    """Validate schema, drop missing values, and filter to canonical verdict labels."""
    missing_cols = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    cleaned = df.dropna(subset=REQUIRED_COLUMNS).copy()
    cleaned["verdict"] = cleaned["verdict"].astype(str).str.strip()
    cleaned = cleaned[cleaned["verdict"].isin(VALID_VERDICTS)].copy()
    return cleaned


def calculate_model_ranking(data: pd.DataFrame, tie_weight: float = 0.5) -> pd.DataFrame:
    """Compute wins, losses, ties, comparisons, win_rate, and ordinal rank per model."""
    stats = defaultdict(lambda: {"wins": 0, "losses": 0, "ties": 0, "comparisons": 0})

    for _, row in data.iterrows():
        a = row["model_A"]
        b = row["model_B"]
        verdict = row["verdict"]

        stats[a]["comparisons"] += 1
        stats[b]["comparisons"] += 1

        if verdict == "A":
            stats[a]["wins"] += 1
            stats[b]["losses"] += 1
        elif verdict == "B":
            stats[b]["wins"] += 1
            stats[a]["losses"] += 1
        elif verdict == "Tie":
            stats[a]["ties"] += 1
            stats[b]["ties"] += 1

    ranking = pd.DataFrame.from_dict(stats, orient="index")
    ranking.index.name = "model"
    ranking["win_rate"] = (
        ranking["wins"] + tie_weight * ranking["ties"]
    ) / ranking["comparisons"]
    ranking = ranking.sort_values(by="win_rate", ascending=False)
    ranking["rank"] = range(1, len(ranking) + 1)
    return ranking


def run_bootstrap_stability(
    df: pd.DataFrame,
    n_bootstraps: int = 100,
    seed: int = 42,
) -> pd.DataFrame:
    """Evaluate Kendall tau-b across bootstrap replicates drawn with replacement."""
    rng = np.random.default_rng(seed)
    query_ids = df["query_id"].unique()
    reference_scores = calculate_model_ranking(df)["win_rate"]
    records = []

    for b in range(n_bootstraps):
        sampled_queries = rng.choice(query_ids, size=len(query_ids), replace=True)
        counts = pd.Series(sampled_queries).value_counts()
        parts = [df[df["query_id"] == q] for q, c in counts.items() for _ in range(c)]
        boot_df = pd.concat(parts, ignore_index=True)

        boot_ranking = calculate_model_ranking(boot_df)
        common_models = sorted(set(reference_scores.index) & set(boot_ranking.index))
        ref_vals = [reference_scores[m] for m in common_models]
        boot_vals = [boot_ranking.loc[m, "win_rate"] for m in common_models]

        records.append(
            {
                "bootstrap_id": b + 1,
                "kendall_tau": kendalltau(ref_vals, boot_vals, variant="b").statistic,
                "spearman_rho": spearmanr(ref_vals, boot_vals).statistic,
            }
        )

    return pd.DataFrame(records)


def run_query_subsampling(
    df: pd.DataFrame,
    fractions: List[float],
    n_repeats: int = 100,
    seed: int = 42,
) -> pd.DataFrame:
    """Evaluate Kendall tau-b and Spearman rho across repeated query-level subsamples."""
    rng = np.random.default_rng(seed)
    query_ids = df["query_id"].unique()
    reference_scores = calculate_model_ranking(df)["win_rate"]
    records = []

    for fraction in fractions:
        sample_size = max(1, int(len(query_ids) * fraction))
        for repeat in range(n_repeats):
            if fraction == 1.0:
                sampled_queries = query_ids
            else:
                sampled_queries = rng.choice(query_ids, size=sample_size, replace=False)

            sample_df = df[df["query_id"].isin(sampled_queries)]
            sample_ranking = calculate_model_ranking(sample_df)
            common_models = sorted(set(reference_scores.index) & set(sample_ranking.index))

            ref_vals = [reference_scores[m] for m in common_models]
            samp_vals = [sample_ranking.loc[m, "win_rate"] for m in common_models]

            tau = kendalltau(ref_vals, samp_vals, variant="b").statistic
            rho = spearmanr(ref_vals, samp_vals).statistic

            records.append(
                {
                    "fraction": fraction,
                    "queries_used": sample_size,
                    "repeat": repeat + 1,
                    "models_compared": len(common_models),
                    "kendall_tau": tau,
                    "spearman_rho": rho,
                }
            )

    return pd.DataFrame(records)


def run_individual_model_stability(
    df: pd.DataFrame,
    fractions: List[float] = [0.25, 0.50, 0.75],
    n_repeats: int = 100,
    seed: int = 123,
) -> pd.DataFrame:
    """Track per-model rank mean and standard deviation across repeated query subsamples."""
    rng = np.random.default_rng(seed)
    query_ids = df["query_id"].unique()
    records = []

    for fraction in fractions:
        sample_size = max(1, int(len(query_ids) * fraction))
        for _ in range(n_repeats):
            selected = rng.choice(query_ids, size=sample_size, replace=False)
            sample_df = df[df["query_id"].isin(selected)]
            sample_ranking = calculate_model_ranking(sample_df)
            for model in sample_ranking.index:
                records.append(
                    {
                        "fraction": fraction,
                        "model": model,
                        "rank": sample_ranking.loc[model, "rank"],
                    }
                )

    rank_df = pd.DataFrame(records)
    return (
        rank_df.groupby(["fraction", "model"])["rank"]
        .agg(["mean", "std"])
        .reset_index()
    )


def compute_cross_lingual_correlations(
    language_rankings: Dict[str, pd.DataFrame],
    min_common_models: int = 3,
) -> pd.DataFrame:
    """Compute pairwise Kendall tau-b and Spearman rho across all language pairs."""
    languages = list(language_rankings.keys())
    results = []

    for i in range(len(languages)):
        for j in range(i + 1, len(languages)):
            lang1, lang2 = languages[i], languages[j]
            r1, r2 = language_rankings[lang1], language_rankings[lang2]
            common = sorted(set(r1.index) & set(r2.index))
            if len(common) < min_common_models:
                continue

            s1 = [r1.loc[m, "win_rate"] for m in common]
            s2 = [r2.loc[m, "win_rate"] for m in common]

            results.append(
                {
                    "language_1": lang1,
                    "language_2": lang2,
                    "common_models": len(common),
                    "kendall_tau": kendalltau(s1, s2, variant="b").statistic,
                    "spearman_rho": spearmanr(s1, s2).statistic,
                }
            )

    return pd.DataFrame(results)
