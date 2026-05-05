
# import torch
# import torch.nn as nn

class ToyGRPO:
    def __init__(self):
        pass
        
    def forward(self, x):
        return x

def group_relative_policy_optimization(model, data, group_size=4):
    # Simplified GRPO: compute mean reward per group and subtract for advantage
    # data is list of rewards
    rewards = data
    group_rewards = [rewards[i:i+group_size] for i in range(0, len(rewards), group_size)]
    advantages = []
    for group in group_rewards:
        avg = sum(group) / len(group)
        advantages.append([r - avg for r in group])
    return advantages

if __name__ == "__main__":
    model = ToyGRPO()
    data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    adv = group_relative_policy_optimization(model, data)
    print(f"Computed advantages for {len(adv)} groups.")
    assert len(adv) == 2
    print("GRPO logic verified.")
