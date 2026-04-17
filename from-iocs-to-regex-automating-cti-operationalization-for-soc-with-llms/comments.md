# Comments

## Critical notes
- Operationalizing IOCs as regex patterns is a practical, high-leverage SOC automation target.
- Validation loops are as important as generation quality; brittle regexes can silently harm detection quality.

## Limitations (in this repo demo)
- Type inference is simplistic and not robust to obfuscation.
- No staged self-correction loop with LLM reasoning yet.
- Regexes are generic templates, not context-aware to specific log schemas.

## Potential extensions
- Add schema-aware regex generation for different log sources.
- Introduce adversarial test corpus (obfuscation, homoglyphs, delimiter tricks).
- Add confidence scoring and human-in-the-loop review thresholds.
