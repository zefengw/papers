
def outcome_reward_model(correct_answer, predicted_answer):
    return 1.0 if correct_answer == predicted_answer else 0.0

def process_reward_model(steps):
    # Simulate process reward by grading each step
    return [random.uniform(0, 1) for _ in steps]

if __name__ == "__main__":
    import random
    orm = outcome_reward_model("42", "42")
    prm = process_reward_model(["Step 1", "Step 2", "Step 3"])
    print(f"ORM: {orm}, PRM mean: {sum(prm)/len(prm)}")
    assert orm == 1.0
    print("Reward models verified.")
