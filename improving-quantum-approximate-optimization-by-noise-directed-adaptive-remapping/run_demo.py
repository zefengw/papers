import json
from src.ndar_qaoa_sim import run_ndar_demo

if __name__ == "__main__":
    print(json.dumps(run_ndar_demo(), indent=2))
