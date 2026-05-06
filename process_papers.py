import json
import os
import re

with open('papers.json', 'r') as f:
    papers = json.load(f)

selected_papers = [
    {
        'title': 'OpenSeeker-v2: Pushing the Limits of Search Agents with Informative and High-Difficulty Trajectories',
        'summary': 'Deep search capabilities have become an indispensable competency for frontier Large Language Model (LLM) agents, yet their development remains dominated by industrial giants. The typical industry recipe involves a highly resource-intensive pipeline spanning pre-training, continual pre-training (CPT), supervised fine-tuning (SFT), and reinforcement learning (RL). In this report, we show that when fueled with informative and high-difficulty trajectories, a simple SFT approach could be surprisingly powerful for training frontier search agents. By introducing three simple data synthesis modifications: scaling knowledge graph size for richer exploration, expanding the tool set size for broader functionality, and strict low-step filtering, we establish a stronger baseline. Trained on merely 10.6k data points, our OpenSeeker-v2 achieves state-of-the-art performance across 4 benchmarks (30B-sized agents with ReAct paradigm): 46.0% on BrowseComp, 58.1% on BrowseComp-ZH, 34.6% on Humanity\'s Last Exam, and 78.0% on xbench, surpassing even Tongyi DeepResearch trained with heavy CPT+SFT+RL pipeline, which achieves 43.4%, 46.7%, 32.9%, and 75.0%, respectively. Notably, OpenSeeker-v2 represents the first state-of-the-art search agent within its model scale and paradigm to be developed by a purely academic team using only SFT. We are excited to open-source the OpenSeeker-v2 model weights and share our simple yet effective findings to make frontier search agent research more accessible to the community.',
        'field': 'AI (Agent search/SFT)',
        'relevance': 'Open-sources a frontier-level search agent trained via SFT without heavy RL, showing data quality drives search reasoning.',
        'takeaway': 'Informative mapping of high-difficulty trajectories via SFT can rival complex pipeline search agents.',
        'impl_status': 'approximation',
        'link': 'http://arxiv.org/abs/2605.04036v1'
    },
    {
        'title': 'Safety and accuracy follow different scaling laws in clinical large language models',
        'summary': 'Clinical LLMs are often scaled by increasing model size, context length, retrieval complexity, or inference-time compute, with the implicit expectation that higher accuracy implies safer behavior. This assumption is incomplete in medicine, where a few confident, high-risk, or evidence-contradicting errors can matter more than average benchmark performance. We introduce SaFE-Scale, a framework for measuring how clinical LLM safety changes across model scale, evidence quality, retrieval strategy, context exposure, and inference-time compute. To instantiate this framework, we introduce RadSaFE-200, a Radiology Safety-Focused Evaluation benchmark of 200 multiple-choice questions with clinician-defined clean evidence, conflict evidence, and option-level labels for high-risk error, unsafe answer, and evidence contradiction. We evaluated 34 locally deployed LLMs across six deployment conditions: closed-book prompting (zero-shot), clean evidence, conflict evidence, standard RAG, agentic RAG, and max-context prompting. Clean evidence produced the strongest improvement, increasing mean accuracy from 73.5% to 94.1%, while reducing high-risk error from 12.0% to 2.6%, contradiction from 12.7% to 2.3%, and dangerous overconfidence from 8.0% to 1.6%. Standard RAG and agentic RAG did not reproduce this safety profile: agentic RAG improved accuracy over standard RAG and reduced contradiction, but high-risk error and dangerous overconfidence remained elevated. Max-context prompting increased latency without closing the safety gap, and additional inference-time compute produced only limited gains. Worst-case analysis showed that clinically consequential errors concentrated in a small subset of questions. Clinical LLM safety is therefore not a passive consequence of scaling, but a deployment property shaped by evidence quality, retrieval design, context construction, and collective failure behavior.',
        'field': 'AI (LLM Safety/Medical)',
        'relevance': 'Highlights that safety does not automatically improve with accuracy in LLMs and is strongly bound to evidence quality and RAG design.',
        'takeaway': 'Clean evidence drastically improves both accuracy and safety, while agentic RAG and scaling compute increase accuracy but leave dangerous high-risk blindspots.',
        'impl_status': 'approximation',
        'link': 'http://arxiv.org/abs/2605.04039v1'
    },
    {
        'title': 'Sequence vs. Simultaneous Entanglement Swapping under Optimal Link-Layer Control',
        'summary': 'Connection-less, packet-switched quantum network architectures distribute entanglement across multi-hop paths through sequential entanglement swapping, in which each node acts on purely local state information. The architectural advantages over the connection-oriented alternative -- simultaneous SWAP-ASAP -- are compelling, but sequential swapping holds partial chains in intermediate buffers between successive swaps, exposing them to memory decoherence in a way simultaneous SWAP-ASAP avoids by design. We present a proof-of-principle study at fixed chain length n = 4 in which each elementary link is governed by a fixed reinforcement-learning policy optimizing the secret-key rate of the six-state protocol, leaving the network-layer protocol as the sole independent variable. Sweeping the network-layer memory coherence time over four orders of magnitude reveals a clear regime structure governed by the dimensionless ratio of coherence time to heralding latency. Simultaneous SWAP-ASAP delivers a constant rate across the full sweep. Sequential swapping, by contrast, collapses to zero end-to-end deliveries below a critical threshold, and begins recovering later. It remains limited by the simultaneous rate, which it saturates only at the relaxed end of the sweep. These results suggest that the connection-less penalty is a near-term phenomenon tied to present-day memory coherence rather than a fundamental property of sequential swapping.',
        'field': 'Quantum (Networking)',
        'relevance': 'Provides a direct comparison of entanglement swapping paradigms, critical for near-term scalable quantum network architecture.',
        'takeaway': 'Sequential entanglement swapping suffers high coherence penalties on current hardware compared to simultaneous SWAP but conceptually matches it given sufficient memory coherence.',
        'impl_status': 'approximation',
        'link': 'http://arxiv.org/abs/2605.04047v1'
    }
]

