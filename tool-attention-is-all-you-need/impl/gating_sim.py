
import numpy as np

class ToolRegistry:
    def __init__(self):
        self.tools = {}
        self.tool_index = None
    
    def add_tool(self, name, description, schema):
        self.tools[name] = {"description": description, "schema": schema}
        
    def build_index(self):
        # In a real impl, we'd use sentence-transformers
        # Here we mock embeddings with random vectors for demonstration
        self.tool_names = list(self.tools.keys())
        self.tool_vectors = np.random.rand(len(self.tool_names), 32)
        
    def gate_query(self, query_vector, k=3):
        scores = np.dot(self.tool_vectors, query_vector)
        top_k_indices = np.argsort(scores)[-k:][::-1]
        return [self.tool_names[i] for i in top_k_indices]

# Simulation
registry = ToolRegistry()
for i in range(100):
    registry.add_tool(f"tool_{i}", f"Does something related to {i}", {"type": "object"})
registry.build_index()

query_vec = np.random.rand(32)
selected = registry.gate_query(query_vec)
print(f"Query triggered tools: {selected}")
