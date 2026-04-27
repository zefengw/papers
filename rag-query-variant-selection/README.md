# Can QPP Choose the Right Query Variant? Evaluating Query Variant Selection for RAG Pipelines

**Authors:** Negar Arabzadeh, Andrew Drozdov, Michael Bendersky, Matei Zaharia
**Affiliation:** Stanford / Google / Databricks
**Link:** [http://arxiv.org/abs/2604.22661v1](http://arxiv.org/abs/2604.22661v1)

## Summary
Query Performance Prediction (QPP) techniques are evaluated for selecting the best query variant among several reformulations in a RAG pipeline. The paper shows that choosing the right variant significantly improves retrieval quality.

## Method Details
Implementation of a QPP-based selector that scores multiple query reformulations using a scoring function (e.g., clarity, specificity) and routes the highest-scoring one to the vector database.

## Reproducibility Notes
This implementation focus on the core algorithms described in the paper.
