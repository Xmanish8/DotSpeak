from ultralytics import YOLO
from pathlib import Path

BASE = Path(r"C:\Users\nites\Downloads\DotSpeak")

MODEL_PATH = BASE / "best.pt"
if not MODEL_PATH.exists():
    MODEL_PATH = BASE / "model" / "best.pt"

# find any image automatically
search_folder = BASE / "braille_dataset" / "images" / "val"

images = []
for ext in ["*.png", "*.jpg", "*.jpeg"]:
    images += list(search_folder.rglob(ext))

if len(images) == 0:
    print("No images found in:", search_folder)
    exit()

IMAGE_PATH = BASE / "mytest.jpg"

print("Using model:", MODEL_PATH)
print("Using image:", IMAGE_PATH)

model = YOLO(str(MODEL_PATH))

results = model.predict(
    source=str(IMAGE_PATH),
    imgsz=64,
    verbose=False
)

probs = results[0].probs
label = model.names[probs.top1]
conf = probs.top1conf.item()

print("Predicted Letter:", label)
print("Confidence:", round(conf, 3))