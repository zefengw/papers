import json
from src.light_r1_pipeline import run_demo

if __name__ == "__main__":
    metrics = run_demo()
    print(json.dumps(metrics, indent=2))
