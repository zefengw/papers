# Aligning Dense Retrievers with LLM Utility via Distillation

**Authors:** Rajinder Sandhu, Di Mu, Cheng Chang, Md Shahriar Tasjid, Himanshu Rai
**Affiliation:** Unknown / High-Signal
**Link:** [http://arxiv.org/abs/2604.22722v1](http://arxiv.org/abs/2604.22722v1)

## Summary
Retrievers often retrieve topically relevant but useless documents for the LLM. This paper aligns the retriever's scoring with the LLM's final answer accuracy through a distillation process where the LLM's 'utility' signals guide the retriever's training.

## Method Details
An implementation of a custom loss function for bi-encoders that incorporates feedback from an LLM's likelihood of producing the correct answer given a document.

## Reproducibility Notes
This implementation focus on the core algorithms described in the paper.
