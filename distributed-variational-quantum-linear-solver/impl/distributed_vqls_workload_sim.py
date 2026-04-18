#!/usr/bin/env python3
"""
D-VQLS workload simulator:
- LCU term growth model
- Thresholding compression model
- Multi-worker task distribution and speedup estimate
"""

from dataclasses import dataclass


@dataclass
class VQLSConfig:
    n_qubits: int = 10
    lcu_terms_raw: int = 4 ** 10
    threshold_keep_ratio: float = 0.0039
    workers: int = 96
    circuit_time_ms: float = 0.08
    scheduler_overhead: float = 0.12


def compressed_terms(cfg: VQLSConfig) -> int:
    return max(1, int(cfg.lcu_terms_raw * cfg.threshold_keep_ratio))


def circuits_per_iter(l_terms: int) -> int:
    return l_terms * l_terms


def iteration_time_s(circuits: int, cfg: VQLSConfig) -> float:
    ideal = circuits * (cfg.circuit_time_ms / 1000) / cfg.workers
    return ideal * (1 + cfg.scheduler_overhead)


def run():
    cfg = VQLSConfig()
    raw_terms = cfg.lcu_terms_raw
    cmp_terms = compressed_terms(cfg)

    raw_c = circuits_per_iter(raw_terms)
    cmp_c = circuits_per_iter(cmp_terms)

    t_raw = iteration_time_s(raw_c, cfg)
    t_cmp = iteration_time_s(cmp_c, cfg)

    print("=== Distributed VQLS Workload Simulation ===")
    print(f"Qubits: {cfg.n_qubits}")
    print(f"Raw LCU terms: {raw_terms:,}")
    print(f"Compressed LCU terms: {cmp_terms:,}")
    print(f"Raw circuits/iter: {raw_c:,}")
    print(f"Compressed circuits/iter: {cmp_c:,}")
    print(f"Circuit count reduction: {raw_c / cmp_c:,.1f}x")
    print(f"Iteration time @ {cfg.workers} workers (raw): {t_raw:,.1f}s")
    print(f"Iteration time @ {cfg.workers} workers (compressed): {t_cmp:,.2f}s")
    print(f"Estimated speedup: {t_raw / t_cmp:,.1f}x")


if __name__ == "__main__":
    run()
