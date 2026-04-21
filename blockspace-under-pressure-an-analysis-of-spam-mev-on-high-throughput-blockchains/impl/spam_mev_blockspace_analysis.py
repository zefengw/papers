#!/usr/bin/env python3
"""Spam-MEV blockspace pressure simulation."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import List


@dataclass
class Tx:
    gas_used: int
    priority_fee: float
    is_spam_mev: bool


@dataclass
class Block:
    txs: List[Tx]


def generate_block(n_txs: int = 500, spam_ratio: float = 0.28) -> Block:
    txs: List[Tx] = []
    for _ in range(n_txs):
        spam = random.random() < spam_ratio
        if spam:
            txs.append(Tx(
                gas_used=random.randint(18_000, 35_000),
                priority_fee=random.uniform(2.0, 12.0),
                is_spam_mev=True,
            ))
        else:
            txs.append(Tx(
                gas_used=random.randint(20_000, 120_000),
                priority_fee=random.uniform(1.0, 6.0),
                is_spam_mev=False,
            ))
    return Block(txs)


def metrics(block: Block) -> dict:
    total_gas = sum(t.gas_used for t in block.txs)
    spam_gas = sum(t.gas_used for t in block.txs if t.is_spam_mev)
    avg_fee = sum(t.priority_fee for t in block.txs) / len(block.txs)
    normal_fees = [t.priority_fee for t in block.txs if not t.is_spam_mev]
    spam_fees = [t.priority_fee for t in block.txs if t.is_spam_mev]
    return {
        "tx_count": len(block.txs),
        "spam_share_gas": spam_gas / total_gas if total_gas else 0.0,
        "avg_priority_fee": avg_fee,
        "avg_priority_fee_normal": sum(normal_fees)/len(normal_fees) if normal_fees else 0.0,
        "avg_priority_fee_spam": sum(spam_fees)/len(spam_fees) if spam_fees else 0.0,
    }


def apply_spam_filter(block: Block, fee_threshold: float = 8.0) -> Block:
    # naive mitigation: drop suspiciously high-priority-fee short-gas spam patterns
    filtered = [
        t for t in block.txs
        if not (t.is_spam_mev and t.priority_fee >= fee_threshold and t.gas_used < 40_000)
    ]
    return Block(filtered)


def run_sim(num_blocks: int = 20) -> None:
    before = []
    after = []
    for _ in range(num_blocks):
        b = generate_block()
        before.append(metrics(b))
        after.append(metrics(apply_spam_filter(b)))

    def avg(key: str, rows: List[dict]) -> float:
        return sum(r[key] for r in rows) / len(rows)

    print("=== Aggregate over", num_blocks, "blocks ===")
    for k in ["spam_share_gas", "avg_priority_fee", "avg_priority_fee_normal"]:
        print(f"{k}: before={avg(k,before):.4f} after={avg(k,after):.4f}")


if __name__ == "__main__":
    random.seed(123)
    run_sim()
