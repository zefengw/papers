#!/usr/bin/env python3
"""Toy cycle-consistent reward demo for search trajectories."""
import re

STOP = {'the','a','an','of','to','in','for','and','is','on','with','by','what','which'}


def normalize(text: str) -> set[str]:
    tokens = re.findall(r"[A-Za-z0-9]+", text.lower())
    return {t for t in tokens if t not in STOP}


def mask_named_entities(text: str) -> str:
    # Very naive proxy: mask TitleCase words.
    return re.sub(r"[A-Z][a-zA-Z0-9]+", "<NE>", text)


def reconstructability(question: str, trajectory_text: str) -> float:
    q = normalize(mask_named_entities(question))
    t = normalize(mask_named_entities(trajectory_text))
    if not q:
        return 0.0
    return len(q & t) / len(q)


def leakage_penalty(question: str, trajectory_text: str) -> float:
    # Penalize exact unmasked overlap of long tokens (proxy for lexical leakage).
    q_tokens = {w for w in re.findall(r"[A-Za-z0-9]+", question) if len(w) >= 6}
    t_tokens = set(re.findall(r"[A-Za-z0-9]+", trajectory_text))
    return min(1.0, len(q_tokens & t_tokens) / max(1, len(q_tokens)))


def ccs_reward(question: str, trajectory_text: str) -> float:
    rec = reconstructability(question, trajectory_text)
    leak = leakage_penalty(question, trajectory_text)
    return rec - 0.35 * leak


def main() -> None:
    question = "Which city hosts the headquarters of the company that created PyTorch?"

    good_traj = ""
    good_traj += "PyTorch was originally developed by Facebook AI Research. "
    good_traj += "Facebook's parent company Meta has headquarters in Menlo Park."

    bad_traj = ""
    bad_traj += "PyTorch company created pytorch pytorch. headquarters headquarters. "
    bad_traj += "irrelevant chatter without factual chain."

    for name, traj in [("good", good_traj), ("bad", bad_traj)]:
        rec = reconstructability(question, traj)
        leak = leakage_penalty(question, traj)
        reward = ccs_reward(question, traj)
        print(f"{name}: reconstructability={rec:.3f} leakage={leak:.3f} reward={reward:.3f}")


if __name__ == '__main__':
    main()
