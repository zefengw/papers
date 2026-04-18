#!/usr/bin/env python3
"""
Toy surface-code pre-decoder pipeline:
1) Inject random syndrome defects on a 2D grid
2) Local pre-decoder removes easy nearest-neighbor pairs
3) Global decoder handles residual defects

Goal: illustrate how local pre-decoding lowers global workload.
"""

from random import Random


def make_syndrome(n=9, defect_p=0.12, seed=42):
    rng = Random(seed)
    grid = [[1 if rng.random() < defect_p else 0 for _ in range(n)] for _ in range(n)]
    return grid


def count_defects(grid):
    return sum(sum(row) for row in grid)


def local_pair_cancel(grid):
    n = len(grid)
    cancelled = 0
    # horizontal pairing
    for i in range(n):
        j = 0
        while j < n - 1:
            if grid[i][j] == 1 and grid[i][j + 1] == 1:
                grid[i][j] = 0
                grid[i][j + 1] = 0
                cancelled += 2
                j += 2
            else:
                j += 1
    # vertical pairing
    for j in range(n):
        i = 0
        while i < n - 1:
            if grid[i][j] == 1 and grid[i + 1][j] == 1:
                grid[i][j] = 0
                grid[i + 1][j] = 0
                cancelled += 2
                i += 2
            else:
                i += 1
    return cancelled


def global_decoder_cost(residual_defects):
    # Proxy: matching decoders become superlinear with unresolved defects.
    return residual_defects ** 1.35


def demo(n=17, defect_p=0.1):
    syn = make_syndrome(n=n, defect_p=defect_p)
    initial = count_defects(syn)
    cancelled = local_pair_cancel(syn)
    residual = count_defects(syn)

    cost_before = global_decoder_cost(initial)
    cost_after = global_decoder_cost(residual)

    print("=== Surface-Code Pre-Decoder Demo ===")
    print(f"Grid size: {n}x{n}")
    print(f"Initial defects: {initial}")
    print(f"Locally cancelled: {cancelled}")
    print(f"Residual defects: {residual}")
    print(f"Global decoder proxy cost (before): {cost_before:.2f}")
    print(f"Global decoder proxy cost (after):  {cost_after:.2f}")
    if cost_after > 0:
        print(f"Estimated global workload reduction: {(1 - cost_after/cost_before)*100:.1f}%")


if __name__ == "__main__":
    demo()
