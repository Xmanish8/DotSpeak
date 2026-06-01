import streamlit as st
from ultralytics import YOLO
from PIL import Image
from pathlib import Path
import tempfile

st.set_page_config(page_title="BrailleVision AI", layout="centered")

st.title("BrailleVision AI")
st.write("Upload or capture one cropped Braille character image.")

MODEL_PATH = Path("best.pt")

@st.cache_resource
def load_model():
    return YOLO(str(MODEL_PATH))

model = load_model()

uploaded_file = st.file_uploader("Upload Braille Image", type=["jpg", "jpeg", "png"])
camera_file = st.camera_input("Or capture from camera")

file = uploaded_file if uploaded_file else camera_file

if file:
    image = Image.open(file).convert("RGB")
    st.image(image, caption="Input Image", use_container_width=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        image.save(tmp.name)
        temp_path = tmp.name

    results = model.predict(source=temp_path, imgsz=64, verbose=False)

    probs = results[0].probs
    label = model.names[probs.top1]
    conf = probs.top1conf.item()

    st.success(f"Predicted Letter: {label}")
    st.info(f"Confidence: {conf:.3f}")

    st.components.v1.html(
        f"""
        <script>
        const msg = new SpeechSynthesisUtterance("Predicted letter is {label}");
        window.speechSynthesis.speak(msg);
        </script>
        """,
        height=0,
    )
