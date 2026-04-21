# Comments: MathNet

## Critical notes
- Strong benchmark contribution: multilingual + retrieval + reasoning in one framework.
- Practical implication: retrieval quality is often the limiting factor for downstream solver gains.

## Limitations
- Public reproductions may understate true gains without high-quality retrieval infrastructure.
- Multimodal evaluation remains sensitive to OCR/diagram parsing quality.

## Extension ideas
1. Add hybrid retrieval (sparse + dense + symbolic indexing).
2. Add difficulty-aware curriculum for RAG fine-tuning.
3. Build adversarial split to stress near-miss but non-equivalent problems.
