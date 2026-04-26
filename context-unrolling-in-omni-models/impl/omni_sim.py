
class OmniModel:
    def __init__(self):
        self.modalities = ["text", "image", "video", "3d"]
        
    def unroll_context(self, interleaved_context):
        # Conceptual unrolling: separate and expand modalities
        unrolled = {}
        for mod in self.modalities:
            unrolled[mod] = [item for item in interleaved_context if item["type"] == mod]
        return unrolled

# Simulation
context = [
    {"type": "text", "content": "Look at this video:"},
    {"type": "video", "content": "vid_01.mp4"},
    {"type": "text", "content": "And this 3D model:"},
    {"type": "3d", "content": "mesh_01.obj"}
]

omni = OmniModel()
unrolled = omni.unroll_context(context)
print(f"Unrolled Context Modalities: {list(unrolled.keys())}")
