# Set-of-Mark (SoM) Planning Sketch
def predict_action(image, task):
    # 1. Overlay marks on actionable objects (Buttons, Handles)
    marks = some_segmentation_model(image)
    marked_image = overlay(image, marks)
    
    # 2. Ask Magma to choose a mark
    # Prompt: "To open the door, which mark should I pull?"
    chosen_mark_id = magma.query(marked_image, task)
    
    # 3. Resolve coordinate
    coords = marks[chosen_mark_id].center
    return f"Click at {coords}"
