import json
from src.token_efficient_rl import run_comparison

if __name__ == "__main__":
    print(json.dumps(run_comparison(), indent=2))
