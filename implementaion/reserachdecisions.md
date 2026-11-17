# Research Decisions & Gate G1 Brief

**Student:** Devarasetty Seetesh (`MRA2026015`)  
**Topic:** Query-Sample Sensitivity and Cross-Lingual Rank Transfer in Pairwise LLM-as-a-Judge Evaluation  

## 1. Review Topic & Verified Gap
- **Domain:** Multilingual Retrieval-Augmented Generation (RAG) & Automated LLM-as-a-Judge Evaluation.
- **Verified Gap:** Pairwise LLM-as-a-judge leaderboards (e.g., MIRAGE-Bench) aggregate head-to-head preferences into scalar model rankings. Two methodological assumptions require empirical validation:
  1. **Query-Sample Sufficiency:** How many evaluation queries are required before pairwise win-rate rankings stabilize, and how much do individual model ranks fluctuate under reduced query budgets?
  2. **Cross-Lingual Ranking Transfer:** Do English pairwise model rankings generalize reliably across typologically diverse and lower-resource languages, or do model hierarchies shift across languages?

## 2. Research Questions
- **RQ1 (Baseline Ranking):** What is the baseline win-rate hierarchy of the 19 evaluated RAG/LLM systems on the English MIRAGE-Bench development partition?
- **RQ2 (Query-Sample Sensitivity):** How rapidly does ranking stability (Kendall's $\tau_b$ and Spearman's $\rho$) converge across query sample fractions (`25%`, `50%`, `75%`, `100%`) over `100` repeated random subsamples?
- **RQ3 (Cross-Lingual Consistency):** To what extent do pairwise model rankings correlate across all `18` languages in MIRAGE-Bench?

## 3. Approved Study Pathway
- **Pathway B (Controlled Comparative & Robustness Study):** Establish a verified pairwise win-rate baseline on English (`en`), then run controlled query-subsampling sensitivity experiments (`R=100` repeats per fraction, fixed seeds `42` and `123`) and cross-lingual rank correlation analysis across 18 languages.
