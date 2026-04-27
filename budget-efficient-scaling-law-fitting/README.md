# Spend Less, Fit Better: Budget-Efficient Scaling Law Fitting via Active Experiment Selection

**Authors:** Sijie Li, Shanda Li, Haowei Lin, Weiwei Sun, Ameet Talwalkar
**Affiliation:** Carnegie Mellon University
**Link:** [http://arxiv.org/abs/2604.22753v1](http://arxiv.org/abs/2604.22753v1)

## Summary
Scaling laws are typically fitted using a grid search of model sizes and data scales, which is computationally expensive. This paper introduces an active learning framework to select the most informative experiments (model/data configurations) to fit the scaling law with a minimal budget.

## Method Details
Implement an active selection algorithm that chooses the next experiment configuration (N, D) based on the uncertainty of the current scaling law fit (e.g., using a Gaussian Process or similar surrogate).

## Reproducibility Notes
This implementation focus on the core algorithms described in the paper.
