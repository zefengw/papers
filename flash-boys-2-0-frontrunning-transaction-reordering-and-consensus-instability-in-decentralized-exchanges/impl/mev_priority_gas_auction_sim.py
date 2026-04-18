#!/usr/bin/env python3
"""Toy simulation of MEV extraction under priority gas auctions (PGA)."""

import random
from statistics import mean


def simulate_round(opportunity_value, bot_count=3, gas_unit_cost=0.002):
    bids = [random.uniform(20, 180) for _ in range(bot_count)]
    winner_bid = max(bids)

    extracted_value = opportunity_value
    gas_cost = winner_bid * gas_unit_cost
    winner_profit = max(0.0, extracted_value - gas_cost)
    total_gas_paid = sum(b * gas_unit_cost for b in bids)
    return winner_profit, extracted_value, total_gas_paid


def run_sim(rounds=200, pga=True):
    profits, extracted, fees = [], [], []
    for _ in range(rounds):
        opp = random.uniform(0.05, 0.60)
        if pga:
            p, e, f = simulate_round(opp, bot_count=3)
        else:
            p, e, f = simulate_round(opp, bot_count=1)
            f *= 0.25
        profits.append(p)
        extracted.append(e)
        fees.append(f)

    return {
        "avg_profit": mean(profits),
        "avg_extracted_value": mean(extracted),
        "avg_fees_paid": mean(fees),
        "net_after_fees": mean(profits) - mean(fees),
    }


def main():
    random.seed(7)
    baseline = run_sim(pga=False)
    pga = run_sim(pga=True)

    print("=== MEV ordering simulation (toy) ===")
    print("Baseline (no aggressive PGA):")
    for k, v in baseline.items():
        print(f"  {k}: {v:.4f}")

    print("\nPriority Gas Auction regime:")
    for k, v in pga.items():
        print(f"  {k}: {v:.4f}")

    print("\nDelta (PGA - baseline):")
    for key in baseline:
        print(f"  {key}: {pga[key] - baseline[key]:.4f}")


if __name__ == "__main__":
    main()
