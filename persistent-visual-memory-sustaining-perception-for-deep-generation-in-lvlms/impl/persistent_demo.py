
import torch
import torch.nn as nn

class PVM(nn.Module):
    def __init__(self, dim, visual_dim):
        super().__init__()
        self.retrieval_gate = nn.Linear(dim, 1)
        self.visual_proj = nn.Linear(visual_dim, dim)

    def forward(self, x, visual_memory):
        # x: [B, L, D], visual_memory: [B, N, V_D]
        gate = torch.sigmoid(self.retrieval_gate(x))
        # Simplified cross-attention retrieval
        scores = torch.matmul(x, self.visual_proj(visual_memory).transpose(-1, -2))
        weights = torch.softmax(scores, dim=-1)
        v_retrieved = torch.matmul(weights, self.visual_proj(visual_memory))
        return x + gate * v_retrieved

# Toy test
dim, visual_dim = 128, 256
model = PVM(dim, visual_dim)
x = torch.randn(1, 10, dim)
v_mem = torch.randn(1, 5, visual_dim)
out = model(x, v_mem)
print(f"PVM Output Shape: {out.shape}")
assert out.shape == x.shape
