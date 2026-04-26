# MEV-ACE: Identity-Authenticated Fair Ordering

## Summary
MEV-ACE addresses the structural threat of Maximal Extractable Value (MEV) to blockchain fairness. It proposes an identity-authenticated ordering mechanism where proposers are constrained by a verifiable fair-ordering protocol that leverages cryptographic identities to prevent front-running and discriminatory transaction sequencing.

## Key Methods
- **Identity Authentication**: Transactions are bound to cryptographic identities that limit the ability of proposers to inject their own transactions ahead of others.
- **Fair Ordering Rules**: Enforcing First-Come-First-Serve (FCFS) or commit-reveal schemes to ensure the proposer cannot see transaction content before ordering.
- **Proposer Mitigation**: Reducing the incentive for centralized builder markets by embedding fairness at the consensus/proposer level.

## References
Jian Sheng Wang. "MEV-ACE: Identity-Authenticated Fair Ordering for Proposer-Controlled MEV Mitigation". arXiv:2604.07568, 2026.
