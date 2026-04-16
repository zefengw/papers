import json

from src.distributed_quantum_search import run_demo

if __name__ == "__main__":
    out = run_demo(seed=23)
    print(json.dumps(out, indent=2))
