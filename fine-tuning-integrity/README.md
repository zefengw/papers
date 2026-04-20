# Fine-Tuning Integrity for Modern Neural Networks: Structured Drift Proofs

## Summary
This paper addresses the security risk of untrusted fine-tuning, where an adversary might insert backdoors or drastically alter model behavior while claiming the update is "small." The authors propose **Fine-Tuning Integrity (FTI)**, utilizing **Succinct Model Difference Proofs (SMDPs)** to certify that the model drift (the difference between base and fine-tuned weights) conforms to a specific structure (e.g., norm-bounded, low-rank, or sparse).

## Method Details
- **SMDPs**: Cryptographic proofs that the weight delta $\Delta W$ satisfies:
    - **Norm Bound**: $||\Delta W|| \le \epsilon$ (prevents massive weight shifts).
    - **Low-Rank**: $\text{rank}(\Delta W) \le k$ (typical of LoRA).
    - **Sparsity**: $||\Delta W||_0 \le s$ (only a few parameters changed).
- **Verification**: Verifiers can check these certificates without needing to process the entire model, making the check succinct.

## Reproducibility Notes
The "proof" part uses ZKPs (e.g., polynomial commitments), but the *integrity check* part can be implemented by calculating the norm, rank, or sparsity of the weight difference.

## References
- arXiv: 2604.04738v1
