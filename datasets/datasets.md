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
