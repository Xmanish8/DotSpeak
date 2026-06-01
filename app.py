import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
from ultralytics import YOLO
import av
import cv2
from pathlib import Path

st.set_page_config(page_title="BrailleVision AI Realtime", layout="wide")

st.title("BrailleVision AI - Realtime Web Camera")
st.write("Place one Braille character/cell inside the green box.")

MODEL_PATH = Path("best.pt")

@st.cache_resource
def load_model():
    return YOLO(str(MODEL_PATH))

model = load_model()


class BrailleProcessor(VideoProcessorBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        h, w = img.shape[:2]

        box_size = 220
        x1 = w // 2 - box_size // 2
        y1 = h // 2 - box_size // 2
        x2 = w // 2 + box_size // 2
        y2 = h // 2 + box_size // 2

        crop = img[y1:y2, x1:x2]

        try:
            results = model.predict(
                source=crop,
                imgsz=64,
                verbose=False
            )

            probs = results[0].probs
            label = model.names[probs.top1]
            conf = probs.top1conf.item()

            text = f"{label} {conf:.2f}"

        except Exception:
            text = "Detecting..."

        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv2.putText(
            img,
            text,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            img,
            "Place ONE Braille cell inside box",
            (30, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(
    key="braille-realtime",
    video_processor_factory=BrailleProcessor,
    media_stream_constraints={
        "video": True,
        "audio": False
    },
    async_processing=True,
)
