import json

from src.tip_distillation import run_comparison

if __name__ == "__main__":
    out = run_comparison(seed=7)
    print(json.dumps(out, indent=2))
