class AgenticVerifier:
    def __init__(self):
        self.tools = {"calculator": lambda x: eval(x)}

    def forward_verify(self, steps):
        # Mock: check if each step follows from the previous
        print("[Forward Agent] Verifying steps sequentially...")
        for i, step in enumerate(steps):
            # In reality, this would be an LLM call
            if "ERROR" in step:
                return False, f"Error found at step {i}"
        return True, "All steps logically consistent."

    def backward_verify(self, conclusion, steps):
        # Mock: check if conclusion is supported by the final steps
        print("[Backward Agent] Verifying conclusion from premises...")
        if not steps or "ERROR" in steps[-1]:
            return False, "Conclusion not supported by final step."
        return True, "Conclusion is supported."

    def verify(self, solution_steps, conclusion):
        f_ok, f_msg = self.forward_verify(solution_steps)
        b_ok, b_msg = self.backward_verify(conclusion, solution_steps)
        
        if f_ok and b_ok:
            return "VERIFIED", f"{f_msg} | {b_msg}"
        else:
            return "REJECTED", f"{f_msg} | {b_msg}"

# Test
verifier = AgenticVerifier()
solution = ["Step 1: 2+2=4", "Step 2: 4*2=8"]
conclusion = "8"

status, msg = verifier.verify(solution, conclusion)
print(f"Status: {status}\nMessage: {msg}")

solution_bad = ["Step 1: 2+2=4", "Step 2: ERROR"]
status_bad, msg_bad = verifier.verify(solution_bad, conclusion)
print(f"Status: {status_bad}\nMessage: {msg_bad}")
