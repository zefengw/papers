import json

from src.kindhml_checker import run_demo

if __name__ == "__main__":
    out = run_demo()
    print(json.dumps(out, indent=2))