def format_title(title):
    t = title.lower()
    t = re.sub(r'[^a-z0-9\s-]', '', t)
    t = re.sub(r'\s+', '-', t)
    return t.strip('-')

for paper in selected_papers:
    folder_name = format_title(paper['title'])
    os.makedirs(f"{folder_name}/impl", exist_ok=True)
    
    with open(f"{folder_name}/README.md", 'w') as f:
        f.write(f"""# {paper['title']}

**Link:** {paper['link']}
**Field:** {paper['field']}
**Relevance:** {paper['relevance']}

## Summary
{paper['summary']}

## Implementation Status
**Status:** {paper['impl_status'].title()}

### Reason
Full implementation requires specialized training setups, hardware, or access to the specific datasets/models mentioned in the paper, which are not currently available or feasible to run in a short timeframe. 
We provide a conceptual scaffold reflecting the core mechanism discussed.
""")

    if 'openseeker' in folder_name:
        with open(f"{folder_name}/impl/search_agent_scaffold.py", 'w') as f:
            f.write("""# Concept: SFT-based Search Agent over Complex Trajectories
# This approximates the pipeline: generating high-quality synthetic trajectories
# through exploration and filtering, then fine-tuning a model (represented as a mock).

import random

class SearchEnvironment:
    def __init__(self, knowledge_graph_depth=5, tool_set_size=10):
        self.kg_depth = knowledge_graph_depth
        self.tool_set_size = tool_set_size

    def execute_action(self, action):
        # Mocking environment response
        success = random.random() > 0.3
        return {"success": success, "info": "Mocked environment state change."}

def synthesize_trajectories(env, num_samples=1000):
    trajectories = []
    for _ in range(num_samples):
        # 1. Broad Exploration (Expanded tools/KG)
        trajectory = [{"step": i, "action": f"tool_{random.randint(0, env.tool_set_size)}"} for i in range(random.randint(2, 8))]
        
        # 2. Strict Low-Step Filtering
        if len(trajectory) <= 4: # Prefer efficient paths
             # Check if path reached success (mock check)
             if random.random() > 0.5:
                 trajectories.append(trajectory)
                 
    return trajectories

def sft_fine_tune(model, trajectories):
    print(f"Fine-tuning {model} on {len(trajectories)} high-quality informative trajectories...")
    # Core insight: Data quality (filtered, complex trajectories) > RL volume
    print("Fine-tuning complete.")

if __name__ == "__main__":
    env = SearchEnvironment(knowledge_graph_depth=10, tool_set_size=25)
    high_quality_data = synthesize_trajectories(env, 5000)
    print(f"Synthesized {len(high_quality_data)} filtered trajectories.")
    sft_fine_tune("Base-LLM-30B", high_quality_data)
""")
    elif 'safety' in folder_name:
        with open(f"{folder_name}/impl/safety_evaluation_scaffold.py", 'w') as f:
            f.write("""# Concept: SaFE-Scale Medical LLM Evaluation
# Approximates the evaluation of LLM answers against different evidence qualities (Clean vs Conflict vs Zero-Shot).

class MedicalLLM:
    def __init__(self, scale="7B"):
        self.scale = scale
        self.base_accuracy = 0.7 if scale == "7B" else 0.85
        
    def generate_answer(self, query, evidence=None):
        if not evidence: # Zero-shot
            acc = self.base_accuracy - 0.1
            safety_risk = 0.15
        elif evidence == "clean":
            acc = self.base_accuracy + 0.1
            safety_risk = 0.02
        elif evidence == "conflict":
            acc = self.base_accuracy - 0.2
            safety_risk = 0.25 # High risk of contradiction
        else:
            acc = self.base_accuracy
            safety_risk = 0.1
            
        success = True if acc > 0.75 else False
        return {"answer": "Mock Answer", "correct": success, "high_risk_error": safety_risk > 0.1}

def evaluate_models():
    models = [MedicalLLM("7B"), MedicalLLM("70B")]
    conditions = [None, "clean", "conflict"]
    
    for model in models:
        print(f"\\nEvaluating {model.scale} model:")
        for cond in conditions:
            result = model.generate_answer("Assess radiology image X", evidence=cond)
            cond_str = cond if cond else "Zero-shot"
            print(f"Condition: {cond_str:10} | Correct: {result['correct']} | High Risk Error: {result['high_risk_error']}")
            
evaluate_models()
""")
    elif 'entanglement' in folder_name:
        with open(f"{folder_name}/impl/entanglement_sim_scaffold.py", 'w') as f:
            f.write("""# Concept: Sequential vs Simultaneous Entanglement Swapping Coherence Simulation
# Approximates the decay of entanglement fidelity based on memory coherence time and swapping strategy.

import math

def simulate_swapping(chain_length=4, coherence_time=100, heralding_latency=10, strategy="simultaneous"):
    base_fidelity = 0.99
    
    if strategy == "simultaneous":
        # All swaps happen ASAP, less time lingering in memory
        time_in_memory = heralding_latency
    elif strategy == "sequential":
        # Partial chains held in memory waiting for adjacent swaps
        # Scales with chain length
        time_in_memory = heralding_latency * (chain_length - 1)
        
    # Coherence penalty
    ratio = coherence_time / time_in_memory
    
    if ratio < 1.0:
        penalty = math.exp(-1/ratio) # steep dropoff if coherence < memory time
    else:
        penalty = 1.0 - (1/ratio) * 0.1 # gradual penalty
        
    final_fidelity = base_fidelity * penalty
    return max(0.0, final_fidelity)

print("Sweeping Coherence Time / Heralding Latency Ratios:\\n")
latency = 10
for coherence in [10, 50, 250, 1000, 5000]:
    ratio = coherence / latency
    sim_fid = simulate_swapping(coherence_time=coherence, heralding_latency=latency, strategy="simultaneous")
    seq_fid = simulate_swapping(coherence_time=coherence, heralding_latency=latency, strategy="sequential")
    print(f"Ratio: {ratio:5.1f} | Simultaneous Fidelity: {sim_fid:.3f} | Sequential Fidelity: {seq_fid:.3f}")
    if ratio < 25 and seq_fid < 0.1:
        print("  -> Sequential hit severe coherence threshold collapse.")
""")

