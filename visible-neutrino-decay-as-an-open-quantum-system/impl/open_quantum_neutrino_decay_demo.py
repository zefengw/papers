#!/usr/bin/env python3
"""Toy two-level oscillation + decay dynamics (open-quantum-system flavor)."""
import math


def survival_probability(t, theta=0.58, delta_m2=2.4e-3, E=1.0, gamma=0.08):
    # Simplified damped two-flavor oscillation in naturalized units.
    phase = 1.267 * delta_m2 * t / E
    osc = 1.0 - (math.sin(2*theta) ** 2) * (math.sin(phase) ** 2)
    decay = math.exp(-gamma * t)
    return osc * decay


def main() -> None:
    print('t	P_survival')
    for t in [0, 5, 10, 20, 40, 60, 80, 100]:
        print(f'{t}	{survival_probability(t):.4f}')


if __name__ == '__main__':
    main()
