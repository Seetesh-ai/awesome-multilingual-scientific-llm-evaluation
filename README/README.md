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
