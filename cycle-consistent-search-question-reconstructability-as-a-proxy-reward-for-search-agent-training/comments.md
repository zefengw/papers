# Comments

## Critical notes
- Reconstructability is a practical proxy: it captures informational sufficiency without requiring labeled final answers.
- Bottlenecks are essential; otherwise agents can game rewards by parroting lexical cues.

## Limitations (in this repo demo)
- Uses simplistic overlap-based reconstruction, not learned question reconstruction.
- Leakage detection is heuristic and can miss subtle shortcuts.
- No policy optimization loop (reward diagnostics only).

## Potential extensions
- Add trainable reconstructor model and compare to heuristic overlap reward.
- Evaluate reward robustness against synthetic adversarial trajectories.
- Integrate into PPO/GRPO-style training for an actual search policy.
