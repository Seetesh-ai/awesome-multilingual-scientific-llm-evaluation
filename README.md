# Dataset Access & Protocol

- **Dataset ID:** `nthakur/mirage-bench-pairwise-judgments` (Hugging Face Datasets)
- **Official Benchmark Repository:** `https://github.com/vectara/mirage-bench`
- **Splits Used:** `dev` partition across 18 languages (`ar`, `bn`, `de`, `en`, `es`, `fa`, `fi`, `fr`, `hi`, `id`, `ja`, `ko`, `ru`, `sw`, `te`, `th`, `yo`, `zh`).
- **Columns:** `query_id`, `model_A`, `model_B`, `verdict` (`A`, `B`, `Tie`), `judge`.
- **Validation & Filtering:**
  1. Drop rows with missing values in `["query_id", "model_A", "model_B", "verdict"]`.
  2. Strip leading/trailing whitespace from `verdict`.
  3. Keep only documented verdict labels (`A`, `B`, `Tie`).
- **Redistribution Policy:** Raw parquet files are fetched dynamically via `datasets.load_dataset()` and are not redistributed inside this repository.
