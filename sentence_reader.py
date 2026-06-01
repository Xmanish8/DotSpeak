from ultralytics import YOLO
import cv2
import pyttsx3
import time
from pathlib import Path

BASE = Path(r"C:\Users\nites\Downloads\DotSpeak")

MODEL_PATH = BASE / "best.pt"
if not MODEL_PATH.exists():
    MODEL_PATH = BASE / "model" / "best.pt"

model = YOLO(str(MODEL_PATH))

engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

cap = cv2.VideoCapture(1)   # change 0 / 1 / 2 if camera not open

if not cap.isOpened():
    print("Camera not opening. Try cap = cv2.VideoCapture(0)")
    exit()

CELL_COUNT = 5          # change according to letters
CONF_LIMIT = 0.80       # only accept confident letters

last_spoken = ""
last_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]

    roi_x1 = 100
    roi_y1 = h // 2 - 120
    roi_x2 = w - 100
    roi_y2 = h // 2 + 120

    roi = frame[roi_y1:roi_y2, roi_x1:roi_x2]

    cell_w = roi.shape[1] // CELL_COUNT
    letters = []

    for i in range(CELL_COUNT):
        x1 = i * cell_w
        x2 = (i + 1) * cell_w

        cell = roi[:, x1:x2]

        results = model.predict(
            source=cell,
            imgsz=64,
            verbose=False
        )

        probs = results[0].probs
        label = model.names[probs.top1]
        conf = probs.top1conf.item()

        if conf >= CONF_LIMIT:
            letters.append(label)

        color = (0, 255, 0) if conf >= CONF_LIMIT else (0, 0, 255)

        cv2.rectangle(
            frame,
            (roi_x1 + x1, roi_y1),
            (roi_x1 + x2, roi_y2),
            color,
            2
        )

        cv2.putText(
            frame,
            f"{label} {conf:.2f}",
            (roi_x1 + x1 + 5, roi_y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            color,
            2
        )

    sentence = "".join(letters)

    cv2.putText(
        frame,
        "Sentence: " + sentence,
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0, 255, 255),
        3
    )

    cv2.putText(
        frame,
        "Press S to Speak | A Auto Speak | Q Quit",
        (30, 95),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.imshow("BrailleVision AI Sentence Reader", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s") and len(sentence) > 0:
        print("Speaking:", sentence)
        engine.say(sentence)
        engine.runAndWait()

    if key == ord("a"):
        if sentence != last_spoken and len(sentence) > 0 and time.time() - last_time > 3:
            print("Auto Speaking:", sentence)
            engine.say(sentence)
            engine.runAndWait()
            last_spoken = sentence
            last_time = time.time()

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()