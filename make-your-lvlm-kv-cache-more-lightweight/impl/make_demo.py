
import numpy as np

def lightkv_sim(vision_tokens, text_prompts, ratio=0.5):
    # Mean prompt embedding
    prompt_avg = np.mean(text_prompts, axis=0)
    # Cosine similarity importance
    importance = np.dot(vision_tokens, prompt_avg)
    k = int(len(vision_tokens) * ratio)
    indices = np.argsort(importance)[-k:]
    return vision_tokens[indices]

v_tokens = np.random.randn(100, 128)
t_prompts = np.random.randn(10, 128)
comp = lightkv_sim(v_tokens, t_prompts)
print(f"Original: {len(v_tokens)}, Compressed: {len(comp)}")
