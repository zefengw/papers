"""Impermanent loss framework for weighted geometric-mean AMMs (G3M).

Model:
    invariant k = x^w * y^(1-w), with 0 < w < 1
where x and y are reserves of token X and Y, and external price p is in Y per X.

The code provides closed-form reserve updates and IL calculations under arbitrage
to new market prices, plus consistency checks against the constant-product formula.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Tuple
import math


@dataclass(frozen=True)
class WeightedG3M:
    """Weighted geometric mean market maker.

    We initialize at p0=1 by default with equilibrium reserves:
        x0 = w
        y0 = 1 - w
    so initial total value is normalized to 1 in Y units.
    """

    weight_x: float
    p0: float = 1.0

    def __post_init__(self) -> None:
        if not (0.0 < self.weight_x < 1.0):
            raise ValueError("weight_x must be in (0,1)")
        if self.p0 <= 0:
            raise ValueError("p0 must be positive")

    @property
    def w(self) -> float:
        return self.weight_x

    @property
    def x0(self) -> float:
        # Equilibrium reserve normalization.
        return self.w

    @property
    def y0(self) -> float:
        return (1.0 - self.w) * self.p0

    def reserves_after_price_ratio(self, r: float) -> Tuple[float, float]:
        """Arbitrage-adjusted reserves after price move r = p_t / p0.

        Derived by combining:
        - invariant preservation
        - new marginal price condition
        """
        if r <= 0:
            raise ValueError("price ratio must be positive")

        x_t = self.x0 * (r ** (-(1.0 - self.w)))
        y_t = self.y0 * (r ** self.w)
        return x_t, y_t

    def lp_value(self, r: float) -> float:
        """LP portfolio value in Y units after move ratio r."""
        x_t, y_t = self.reserves_after_price_ratio(r)
        p_t = self.p0 * r
        return p_t * x_t + y_t

    def hodl_value(self, r: float) -> float:
        """Passive hold benchmark value in Y units."""
        p_t = self.p0 * r
        return p_t * self.x0 + self.y0

    def impermanent_loss(self, r: float) -> float:
        """Impermanent loss = LP / HODL - 1 (typically <= 0)."""
        return self.lp_value(r) / self.hodl_value(r) - 1.0

    def closed_form_il(self, r: float) -> float:
        """Closed-form IL for weighted G3M from derived expression."""
        return (r ** self.w) / (self.w * r + (1.0 - self.w)) - 1.0


def constant_product_il(r: float) -> float:
    """Classic IL formula for x*y=k pools (w=0.5)."""
    return (2.0 * math.sqrt(r) / (1.0 + r)) - 1.0


def scenario_sweep(weights: Iterable[float], price_ratios: Iterable[float]) -> List[Tuple[float, float, float]]:
    rows = []
    for w in weights:
        pool = WeightedG3M(weight_x=w)
        for r in price_ratios:
            rows.append((w, r, pool.impermanent_loss(r)))
    return rows


def run_demo() -> str:
    # A compact scenario grid for analysts.
    weights = [0.3, 0.5, 0.7]
    ratios = [0.5, 0.8, 1.0, 1.2, 2.0]

    lines = []
    lines.append("Impermanent Loss Sweep (value in %):")
    lines.append("weight_x | price_ratio | IL%")
    lines.append("---------|-------------|---------")

    for w, r, il in scenario_sweep(weights, ratios):
        lines.append(f"{w:8.2f} | {r:11.2f} | {il*100:7.3f}")

    # Validate weighted formula vs standard constant-product result.
    cp_pool = WeightedG3M(weight_x=0.5)
    max_err = 0.0
    for r in ratios:
        err = abs(cp_pool.impermanent_loss(r) - constant_product_il(r))
        max_err = max(max_err, err)

    lines.append("")
    lines.append(f"Constant-product formula max error: {max_err:.12f}")
    return "\n".join(lines)


if __name__ == "__main__":
    print(run_demo())
