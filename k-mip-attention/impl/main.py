
import torch
import torch.nn as nn
import torch.nn.functional as F

class KMIPAttention(nn.Module):
    def __init__(self, dim, k=4):
        super().__init__()
        self.dim = dim
        self.k = k
        self.q = nn.Linear(dim, dim)
        self.k = nn.Linear(dim, dim)
        self.v = nn.Linear(dim, dim)

    def forward(self, x):
        # x: (batch, seq_len, dim)
        b, s, d = x.shape
        q = self.q(x)
        k = self.k(x)
        v = self.v(x)
        
        # Compute inner product (similarity)
        sim = torch.matmul(q, k.transpose(-2, -1)) # (b, s, s)
        
        # k-MIP approximation: only keep top k values
        topk_vals, topk_indices = torch.topk(sim, self.k, dim=-1)
        
        # Mask other values to -inf
        mask = torch.full_like(sim, float('-inf'))
        mask.scatter_(-1, topk_indices, topk_vals)
        
        attn = F.softmax(mask, dim=-1)
        out = torch.matmul(attn, v)
        return out

if __name__ == '__main__':
    x = torch.randn(1, 10, 32)
    attn_layer = KMIPAttention(32, k=3)
    out = attn_layer(x)
    print("Input shape:", x.shape)
    print("Output shape:", out.shape)
