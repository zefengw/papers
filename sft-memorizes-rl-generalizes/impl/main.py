
class Model:
    def __init__(self, mode="SFT"):
        self.mode = mode
    
    def predict(self, x):
        if self.mode == "SFT":
            return "Pattern match" # Memorization
        return "Reasoned output" # Generalization

if __name__ == "__main__":
    sft_model = Model("SFT")
    rl_model = Model("RL")
    print(f"SFT: {sft_model.predict(1)}, RL: {rl_model.predict(1)}")
    assert sft_model.predict(1) != rl_model.predict(1)
    print("RL vs SFT hypothesis simulated.")
