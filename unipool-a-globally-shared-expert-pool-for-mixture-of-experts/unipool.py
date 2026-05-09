import torch
import torch.nn as nn
import torch.nn.functional as F

class Expert(nn.Module):
    def __init__(self, d_model, d_ff):
        super().__init__()
        self.w1 = nn.Linear(d_model, d_ff, bias=False)
        self.w2 = nn.Linear(d_ff, d_model, bias=False)
        
    def forward(self, x):
        return self.w2(F.silu(self.w1(x)))

class VanillaMoELayer(nn.Module):
    def __init__(self, d_model, d_ff, num_experts):
        super().__init__()
        self.experts = nn.ModuleList([Expert(d_model, d_ff) for _ in range(num_experts)])
        self.router = nn.Linear(d_model, num_experts, bias=False)
        
    def forward(self, x):
        # Simplified top-1 routing for demonstration
        logits = self.router(x)
        weights, indices = torch.max(F.softmax(logits, dim=-1), dim=-1)
        
        out = torch.zeros_like(x)
        # In a real implementation this is batched via scatter/gather
        for i, expert in enumerate(self.experts):
            mask = (indices == i)
            if mask.any():
                out[mask] = expert(x[mask]) * weights[mask].unsqueeze(-1)
        return out

class VanillaMoEModel(nn.Module):
    def __init__(self, num_layers, d_model, d_ff, experts_per_layer):
        super().__init__()
        self.layers = nn.ModuleList([
            VanillaMoELayer(d_model, d_ff, experts_per_layer) 
            for _ in range(num_layers)
        ])
    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

class UniPoolLayer(nn.Module):
    def __init__(self, d_model, global_experts):
        super().__init__()
        self.num_global_experts = len(global_experts)
        self.global_experts = global_experts  # Reference to shared pool
        self.router = nn.Linear(d_model, self.num_global_experts, bias=False)
        
    def forward(self, x):
        logits = self.router(x)
        weights, indices = torch.max(F.softmax(logits, dim=-1), dim=-1)
        
        out = torch.zeros_like(x)
        for i, expert in enumerate(self.global_experts):
            mask = (indices == i)
            if mask.any():
                out[mask] = expert(x[mask]) * weights[mask].unsqueeze(-1)
        return out

class UniPoolModel(nn.Module):
    def __init__(self, num_layers, d_model, d_ff, total_global_experts):
        super().__init__()
        # Centralized pool of experts
        self.expert_pool = nn.ModuleList([
            Expert(d_model, d_ff) for _ in range(total_global_experts)
        ])
        
        self.layers = nn.ModuleList([
            UniPoolLayer(d_model, self.expert_pool) 
            for _ in range(num_layers)
        ])
        
    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

if __name__ == "__main__":
    num_layers = 12
    d_model = 128
    d_ff = 512
    
    # Vanilla: 8 experts PER layer
    vanilla_experts_per_layer = 8
    model_vanilla = VanillaMoEModel(num_layers, d_model, d_ff, vanilla_experts_per_layer)
    params_vanilla = sum(p.numel() for p in model_vanilla.parameters())
    
    # UniPool: 32 experts GLOBALLY (sub-linear, much smaller than 12 * 8 = 96)
    total_unipool_experts = 32
    model_unipool = UniPoolModel(num_layers, d_model, d_ff, total_unipool_experts)
    params_unipool = sum(p.numel() for p in model_unipool.parameters())
    
    print("--- UniPool vs Vanilla MoE Architecture Comparison ---")
    print(f"Vanilla MoE (12 layers, 8 per layer = 96 total experts): {params_vanilla:,} parameters")
    print(f"UniPool (12 layers, 32 global experts total):          {params_unipool:,} parameters")
    print(f"Parameter Reduction: {(1 - params_unipool/params_vanilla)*100:.1f}%")
    
    x = torch.randn(10, d_model)
    out_vanilla = model_vanilla(x)
    out_unipool = model_unipool(x)
    
    print("\nForward pass successful for both architectures.")
