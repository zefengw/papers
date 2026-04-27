
import torch
import torch.nn as nn

class AbstractCOTModel(nn.Module):
    def __init__(self, vocab_size, embed_dim, latent_dim):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.transformer = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(d_model=embed_dim, nhead=8), num_layers=4
        )
        self.abtract_thought_head = nn.Linear(embed_dim, latent_dim)
        self.output_head = nn.Linear(latent_dim, vocab_size)

    def forward(self, x):
        embedded = self.embedding(x)
        features = self.transformer(embedded)
        # Use first token or pooled feature for abstract thought
        thought = self.abtract_thought_head(features.mean(dim=1))
        logits = self.output_head(thought)
        return logits, thought

if __name__ == "__main__":
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = AbstractCOTModel(vocab_size=1000, embed_dim=256, latent_dim=128).to(device)
    dummy_input = torch.randint(0, 1000, (1, 32)).to(device)
    logits, thought = model(dummy_input)
    print(f"Model output shape: {logits.shape}, Latent thought shape: {thought.shape}")
