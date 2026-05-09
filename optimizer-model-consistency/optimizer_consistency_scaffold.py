import torch
import torch.nn as nn
import torch.optim as optim
import copy

# Synthetic task scaffold measuring generic loss
# In reality, this would be Language Modeling (Pretrain) -> Instruction Tuning (SFT)
class ToyLLM(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(10, 50),
            nn.ReLU(),
            nn.Linear(50, 10)
        )
    def forward(self, x):
        return self.net(x)

def run_experiment():
    print("--- Optimizer-Model Consistency Toy Experiment ---")
    
    # 1. Provide 'Pre-training' data and 'SFT' data
    torch.manual_seed(42)
    pretrain_X = torch.randn(100, 10)
    pretrain_Y = torch.randn(100, 10) # Task A
    
    sft_X = torch.randn(100, 10)
    sft_Y = torch.randn(100, 10) # Task B
    
    criterion = nn.MSELoss()
    
    # 2. Phase 1: Pre-training with SGD (representing the pre-train optimizer)
    model = ToyLLM()
    optimizer_pt = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
    
    print("Pre-training with SGD...")
    for epoch in range(50):
        optimizer_pt.zero_grad()
        loss = criterion(model(pretrain_X), pretrain_Y)
        loss.backward()
        optimizer_pt.step()
        
    print(f"Final Pretrain Loss: {loss.item():.4f}")
    
    # Checkpoint
    checkpoint = {
        'model_state': copy.deepcopy(model.state_dict()),
        'optimizer_state': copy.deepcopy(optimizer_pt.state_dict())
    }
    
    # 3. Phase 2 Branch A: Fine-tune with SAME optimizer (SGD)
    model_same = ToyLLM()
    model_same.load_state_dict(checkpoint['model_state'])
    optimizer_same = optim.SGD(model_same.parameters(), lr=0.001, momentum=0.9)
    # Crucial finding: inheriting state heavily influences the landscape
    # optimizer_same.load_state_dict(checkpoint['optimizer_state']) 
    
    for epoch in range(20):
        optimizer_same.zero_grad()
        loss_sft = criterion(model_same(sft_X), sft_Y)
        loss_sft.backward()
        optimizer_same.step()
        
    # Measure 'Forgetting' on Pretrain Task
    with torch.no_grad():
        forget_same = criterion(model_same(pretrain_X), pretrain_Y).item()
        
    # 4. Phase 2 Branch B: Fine-tune with DIFFERENT optimizer (AdamW)
    model_diff = ToyLLM()
    model_diff.load_state_dict(checkpoint['model_state'])
    optimizer_diff = optim.AdamW(model_diff.parameters(), lr=0.001)
    
    for epoch in range(20):
        optimizer_diff.zero_grad()
        loss_sft = criterion(model_diff(sft_X), sft_Y)
        loss_sft.backward()
        optimizer_diff.step()
        
    # Measure 'Forgetting' on Pretrain Task
    with torch.no_grad():
        forget_diff = criterion(model_diff(pretrain_X), pretrain_Y).item()

    print(f"\nForgetting evaluation (lower is better):")
    print(f"Pre-train task loss when SFT used SAME optimizer (SGD): {forget_same:.4f}")
    print(f"Pre-train task loss when SFT used DIFF optimizer (AdamW): {forget_diff:.4f}")
    
if __name__ == "__main__":
    run_experiment()
