
class MultiCommitAnalyzer:
    def __init__(self):
        self.history = []

    def track_data_flow(self, commit_diff):
        self.history.append(commit_diff)
        # Simplified: Check if sensitive data introduced in C1 is leaked in C2
        sensitive = [d for d in self.history if "API_KEY" in d]
        exposure = [d for d in self.history if "print" in d]
        if sensitive and exposure:
            return "VULNERABILITY: Cross-commit sensitive data exposure detected."
        return "Safe."

if __name__ == "__main__":
    analyzer = MultiCommitAnalyzer()
    print(analyzer.track_data_flow("Added API_KEY to config"))
    print(analyzer.track_data_flow("Added debug logs with print statements"))
