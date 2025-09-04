import os
import gradio as gr
from ultralytics import YOLO

# ----------------------
# Load your trained YOLO model
# ----------------------
MODEL_PATH = "best.pt"  # Put your weights file in the repo root or /models/
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"❌ Model file not found at {MODEL_PATH}. Please upload best.pt to your Space.")

model = YOLO(MODEL_PATH)

# ----------------------
# Prediction function
# ----------------------
def predict(image, conf_threshold=0.5):
    """
    Run YOLO prediction on the uploaded image.
    Returns the annotated image.
    """
    results = model.predict(image, conf=conf_threshold, save=False)
    # results[0].plot() gives back a numpy array with predictions drawn
    return results[0].plot()

# ----------------------
# Gradio Interface
# ----------------------
demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Image(type="filepath", label="Upload an Image"),
        gr.Slider(0, 1, value=0.5, step=0.05, label="Confidence Threshold")
    ],
    outputs=gr.Image(type="numpy", label="Predicted Image"),
    title="🚀 Space Station Detection",
    description="Upload an image and the YOLO model will detect objects (trained on your dataset)."
)

if __name__ == "__main__":
    demo.launch()
