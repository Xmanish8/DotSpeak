import streamlit as st
from ultralytics import YOLO
from PIL import Image
from pathlib import Path
import tempfile

st.set_page_config(page_title="BrailleVision AI", layout="centered")

st.title("BrailleVision AI")
st.write("Upload image or use webcam to capture one cropped Braille character.")

MODEL_PATH = Path("best.pt")

@st.cache_resource
def load_model():
    return YOLO(str(MODEL_PATH))

model = load_model()

option = st.radio(
    "Choose input method",
    ["Upload Image", "Use Webcam"]
)

file = None

if option == "Upload Image":
    file = st.file_uploader(
        "Upload Braille character image",
        type=["jpg", "jpeg", "png"]
    )

if option == "Use Webcam":
    file = st.camera_input("Take a Braille character photo")

if file is not None:
    image = Image.open(file).convert("RGB")
    st.image(image, caption="Input Image", use_container_width=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        image.save(tmp.name)
        temp_path = tmp.name

    results = model.predict(
        source=temp_path,
        imgsz=64,
        verbose=False
    )

    probs = results[0].probs
    label = model.names[probs.top1]
    conf = probs.top1conf.item()

    st.success(f"Predicted Letter: {label}")
    st.info(f"Confidence: {conf:.3f}")

    st.markdown(
        f"""
        <script>
        const msg = new SpeechSynthesisUtterance("Predicted letter is {label}");
        window.speechSynthesis.speak(msg);
        </script>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning("Please upload an image or capture from webcam.")
