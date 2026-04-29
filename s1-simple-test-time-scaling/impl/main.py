# Budget Forcing Implementation
def generate_with_budget(prompt, model, tokenizer, forced_length=512):
    thinking_tokens = []
    for _ in range(forced_length):
        # Output distribution
        probs = model.get_probs(prompt + thinking_tokens)
        
        # Suppress </think> if count < min_budget
        if len(thinking_tokens) < forced_length:
            probs[tokenizer.encode('</think>')] = -float('inf')
            # Inject 'Wait' occasionally to force continuation
            if len(thinking_tokens) % 100 == 0:
                thinking_tokens.append(tokenizer.encode('Wait'))
        
        token = sample(probs)
        thinking_tokens.append(token)
    return thinking_tokens
