
import numpy as np

def dual_speed_sampler(video_frames, fast_rate=1, slow_rate=5):
    """
    Simulates seeing fast (high temporal resolution) and 
    slow (high spatial/semantic resolution at key intervals).
    """
    fast_indices = np.arange(0, len(video_frames), fast_rate)
    slow_indices = np.arange(0, len(video_frames), slow_rate)
    
    return {
        'fast_stream': [video_frames[i] for i in fast_indices],
        'slow_stream': [video_frames[i] for i in slow_indices]
    }

if __name__ == "__main__":
    frames = [f"frame_{i}" for i in range(20)]
    sampled = dual_speed_sampler(frames)
    print("Fast bits (motion):", sampled['fast_stream'])
    print("Slow bits (objects):", sampled['slow_stream'])
