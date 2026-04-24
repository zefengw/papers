# Hyperloop Transformer - PyTorch Implementation
# Implementation of [2604.21254v1] Hyperloop Transformers

import math
import torch
import torch.nn as nn
import torch.nn.functional as F

class ProgressGate(nn.Module):
    def __init__(self, d_model: int):
        super().__init__()
        self.w_prev = nn.Linear(d_model, d_model, bias=False)
        self.w_cand = nn.Linear(d_model, d_model, bias=False)
        self.w_step = nn.Linear(d_model, d_model, bias=False)
        self.bias   = nn.Parameter(torch.full((d_model,), -2.0))

    def forward(self, h_prev, h_cand, step_emb):
        return torch.sigmoid(self.w_prev(h_prev) + self.w_cand(h_cand) + self.w_step(step_emb) + self.bias)

class SharedTransformerBlock(nn.Module):
    def __init__(self, d_model, n_heads, d_ff, dropout=0.1):
        super().__init__()
        self.norm1 = nn.LayerNorm(d_model)
        self.attn  = nn.MultiheadAttention(d_model, n_heads, dropout=dropout, batch_first=True)
        self.drop1 = nn.Dropout(dropout)
        self.norm2 = nn.LayerNorm(d_model)
        self.ffn   = nn.Sequential(nn.Linear(d_model, d_ff), nn.GELU(), nn.Dropout(dropout), nn.Linear(d_ff, d_model), nn.Dropout(dropout))

    def forward(self, x, attn_mask=None):
        h = self.norm1(x)
        h, _ = self.attn(h, h, h, attn_mask=attn_mask)
        x = x + self.drop1(h)
        x = x + self.ffn(self.norm2(x))
        return x

class HyperloopLayer(nn.Module):
    def __init__(self, d_model, n_heads, d_ff, max_iterations=6, dropout=0.1):
        super().__init__()
        self.max_iterations = max_iterations
        self.block = SharedTransformerBlock(d_model, n_heads, d_ff, dropout)
        self.step_emb = nn.Embedding(max_iterations, d_model)
        self.gate = ProgressGate(d_model)
        self.out_norm = nn.LayerNorm(d_model)

    def forward(self, x, attn_mask=None):
        B, S, D = x.shape
        h = x
        for t in range(self.max_iterations):
            e_t = self.step_emb(torch.tensor([t], device=x.device)).view(1, 1, -1).expand(B, S, -1)
            h_cand = self.block(h + e_t, attn_mask)
            g = self.gate(h, h_cand, e_t)
            h = g * h_cand + (1.0 - g) * h
        return self.out_norm(h)

if __name__ == "__main__":
    # Demo
    model = HyperloopLayer(128, 4, 256, max_iterations=4)
    x = torch.randn(2, 10, 128)
    out = model(x)
    print(f"Input shape: {x.shape}")
    print(f"Output shape: {out.shape}")
    print("Hyperloop layer forward pass successful.")
