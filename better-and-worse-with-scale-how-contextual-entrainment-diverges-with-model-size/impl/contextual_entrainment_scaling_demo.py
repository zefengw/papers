#!/usr/bin/env python3
"""Toy power-law fitting for contextual entrainment trends (stdlib only)."""
import math


def fit_power_law(xs, ys):
    # Fit y = a * x^b via linear regression in log-space.
    lx = [math.log(x) for x in xs]
    ly = [math.log(y) for y in ys]
    n = len(xs)
    mx, my = sum(lx)/n, sum(ly)/n
    num = sum((lx[i]-mx)*(ly[i]-my) for i in range(n))
    den = sum((lx[i]-mx)**2 for i in range(n))
    b = num/den
    a = math.exp(my - b*mx)
    return a, b


def predict(a, b, x):
    return a * (x ** b)


def main() -> None:
    # Synthetic values chosen to mirror described trend directions.
    sizes_b = [0.41, 1.4, 2.8, 6.7, 12.0]  # billions of params
    semantic_entrainment = [0.34, 0.29, 0.25, 0.21, 0.18]      # decreases with scale
    nonsemantic_copying = [0.08, 0.10, 0.12, 0.14, 0.16]       # increases with scale

    a_sem, b_sem = fit_power_law(sizes_b, semantic_entrainment)
    a_non, b_non = fit_power_law(sizes_b, nonsemantic_copying)

    target = 20.0
    print(f'semantic trend exponent b={b_sem:.3f} (negative means improves with scale)')
    print(f'non-semantic trend exponent b={b_non:.3f} (positive means gets worse with scale)')
    print(f'pred semantic entrainment @ {target}B: {predict(a_sem,b_sem,target):.3f}')
    print(f'pred non-semantic copying @ {target}B: {predict(a_non,b_non,target):.3f}')


if __name__ == '__main__':
    main()
