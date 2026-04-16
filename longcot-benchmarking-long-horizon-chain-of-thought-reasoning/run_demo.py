import json

from src.longcot_benchmark import run_benchmark

if __name__ == "__main__":
    out = run_benchmark(seed=42)
    print(json.dumps(out, indent=2))
