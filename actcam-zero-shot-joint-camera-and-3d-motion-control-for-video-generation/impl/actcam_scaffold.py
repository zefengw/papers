import numpy as np

class MockDiffusionSampler:
    def __init__(self, num_steps=50, depth_drop_step=20):
        self.num_steps = num_steps
        self.depth_drop_step = depth_drop_step # Phase 1 ends here

    def sample(self, initial_noise, pose_conditions, depth_conditions):
        """
        Simulates the two-phase ActCam sampling schedule over T steps.
        Phase 1: Condition on both pose and depth for structural layout.
        Phase 2: Drop depth, condition only on pose for finer details.
        """
        latents = initial_noise
        print(f"Starting generation with {self.num_steps} steps. Depth drop at step {self.depth_drop_step}.")
        
        for step in range(self.num_steps):
            if step < self.depth_drop_step:
                # Phase 1: Pose + Depth Conditioning
                guidance = f"Pose + Depth guidance applied"
                latents = self._denoise_step(latents, step, condition=guidance)
            else:
                # Phase 2: Pose Only Conditioning
                guidance = f"Pose ONLY guidance applied (Depth dropped)"
                latents = self._denoise_step(latents, step, condition=guidance)
                
            if step % 10 == 0 or step == self.num_steps - 1:
                print(f"Step {step+1:02d}: {guidance}")

        print("Generation complete.")
        return latents

    def _denoise_step(self, latents, step, condition):
        # Simulate a small modification to latents based on condition
        assert latents is not None
        return latents - (0.01 * np.random.randn(*latents.shape))

if __name__ == "__main__":
    sampler = MockDiffusionSampler(num_steps=50, depth_drop_step=20)
    
    # Mock data for conditional inputs
    noise = np.random.randn(1, 4, 64, 64) # Batch, Channels, H, W
    pose_cond = "Mock Pose Sequence"
    depth_cond = "Mock Depth Sequence"
    
    final_video_latents = sampler.sample(noise, pose_cond, depth_cond)
