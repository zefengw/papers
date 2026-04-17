# Comments

## Critical notes
- Open-system formalism cleanly captures interference + decay + cascades that are awkward in pure-state-only treatments.
- The Lindblad/Kraus equivalence discussion is computationally valuable for choosing numerically efficient implementations.

## Limitations (in this repo demo)
- Very simplified two-state closed-form approximation.
- Does not include full density-matrix evolution, multiple channels, or realistic detector effects.
- Parameters are illustrative, not fit to experimental data.

## Potential extensions
- Implement full matrix-based Lindblad solver for multi-flavor systems.
- Add synthetic event-rate prediction and parameter sweeps.
- Compare ODE-based and superoperator-based runtime/accuracy.
