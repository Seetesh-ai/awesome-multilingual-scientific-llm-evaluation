# Awesome Multilingual LLM Reliability

A curated collection of research papers, datasets, tools, implementations, and
learning resources on the reliability of Large Language Models (LLMs) when used for
multilingual scientific literature analysis — covering cross-lingual retrieval,
citation/hallucination integrity, tokenization fairness, and evaluation bias.

## Contents
- [Overview](#overview)
- [AI-Assisted Research Paper](#ai-assisted-research-paper)
- [Survey and Foundational Papers](#survey-and-foundational-papers)
- [Benchmarks and Evaluation](#benchmarks-and-evaluation)
- [Cross-Lingual RAG and Retrieval](#cross-lingual-rag-and-retrieval)
- [Citation and Hallucination Integrity](#citation-and-hallucination-integrity)
- [Tokenization Fairness](#tokenization-fairness)
- [Domain / Terminology Alignment](#domain--terminology-alignment)
- [Datasets](#datasets)
- [Tools and Libraries](#tools-and-libraries)
- [GitHub Implementations](#github-implementations)
- [Tutorials and Learning Resources](#tutorials-and-learning-resources)
- [Citation Integrity Audit](#citation-integrity-audit)
- [License](#license)

## Overview

Large Language Models are increasingly used across the scientific pipeline for
literature synthesis, cross-lingual systematic review, and evidence retrieval. While
these models perform strongly on English scientific text, performance degrades
sharply once non-English or low-resource languages are involved. This repository
collects verified research on why that degradation happens and how it is measured:
uneven tokenization across scripts, weaker cross-lingual retrieval and embedding
alignment, higher hallucination and citation-fabrication rates outside English, and
systematic bias in the LLM-as-a-judge evaluators used to score multilingual output.

The problem matters for science specifically because a large share of research in
agriculture, regional ecology, public health, and localized engineering is published
outside English-language venues, and errors introduced during multilingual synthesis
(mistranslated terminology, fabricated citations, distorted meta-analyses) can
propagate into downstream research decisions. This collection organizes recent
benchmarks (MMLU-ProX, MM-Eval, MIRAGE-Bench, MEMERAG), tokenization-fairness studies,
cross-lingual retrieval work, and a growing body of research specifically on citation
hallucination in AI-assisted scientific writing — the same failure mode this
repository's own citation-integrity audit was built to guard against.

## AI-Assisted Research Paper
[View Paper](paper/AI_Assisted_Research_Paper.pdf) — *Evaluating Multilingual
Reliability of Large Language Models in Scientific Literature Analysis*. A synthesis
of failure modes in multilingual LLM use for scientific literature review, covering
semantic/nomenclature fidelity, cross-lingual RAG degradation, and citation integrity.

*(Sections below list papers by category — see the References file for the full
verified list with one-line explanations.)*

## Citation Integrity Audit
[View Audit](citation-audit/Citation_Integrity_Audit.pdf) — References and claims in
the AI-assisted paper above were independently checked against publisher pages,
arXiv, and Semantic Scholar before inclusion in this repository; see the audit
document for the full methodology and findings.

## License
This repository's own content (README, curation, audit) is released under the MIT
License — see [LICENSE](LICENSE). Linked third-party papers, datasets, and tools
retain their original licenses; no copyrighted third-party PDFs are hosted here.

## ═══════════════════ FILE: references/references.md ═══════════════════

# References

Format per assignment sheet: title, authors/year/venue, link, one-line relevance note.
**Verify each entry yourself (title, authors, year, that the link resolves to the
same paper) before committing — do not paste this list unverified.**

### Survey and Foundational Papers

- **Multilingual Large Language Models: A Systematic Survey**
  Zhu, Supryadi, Xu, Sun, Pan, Cui, Du, Jin, Branco, Xiong. 2024. arXiv:2411.11072.
  [Paper](https://arxiv.org/abs/2411.11072)
  Broad survey of MLLM architecture, training, and alignment — good starting map of the field.

- **A Survey on Large Language Models with Multilingualism: Recent Advances and New Frontiers**
  Huang, Mo, Li, Li, Zhang, Yi, Mao, Liu, Xu, Xu, et al. 2024. arXiv:2405.10936.
  [Paper](https://arxiv.org/abs/2405.10936)
  Complements the Zhu et al. survey with a taxonomy of multilingual training strategies.

- **A Survey on Multilingual Large Language Models: Corpora, Alignment, and Bias**
  Xu, Hu, Zhao, Qiu, Ye, Gu. 2024. arXiv:2404.00929.
  [Paper](https://arxiv.org/abs/2404.00929)
  Focuses specifically on training-corpus imbalance and cross-lingual representation alignment — directly relevant to why low-resource science underperforms.

- **Multilingual Large Language Model: A Survey of Resources, Taxonomy and Frontiers**
  Qin, Chen, Zhou, Chen, Li, Liao, Li, Che, Yu. 2024. arXiv:2404.04925.
  [Paper](https://arxiv.org/abs/2404.04925)
  Useful for its open-source resource and leaderboard pointers when hunting for tools.

- **Responsible Multilingual Large Language Models: A Survey of Development, Applications, and Societal Impact**
  Liu, Fu. 2024. arXiv:2410.17532.
  [Paper](https://arxiv.org/abs/2410.17532)
  Practical/production lens — useful for the "societal impact" angle of unreliable low-resource science.

### Benchmarks and Evaluation

- **MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation**
  Xuan, Yang, Qi, Zeng, Xiao, et al. 2025. arXiv:2503.10497.
  [Paper](https://arxiv.org/abs/2503.10497)
  Quantifies the high-resource vs low-resource reasoning gap (up to ~24% drop) across 29 languages — a core citation for this topic.

- **MM-Eval: A Multilingual Meta-Evaluation Benchmark for LLM-as-a-Judge and Reward Models**
  Son, Yoon, Suk, Aula-Blasco, Aslan, et al. 2024. arXiv:2410.17578.
  [Paper](https://arxiv.org/abs/2410.17578)
  Shows LLM-judges are themselves unreliable at scoring non-English output — critical for anyone using LLM-as-judge to evaluate multilingual science synthesis.

- **MIRAGE-Bench: Automatic Multilingual Benchmark Arena for Retrieval-Augmented Generation Systems**
  Thakur, Kazi, Luo, Lin, Ahmad. 2024. arXiv:2410.13716. (NAACL 2025)
  [Paper](https://arxiv.org/abs/2410.13716) · [Code](https://github.com/vectara/mirage-bench)
  Arena-style benchmark across 18 languages for multilingual RAG generation quality; verified as a real, code-released benchmark.

- **MEMERAG: A Multilingual End-to-End Meta-Evaluation Benchmark for Retrieval Augmented Generation**
  Cruz Blandón, Talur, Charron, Liu, Mansour, Federico. 2025. arXiv:2502.17163. (ACL 2025)
  [Paper](https://arxiv.org/abs/2502.17163) · [Code](https://github.com/amazon-science/MEMERAG)
  Human-annotated faithfulness/relevance benchmark across 5 languages built on MIRACL — good for measuring evaluator reliability itself.

- **Uhura: A Benchmark for Evaluating Scientific Question Answering and Truthfulness in Low-Resource African Languages**
  (Adelani et al. et al., research group). 2024. arXiv:2412.00948.
  [Paper](https://arxiv.org/abs/2412.00948)
  Directly scientific-domain QA/truthfulness benchmark for six low-resource African languages — strong applied example for the "science in low-resource languages" angle.

### Cross-Lingual RAG and Retrieval

- **Multilingual Retrieval Augmented Generation for Culturally-Sensitive Tasks: A Benchmark for Cross-lingual Robustness (BordIRLines)**
  Li, Luo, Haider, Agashe, Li, Liu, Miao, Ramakrishnan, Yuan, Callison-Burch. 2024. arXiv:2410.01171.
  [Paper](https://arxiv.org/abs/2410.01171)
  49-language RAG robustness benchmark; shows multilingual document retrieval can *improve* consistency over in-language-only retrieval.

- **XRAG: Cross-lingual Retrieval-Augmented Generation**
  Liu, Trenous, Ribeiro, Byrne, Hieber. 2025. arXiv:2505.10089.
  [Paper](https://arxiv.org/abs/2505.10089)
  Benchmark specifically for the case where query language ≠ retrieved-document language — the exact scenario described in your paper's Section 3.2.

- **MIRACL: A Multilingual Retrieval Dataset Covering 18 Diverse Languages**
  Zhang, Thakur, Ogundepo, Kamalloo, Alfonso-Hermelo, Li, Liu, Rezagholizadeh, Lin. 2023. TACL, vol. 11.
  [Paper](https://aclanthology.org/2023.tacl-1.63/) · [Code](https://github.com/project-miracl/miracl)
  Foundational retrieval dataset (18 languages, 726k judgments) underlying MIRAGE-Bench and MEMERAG above — worth including as the shared data backbone.

### Citation and Hallucination Integrity

- **LLM hallucinations in the wild: Large-scale evidence from non-existent citations**
  (Multiple authors). 2026. arXiv:2605.07723.
  [Paper](https://arxiv.org/abs/2605.07723)
  Audits 111 million references across arXiv, bioRxiv, SSRN, and PubMed Central; finds a sharp rise in hallucinated citations — large-scale empirical backbone for the citation-integrity argument.

- **CiteCheck: Retrieval-Grounded Detection of LLM Citation Hallucinations in Scientific Text**
  (Multiple authors). 2026. arXiv:2605.27700.
  [Paper](https://arxiv.org/html/2605.27700v1)
  Proposes a retrieval-grounded verifier for catching fabricated/corrupted citations — directly relevant as a *tool*, not just a finding (see Tools section too).

- **Finetuning with Scientific Data Increases Hallucinations: A Multi-domain Factuality Evaluation of LLMs**
  (Multiple authors). 2026. arXiv:2606.21359.
  [Paper](https://arxiv.org/abs/2606.21359)
  Counterintuitive finding: scientific-domain finetuning can *increase* attribution hallucination — important caveat for anyone building a domain-tuned multilingual science assistant.

- **Influence of Topic Familiarity and Prompt Specificity on Citation Fabrication in Mental Health Research Using Large Language Models**
  (Multiple authors). Experimental study, PMC.
  [Paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12658395/)
  Domain case study quantifying citation-fabrication rates (GPT-3.5 vs GPT-4) with topic-familiarity as a variable — useful applied companion to the large-scale audits above.

### Tokenization Fairness

- **Language Model Tokenizers Introduce Unfairness Between Languages**
  Petrov, La Malfa, Torr, Bibi. 2023. arXiv:2305.15425.
  [Paper](https://arxiv.org/abs/2305.15425)
  The foundational tokenization-fairness paper (up to 15x length disparities across scripts) — explains a root cause of low-resource-language cost and performance gaps.

- **Equity with Efficiency: An Empirical Study of Tokenizers for Multilingual Large Language Models**
  (Multiple authors). 2026. arXiv:2606.15044.
  [Paper](https://arxiv.org/abs/2606.15044)
  Recent follow-up quantifying the same effect on modern byte-level BPE tokenizers used in current LLMs.

### Domain / Terminology Alignment

- **Learning Domain-Specialised Representations for Cross-Lingual Biomedical Entity Linking (XL-BEL)**
  Liu, Cheng, Barahona, Zhang, Ren, Ye, Korhonen, Collier. 2021. ACL 2021 (short papers).
  [Paper](https://aclanthology.org/2021.acl-short.72/)
  Establishes the XL-BEL benchmark for linking biomedical mentions across 10 typologically diverse languages to a shared knowledge base — concrete example of the "entity drift" problem your paper describes for scientific taxonomies.

- **XMEN: A Modular Toolkit for Cross-Lingual Medical Entity Normalization**
  (Multiple authors). 2023. arXiv:2310.11275.
  [Paper](https://arxiv.org/abs/2310.11275)
  A practical toolkit (also usable as a Tool/Implementation entry) for mapping non-English medical terms to UMLS/SNOMED CT concepts.

---

## ═══════════════════ FILE: datasets/datasets.md ═══════════════════

# Datasets

- **MIRACL** — Multilingual Information Retrieval Across a Continuum of Languages.
  Source: Zhang et al., 2023 (TACL) / [HuggingFace](https://huggingface.co/datasets/miracl/miracl) / [GitHub](https://github.com/project-miracl/miracl)
  Description: 18-language ad hoc retrieval dataset over Wikipedia with 726k human relevance judgments.
  Use: Backbone dataset for MIRAGE-Bench and MEMERAG; use it to build or evaluate a cross-lingual retriever for scientific documents.

- **NoMIRACL** — Multilingual hallucination/robustness evaluation dataset.
  Source: project-miracl team / [GitHub](https://github.com/project-miracl/nomiracl) / [HuggingFace](https://huggingface.co/datasets/miracl/nomiracl)
  Description: 18-language dataset for testing whether an LLM hallucinates an answer when retrieved passages contain no answer.
  Use: Directly measures the "hallucination under retrieval failure" reliability dimension this repo focuses on.

- **MMLU-ProX** — Multilingual multi-subject reasoning benchmark.
  Source: Xuan et al., 2025 / [Paper](https://arxiv.org/abs/2503.10497)
  Description: Parallel scientific/academic multiple-choice questions across 29 languages.
  Use: Quantitative baseline for how much reasoning accuracy drops from English to low-resource languages on science-adjacent questions.

## ═══════════════════ FILE: tools/tools.md ═══════════════════

# Tools and Libraries

- **Pyserini** — [github.com/castorini/pyserini](https://github.com/castorini/pyserini) — Python toolkit for reproducible sparse and dense retrieval (BM25, mDPR); official baseline tool for MIRACL.
- **CiteCheck** — [arxiv.org/html/2605.27700v1](https://arxiv.org/html/2605.27700v1) — Retrieval-grounded LLM citation verifier; relevant as a practical way to implement your own citation-integrity audit step.
- **XMEN** — [github.com/hpi-dhc/xmen](https://arxiv.org/abs/2310.11275) *(see paper for repository link)* — Modular toolkit for cross-lingual medical entity normalization against UMLS/SNOMED CT.
- **Habanero / CrossRef REST API client** — [github.com/sckott/habanero](https://github.com/sckott/habanero) — Python client for the CrossRef API; use it to programmatically verify DOIs and metadata for your paper collection (the same verification step this assignment requires).
- **Hugging Face `evaluate` + `sentence-transformers`** — [github.com/huggingface/evaluate](https://github.com/huggingface/evaluate) / [github.com/UKPLab/sentence-transformers](https://github.com/UKPLab/sentence-transformers) — Standard libraries for multilingual embedding models (e.g. LaBSE) and evaluation metrics used across most papers above.

## ═══════════════════ FILE: implementations/github-repositories.md ═══════════════════

# GitHub Implementations

- **project-miracl/miracl** — [github.com/project-miracl/miracl](https://github.com/project-miracl/miracl) — Official MIRACL dataset + BM25/mDPR baselines. Implements the retrieval benchmark referenced throughout this collection.
- **project-miracl/nomiracl** — [github.com/project-miracl/nomiracl](https://github.com/project-miracl/nomiracl) — Reference implementation for the hallucination-under-retrieval-failure evaluation described above, with ready-to-use data loaders.
- **vectara/mirage-bench** — [github.com/vectara/mirage-bench](https://github.com/vectara/mirage-bench) — Official code for MIRAGE-Bench (NAACL 2025); implements the surrogate-judge arena evaluation method.
- **amazon-science/MEMERAG** — [github.com/amazon-science/MEMERAG](https://github.com/amazon-science/MEMERAG) — Official MEMERAG dataset and evaluation code (ACL 2025) for meta-evaluating multilingual RAG judges.
- **castorini/pyserini** — [github.com/castorini/pyserini](https://github.com/castorini/pyserini) — Widely-used, actively maintained reproducible IR toolkit; the reference implementation for most MIRACL-based baselines cited above.

## ═══════════════════ FILE: tutorials (fold into README or a tutorials.md) ═══════════════════

# Tutorials and Learning Resources

- **Hugging Face NLP Course** — [huggingface.co/learn/nlp-course](https://huggingface.co/learn/nlp-course) — Free course covering transformers, tokenization, and multilingual models; start here if tokenization/embeddings are new to you.
- **MIRACL project documentation** — [github.com/project-miracl/miracl#readme](https://github.com/project-miracl/miracl) — Walks through downloading the dataset and reproducing BM25/mDPR baselines with Pyserini.
- **Pyserini documentation** — [github.com/castorini/pyserini/blob/master/docs/](https://github.com/castorini/pyserini) — Hands-on guides for sparse and dense multilingual retrieval.
- **CrossRef REST API documentation** — [api.crossref.org](https://api.crossref.org) — How to programmatically verify a citation's title, authors, and DOI — directly useful for your own citation-integrity audit.
- **ACL Anthology** — [aclanthology.org](https://aclanthology.org) — Authoritative, freely accessible archive of NLP papers (including several cited above); use it to verify venue/publication details for any ACL/EMNLP/NAACL paper you cite.
