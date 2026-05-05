
class MagmaAgent:
    def __init__(self, name="Magma"):
        self.name = name
    
    def perceive(self, visual_input, text_input):
        return f"Perceived: {visual_input} and {text_input}"
    
    def act(self, state):
        return f"Action based on {state}"

if __name__ == "__main__":
    agent = MagmaAgent()
    p = agent.perceive("Image of room", "Find the keys")
    a = agent.act(p)
    print(a)
    assert "Perceived" in p
    print("Magma simulation successful.")
