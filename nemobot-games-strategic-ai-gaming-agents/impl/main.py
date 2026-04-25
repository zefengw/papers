
class StrategicAgent:
    def __init__(self, name, strategy="rational"):
        self.name = name
        self.strategy = strategy

    def decide(self, state):
        # Placeholder for LLM-based reasoning
        if self.strategy == "rational":
            return f"{self.name} chooses optimal move based on {state}"
        return f"{self.name} plays randomly"

def simulate_game():
    agents = [StrategicAgent("Alice"), StrategicAgent("Bob", "random")]
    state = "Game Start"
    for i in range(3):
        for agent in agents:
            action = agent.decide(state)
            print(f"Turn {i}: {action}")
            state = f"After {agent.name} move"

if __name__ == "__main__":
    simulate_game()
