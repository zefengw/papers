
def sequential_bayesian_update(prior, evidence, llm_likelihood_fn):
    posterior = {}
    for event, prob in prior.items():
        likelihood = llm_likelihood_fn(event, evidence)
        posterior[event] = prob * likelihood
    
    # Normalize
    total = sum(posterior.values())
    if total > 0:
        for k in posterior:
            posterior[k] /= total
    return posterior
