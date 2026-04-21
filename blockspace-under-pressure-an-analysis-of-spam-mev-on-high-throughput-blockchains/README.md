# Blockspace Under Pressure: An Analysis of Spam MEV on High-Throughput Blockchains

- **Paper**: https://arxiv.org/abs/2604.00234
- **arXiv ID**: 2604.00234v1 (2026-03-31)
- **Authors**: Wenhao Wang, Aditya Saraf, Lioba Heimbach, Kushal Babel, Fan Zhang
- **Primary affiliations**: Yale University (IC3); Cornell University (IC3); Category Labs
- **Source**: arXiv (cs.GT)

## Summary
The paper studies spam-MEV behavior on high-throughput chains, focusing on how spam transactions consume blockspace and impact congestion/fees.

## Method details
- Analyze block-level transaction composition.
- Quantify spam share and its relation to fee pressure.
- Characterize MEV-related transaction patterns.

## Implementation in this folder
`impl/spam_mev_blockspace_analysis.py` provides:
- A synthetic block generator with normal vs spam-MEV flows.
- Blockspace pressure metrics (spam share, effective fee inflation, throughput waste).
- A simple mitigation simulation (spam filter threshold) and before/after comparison.

## Reproducibility notes
- Python 3.10+
- No additional dependencies.

```bash
python impl/spam_mev_blockspace_analysis.py
```

## References
- Wang et al., *Blockspace Under Pressure*, arXiv:2604.00234, 2026.
