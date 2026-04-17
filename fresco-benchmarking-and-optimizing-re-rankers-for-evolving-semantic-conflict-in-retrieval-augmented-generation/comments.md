# Comments

## Critical notes
- The benchmark targets a real RAG blind spot: temporal drift plus semantic conflict.
- The reported gains suggest reranker instructions/objectives can be tuned to reduce stale-evidence bias.

## Limitations (in this repo demo)
- Uses hand-crafted semantic and temporal scores; no learned reranker.
- Omits uncertainty and source reliability dimensions.
- No full benchmark loader/evaluation scripts yet.

## Potential extensions
- Add a calibration head predicting factual staleness risk.
- Incorporate source credibility and contradiction checks.
- Evaluate on real revision histories with automatic temporal labeling.
