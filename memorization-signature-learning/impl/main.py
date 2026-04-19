
import torch
import torch.nn.functional as F

def compute_memorization_score(model, token_ids, labels):
    # simplified: memorized tokens often have very low loss and very high confidence
    model.eval()
    with torch.no_grad():
        logits = model(token_ids)
        loss = F.cross_entropy(logits.view(-1, logits.size(-1)), labels.view(-1), reduction='none')
        probs = F.softmax(logits, dim=-1)
        confidences = torch.gather(probs, -1, labels.unsqueeze(-1)).squeeze(-1)
        
    # Signature: Low loss AND high confidence
    # Score = exp(-loss) * confidence
    score = torch.exp(-loss) * confidences
    return score.mean().item()

class DummyLM(torch.nn.Module):
    def __init__(self, v=100, d=32):
        super().__init__()
        self.embed = torch.nn.Embedding(v, d)
        self.linear = torch.nn.Linear(d, v)
    def forward(self, x):
        return self.linear(self.embed(x))

if __name__ == '__main__':
    model = DummyLM()
    tokens = torch.randint(0, 100, (1, 10))
    labels = torch.randint(0, 100, (1, 10))
    score = compute_memorization_score(model, tokens, labels)
    print(f"Memorization Score: {score:.4f}")
