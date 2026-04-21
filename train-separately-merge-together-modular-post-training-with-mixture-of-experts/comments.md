# Comments: Train Separately, Merge Together (BAR)

## Critical notes
- The paper's central value is **modularity under post-training**, not just MoE architecture itself.
- Real gains depend on high-quality per-domain expert data and careful router calibration.
- Routing failures can silently degrade output quality if confidence signals are weak.

## Limitations
- The toy implementation does not include full mid-training/SFT/RL pipelines.
- No real token-level MoE gating or distributed training cost accounting.
- Safety compositionality remains under-specified in open reproductions.

## Extension ideas
1. Add uncertainty-aware abstention before expert dispatch.
2. Add online router adaptation from user feedback.
3. Benchmark cost vs. quality for adding one new expert vs full retraining.
