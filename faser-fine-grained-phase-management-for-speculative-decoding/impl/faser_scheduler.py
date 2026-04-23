
class FASERScheduler:
    def __init__(self, draft_model_quota, target_model_quota):
        self.draft_quota = draft_model_quota
        self.target_quota = target_model_quota
        self.phase = "DRAFTING"
        
    def step(self, request_queue):
        if self.phase == "DRAFTING":
            print("Running draft model inferences...")
            return self.draft_quota
        else:
            print("Running target model verification...")
            return self.target_quota
