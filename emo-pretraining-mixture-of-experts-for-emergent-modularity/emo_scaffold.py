import torch
import torch.nn as nn
import torch.nn.functional as F

class EMO_Router_Scaffold(nn.Module):
    """
    A simplified routing mechanism that restricts tokens in the same document
    to prefer similar expert subsets, simulating the core constraint of EMO.
    """
    def __init__(self, d_model, num_experts, top_k=2):
        super().__init__()
        self.num_experts = num_experts
        self.top_k = top_k
        self.gate = nn.Linear(d_model, num_experts, bias=False)
        
    def forward(self, x, doc_indices):
        """
        x: [batch * seq_len, d_model]
        doc_indices: [batch * seq_len] mapping tokens to document IDs
        """
        logits = self.gate(x)
        routing_weights = F.softmax(logits, dim=-1)
        
        # In a real MoE, we'd pick top_k.
        # For EMO, we also want to calculate a penalty to encourage
        # tokens from the same doc to have similar routing distributions.
        
        # Calculate centroids of routing distributions per document
        unique_docs = torch.unique(doc_indices)
        doc_penalty = 0.0
        
        for doc_id in unique_docs:
            doc_mask = (doc_indices == doc_id)
            doc_weights = routing_weights[doc_mask]  # [num_tokens_in_doc, num_experts]
            
            if doc_weights.size(0) > 1:
                # Mean distribution across tokens in this doc
                doc_centroid = doc_weights.mean(dim=0, keepdim=True)
                # MSE penalty between individual tokens and document centroid
                # This encourages tokens in the same doc to select the same experts
                penalty = F.mse_loss(doc_weights, doc_centroid.expand_as(doc_weights))
                doc_penalty += penalty
                
        doc_penalty = doc_penalty / len(unique_docs)
        
        return routing_weights, doc_penalty

if __name__ == "__main__":
    d_model = 64
    num_experts = 8
    seq_len = 10
    
    # Simulate a batch with 2 different documents
    # First 5 tokens = doc 0, next 5 tokens = doc 1
    x = torch.randn(seq_len, d_model)
    doc_indices = torch.tensor([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
    
    router = EMO_Router_Scaffold(d_model, num_experts)
    weights, penalty = router(x, doc_indices)
    
    print("Routing Weights Shape:", weights.shape)
    print("Document Routing Penalty (simulate EMO loss):", penalty.item())
