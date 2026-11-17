# Baseline Reproduction & Validation Report (Gate G2)

**Student:** Devarasetty Seetesh (`MRA2026015`)  

## 1. Environment & Data Verification
- **Status:** VERIFIED
- **Dataset:** `nthakur/mirage-bench-pairwise-judgments` (`en`, `dev` split) loaded via Hugging Face `datasets`.
- **Validated Partition:** `17,097` valid pairwise comparisons across `100` unique queries and `19` unique models (`1,798`–`1,800` comparisons per model).

## 2. Discrepancies Caught & Fixed During Baseline Audit
- **Discrepancy 1 (Loss-Counting Bug in Initial Baseline Script):**
  - *Observation:* In the initial exploratory cell, when `verdict == "B"`, `model_a` was recorded as `[model_a, 0, 0, 0]` instead of `[model_a, 0, 1, 0]`, failing to increment `model_a`'s loss count.
  - *Resolution:* Replaced with `calculate_model_ranking(data)` using explicit `wins`, `losses`, `ties`, and `comparisons` counters (`stats[a]["losses"] += 1` when `verdict == "B"`). Verified that `wins + losses + ties == comparisons` holds for all 19 models.
- **Discrepancy 2 (Whitespace & Case Normalization on Verdict Labels):**
  - *Observation:* Initial loop checked `verdict.lower() == "tie"` on raw string values without normalizing whitespace first.
  - *Resolution:* Enforced `df["verdict"] = df["verdict"].astype(str).str.strip()` and filtered strictly to `["A", "B", "Tie"]`.

## 3. Leakage & Protocol Verification
- **Baseline Win-Rate Formula:** $\text{WinRate}(m) = \frac{W_m + 0.5 T_m}{N_m}$ — **VERIFIED**.
- **Query-Level Grouping:** All subsampling is performed strictly at the `query_id` level (`df["query_id"].isin(sampled_queries)`), keeping all pairwise comparisons per query intact — **VERIFIED**.
