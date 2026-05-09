# Optimizer-Model Consistency: Full Finetuning with the Same Optimizer as Pretraining Forgets Less

## Why it matters
This paper provides crucial evidence that using the identical optimizer for full supervised fine-tuning (SFT) as was used during pre-training reduces catastrophic forgetting, challenging the default industry practice of always switching to AdamW or LoRA.

## Core Setup
This directory contains a PyTorch experiment framework demonstrating the learning-forgetting tradeoff mentioned in the paper. It sets up a synthetic pre-training phase with Optimizer A, followed by branching fine-tuning phases using Optimizer A vs. Optimizer B.

## Why Full Implementation is Not Applicable
Proving the paper's claims at scale requires pre-training an LLM from scratch on large-scale clusters, which cannot be run locally as a standalone artifact. Instead, we provide an experimental harness that validates the architectural concepts of optimization state transitions.

## Usage
Run the script to observe the differing validation behaviors between consistent vs. inconsistent optimizer states across task boundaries.
```
pip install torch
python optimizer_consistency_scaffold.py
```
