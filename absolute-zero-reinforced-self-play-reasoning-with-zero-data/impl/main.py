# Absolute Zero Paradigm Sketch
class AZRAgent:
    def propose_task(self):
        # Generate a problem + test case
        return "Solve 2+2", "assert answer == 4"
    
    def solve_task(self, prompt):
        # Generate solution
        return "answer = 4"

def verify(solution, test_case):
    try:
        exec(solution)
        exec(test_case)
        return 1.0
    except:
        return 0.0

# Self-play loop
agent = AZRAgent()
for _ in range(100):
   task, test = agent.propose_task()
   sol = agent.solve_task(task)
   reward = verify(sol, test)
   # Update agent with RL (e.g. GRPO)
