from ultralytics import YOLO
import cv2

model = YOLO("best.pt")

# Change this to your camera index
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    h, w = frame.shape[:2]

    size = 250

    x1 = w//2 - size//2
    y1 = h//2 - size//2
    x2 = w//2 + size//2
    y2 = h//2 + size//2

    crop = frame[y1:y2, x1:x2]

    results = model.predict(
        source=crop,
        imgsz=64,
        verbose=False
    )

    probs = results[0].probs

    label = model.names[probs.top1]
    conf = probs.top1conf.item()

    cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)

    cv2.putText(
        frame,
        f"{label} {conf:.2f}",
        (x1, y1-10),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.imshow("BrailleVision AI", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()