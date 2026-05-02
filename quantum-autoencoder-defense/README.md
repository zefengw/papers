# Defending Quantum Classifiers through Quantum Autoencoders

## Summary
The paper addresses the vulnerability of Variational Quantum Classifiers (VQC) to adversarial noise. It proposes using a Quantum Autoencoder (QAE) to "purify" input quantum states before classification.

## Methodology
- **QAE Purification**: Mapping high-dimensional noisy quantum states to a lower-dimensional latent space (discarding noise) and reconstructing a cleaner state.
- **Confidence Metric**: Uses the fidelity of the reconstruction as a metric to identify samples that are too noisy to be trusted.
- **Results**: Achieved up to 68% improvement in accuracy under standard adversarial attacks.

## References
- arXiv: 2604.28176
- Affiliations: University of Florida, Pennsylvania State University.
