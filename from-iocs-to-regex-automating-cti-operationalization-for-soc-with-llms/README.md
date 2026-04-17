# From IOCs to Regex: Automating CTI Operationalization for SOC with LLMs

- **Paper**: https://arxiv.org/abs/2604.12228
- **Authors**: Pei-Yu Tseng, Lan Zhang, ZihDwo Yeh, Xiaoyan Sun, Xushu Dai, Peng Liu
- **Primary affiliations**: Northern Arizona University; The Pennsylvania State University; Worcester Polytechnic Institute
- **Publication / source**: arXiv:2604.12228v1 (cs.CR), 2026-04-14
- **Implementation status**: Minimal runnable prototype

## Summary
Presents IOCRegex-gen, an automated LLM pipeline turning CTI IOCs into validated regex patterns with high hit-rate and low false positives.

## Why it matters
Bridges research and SOC operations by reducing manual IOC-to-rule engineering bottlenecks in SIEM and detection workflows.

## Key ideas
- Detect IOC type and generate type-specific regex templates (domain, IPv4, hash, URL, etc.).
- Apply multi-stage validation for syntax and semantic matching behavior.
- Use iterative correction loop to reduce false positives while preserving recall.

## Method details in this repository
- `impl/ioc_regex_gen_demo.py` demonstrates one central mechanism from the paper in an executable, inspectable form.
- The goal is conceptual reproducibility of the method idea, not full benchmark replication.

## Reproducibility notes
- This repo includes a deterministic IOC-to-regex mini-pipeline with positive/negative test harness.
- Implements basic type inference and evaluates hit-rate + false-positive rate.
- Run: `python3 impl/ioc_regex_gen_demo.py`.

## Quick run
```bash
python3 impl/ioc_regex_gen_demo.py
```

## References
- Paper: https://arxiv.org/abs/2604.12228
- PDF: https://arxiv.org/pdf/2604.12228.pdf
