# Visible Neutrino Decay As An Open Quantum System

- **Paper**: https://arxiv.org/abs/2604.09776
- **Authors**: Joachim Kopp, George A. Parker
- **Primary affiliations**: JGU Mainz (Johannes Gutenberg University Mainz)
- **Publication / source**: arXiv:2604.09776v1 (hep-ph), 2026-04-10
- **Implementation status**: Minimal runnable prototype

## Summary
Develops a general open-quantum-system treatment for oscillating/decaying neutrinos using Lindblad, Liouvillian, and Kraus formalisms.

## Why it matters
Provides a clean computational framework for quantum systems with both coherence and decay channels, useful beyond neutrino phenomenology.

## Key ideas
- Represent neutrino system as density matrix evolving under coherent Hamiltonian + dissipative terms.
- Express dynamics with Lindblad master equation and equivalent superoperator/Kraus views.
- Handle multi-step cascades and interference effects in a unified formalism.

## Method details in this repository
- `impl/open_quantum_neutrino_decay_demo.py` demonstrates one central mechanism from the paper in an executable, inspectable form.
- The goal is conceptual reproducibility of the method idea, not full benchmark replication.

## Reproducibility notes
- This repo includes a tiny two-state oscillation+decay simulator with closed-form damping terms.
- Script outputs survival probability over time to illustrate decoherence/decay behavior.
- Run: `python3 impl/open_quantum_neutrino_decay_demo.py`.

## Quick run
```bash
python3 impl/open_quantum_neutrino_decay_demo.py
```

## References
- Paper: https://arxiv.org/abs/2604.09776
- PDF: https://arxiv.org/pdf/2604.09776.pdf
