
import hashlib
import time

class FairMempool:
    def __init__(self):
        self.queue = []
        self.identities = {} # Maps user to last nonce
        
    def submit_tx(self, user_id, payload, signature):
        # In practice, verify identity signature
        timestamp = time.time()
        tx = {
            "user": user_id,
            "payload": payload,
            "timestamp": timestamp,
            "id": hashlib.sha256(f"{user_id}{payload}{timestamp}".encode()).hexdigest()
        }
        self.queue.append(tx)
        
    def get_fair_order(self):
        # Strict FCFS based on arrival in the authenticated sequence
        return sorted(self.queue, key=lambda x: x["timestamp"])

# Simulation
mempool = FairMempool()
mempool.submit_tx("user_A", "buy 1 ETH", "sig_A")
time.sleep(0.01)
mempool.submit_tx("proposer", "frontrun user_A", "sig_P") # Submitted later

ordered = mempool.get_fair_order()
for tx in ordered:
    print(f"User: {tx['user']}, ID: {tx['id'][:8]}")
