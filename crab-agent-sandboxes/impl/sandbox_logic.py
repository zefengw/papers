import json

class CrabSandbox:
    """
    Simulation of the 'Crab' semantics-aware checkpointing.
    Stores high-level state snapshots.
    """
    def __init__(self):
        self.state = {"services": {}, "files": {}}
        self.snapshots = {}

    def checkpoint(self, label):
        """Perform a semantic checkpoint"""
        print(f"Crab: Saving checkpoint [{label}]")
        self.snapshots[label] = json.dumps(self.state)

    def restore(self, label):
        """Restore to a previous semantic state"""
        if label in self.snapshots:
            print(f"Crab: Restoring to [{label}]")
            self.state = json.loads(self.snapshots[label])
        else:
            print(f"Error: label {label} not found")

    def perform_action(self, action_type, key, value):
        self.state[action_type][key] = value

if __name__ == "__main__":
    sandbox = CrabSandbox()
    
    # Init state
    sandbox.perform_action("services", "auth", "logged_in")
    sandbox.checkpoint("post-login")
    
    # State change that might fail
    sandbox.perform_action("files", "data.csv", "corrupted_content")
    print(f"Current State: {sandbox.state}")
    
    # Rollback
    sandbox.restore("post-login")
    print(f"Restored State: {sandbox.state}")
