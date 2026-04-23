
def convert_trace_to_semantic_prompt(trace):
    prompt_template = """
    Analyze the following heterogeneous blockchain transaction trace for fraud.
    Translate this raw bytecode interaction into natural language semantics:
    {trace_data}
    """
    return prompt_template.format(trace_data=str(trace))
