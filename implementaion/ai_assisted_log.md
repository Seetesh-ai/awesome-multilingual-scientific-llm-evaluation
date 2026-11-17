# Human-AI Collaboration & Provenance Log

**Student:** Devarasetty Seetesh (`MRA2026015`)  

| Stage / Task | AI Assistance Used | Human Verification & Manual Corrections | Outcome |
| :--- | :--- | :--- | :--- |
| **1. Environment & Repo Setup** | Generated Colab dependency setup and `vectara/mirage-bench` clone commands. | Verified library versions (`numpy`, `pandas`, `pyarrow`, `datasets`, `scipy`, `matplotlib`) and inspected `README.md`. | Reproducible Colab environment. |
| **2. Data Exploration & Schema Audit** | Generated multi-language loader across 18 splits of `nthakur/mirage-bench-pairwise-judgments`. | Removed an uninitialized `builders` template cell left from initial scaffolding; verified non-null counts and unique `query_id` / model counts. | Clean, validated DataFrames across 18 languages. |
| **3. Baseline Ranking Implementation** | Generated initial loop converting pairwise verdicts into model win/loss/tie counts. | **Manual Bug Fix:** Caught that `verdict == "B"` logged `0` losses for `model_A` (`[model_a, 0, 0, 0]`). Rewrote into `calculate_model_ranking()` with explicit `comparisons` accounting. | Verified baseline ranking table (`model_ranking.csv`). |
| **4. Stability & Cross-Lingual Analysis** | Generated query-level bootstrap, fraction subsampling (`R=100`), and cross-lingual correlation scripts. | Enforced query-level (`query_id`) subsampling to avoid partial-query leakage, fixed seeds (`42`, `123`), and exported traceable CSVs and PNGs. | Complete experimental evidence package. |
