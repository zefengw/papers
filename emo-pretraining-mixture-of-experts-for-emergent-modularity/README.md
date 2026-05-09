# EMO: Pretraining Mixture of Experts for Emergent Modularity

## Why it matters
EMO solves the massive performance degradation seen when restricting standard Mixture-of-Experts (MoE) models to a subset of experts in memory-constrained deployments, making modular LLM deployment practical.

## Core Setup
This directory contains an experiment template/scaffold for emergent modularity in MoE structures, matching the conceptual constraints described in the paper. We simulate a token-affinity penalty mechanism within a small PyTorch model that encourages tokens from a single "document" to select experts from a restricted sub-pool.

## Why Full Implementation is Not Applicable
Replicating the full EMO architecture requires massive pretraining scales (1T tokens minimally to observe the true "emergence" of semantic specialization) and highly optimized distributed MoE frameworks. A local full implementation is computationally out of scope. Therefore, this folder contains a scale-down experimental scaffold mimicking the routing constraint loss.

## Usage
Run the toy script to see the loss components (standard cross entropy + document-expert affinity penalty) working together.
```
pip install torch
python emo_scaffold.py
```
