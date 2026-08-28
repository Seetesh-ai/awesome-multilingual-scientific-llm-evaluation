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
