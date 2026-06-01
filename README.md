<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6C3483,50:8E44AD,100:2980B9&height=220&section=header&text=DotSpeak&fontSize=80&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Braille%20Vision%20AI%20%E2%80%94%20Reading%20Touch%2C%20Bridging%20Worlds&descAlignY=58&descSize=18" width="100%"/>

<br><br>
### Reading Touch, Speaking Knowledge

<img src="https://img.shields.io/badge/Hackathon-BrailleVision_2026-00c6ff?style=for-the-badge" />
<img src="https://img.shields.io/badge/Status-Final_Submission-success?style=for-the-badge" />
<img src="https://img.shields.io/badge/Model-YOLOv8--CLS-orange?style=for-the-badge" />
<img src="https://img.shields.io/badge/Deploy-Streamlit_Cloud-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white" />

🌐 **Live Demo:** https://dotspeak-bymrsn.streamlit.app/  
📦 **GitHub Repo:** https://github.com/Xmanish8/DotSpeak

</div>

---
 
<p align="center">
  <a href="https://youtu.be/GdrlQnaMx3Y">
    <img src="https://img.youtube.com/vi/GdrlQnaMx3Y/maxresdefault.jpg" width="800">
  </a>
</p>

<p align="center">
  🎥 Click the image above to watch the demo
</p>

---
## 🚀 Project Overview

DotSpeak is an AI-powered Braille recognition system that uses a camera or uploaded image to classify Braille characters and convert them into readable text and speech.

It supports:

- Real-time local webcam recognition
- Online Streamlit upload/camera snapshot demo
- A–Z Braille character classification
- Text and speech output
- Local judge verification

---

## 🎯 Problem Statement

Many people cannot read Braille, and dedicated Braille readers are often expensive or hardware-dependent. DotSpeak provides a software-based solution using a normal camera and AI model to recognize Braille characters.

---

## 🧠 System Architecture

```text
Braille Image / Camera
        ↓
Image Capture
        ↓
YOLOv8-CLS Model
        ↓
Predicted Letter
        ↓
Sentence Builder
        ↓
Text + Speech Output
````

---

## ✨ Features

| Feature            | Description                                |
| ------------------ | ------------------------------------------ |
| 🔤 A–Z Recognition | Recognizes Braille alphabet characters     |
| 📷 Camera Input    | Local webcam and Streamlit camera snapshot |
| 🖼️ Image Upload   | Upload cropped Braille character image     |
| 🧠 AI Model        | YOLOv8 classification model                |
| 🔊 Speech          | Local speech output using pyttsx3          |
| 🌐 Deployment      | Streamlit Cloud demo                       |
| ✅ Verification     | Judges can clone and test locally          |

---

## 📂 Repository Structure

```text
DotSpeak/
├── README.md
├── requirements.txt
├── .gitignore
├── app.py
├── BrailleVision_AI.py
├── sentence_reader.py
├── realtime_cam.py
├── test.py
├── best.pt
├── data.yaml
├── inference/
│   └── predict.py
├── training/
│   └── train.py or train.ipynb
├── sample_inputs/
│   └── sample Braille images
├── sample_outputs/
│   └── result screenshots
├── docs/
│   └── demo screenshots
└── braille_dataset/
    └── images/
        ├── train/
        └── val/
```

---

## ⚙️ Installation

```bash
git clone https://github.com/Xmanish8/DotSpeak.git
cd DotSpeak

conda create -n dotspeak python=3.10 -y
conda activate dotspeak

pip install -r requirements.txt
```

---

## 🖥️ Run Local Realtime App

```bash
python BrailleVision_AI.py
```

If camera does not open, change:

```python
cap = cv2.VideoCapture(0)
```

Try:

```python
cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture(2)
```

---

## 🌐 Run Streamlit App Locally

```bash
streamlit run app.py
```

Streamlit version supports:

* Upload image
* Browser camera snapshot
* Prediction
* Confidence score

---

## 🧪 Test Model

```bash
python test.py
```

or:

```bash
python inference/predict.py
```

---

## 🏋️ Training Command

```bash
yolo classify train model=yolov8n-cls.pt data=braille_dataset/images epochs=50 imgsz=64 batch=32
```

---

## 📊 Model Details

| Item       | Details               |
| ---------- | --------------------- |
| Model Type | YOLOv8 Classification |
| Model File | best.pt               |
| Input Size | 64×64                 |
| Classes    | A–Z                   |
| Framework  | Ultralytics + PyTorch |

---

## 📁 Dataset Details

| Item            | Details                          |
| --------------- | -------------------------------- |
| Dataset Type    | Braille character classification |
| Classes         | 26 classes                       |
| Class Names     | A to Z                           |
| Format          | Folder-based classification      |
| Train Path      | `braille_dataset/images/train`   |
| Validation Path | `braille_dataset/images/val`     |
| Annotation      | Folder names are labels          |

Example:

```text
braille_dataset/images/train/A/
braille_dataset/images/train/B/
braille_dataset/images/val/A/
braille_dataset/images/val/B/
```

---

## 🌍 Live Deployment

**Live Streamlit App:**

```text
https://dotspeak-bymrsn.streamlit.app/
```

**Important Note:**
The cloud version supports upload and browser camera snapshot. Full OpenCV realtime webcam runs locally using `BrailleVision_AI.py`.

---

## ✅ Judge Verification Guide

Judges can verify the project using:

```bash
git clone https://github.com/Xmanish8/DotSpeak.git
cd DotSpeak
pip install -r requirements.txt
python test.py
streamlit run app.py
```

For local realtime demo:

```bash
python BrailleVision_AI.py
```

---

## 📌 Submission Details

| Field             | Value                                                                            |
| ----------------- | -------------------------------------------------------------------------------- |
| Team Name         | DotSpeak Team                                                                    |
| Project Title     | DotSpeak — BrailleVision AI                                                      |
| GitHub Repository | [https://github.com/Xmanish8/DotSpeak](https://github.com/Xmanish8/DotSpeak)     |
| Live Demo         | [https://dotspeak-bymrsn.streamlit.app/](https://dotspeak-bymrsn.streamlit.app/) |
| Model Type        | YOLOv8 Classification                                                            |
| Tech Stack        | Python, YOLOv8, PyTorch, OpenCV, Streamlit                                       |
| Model Weights     | `best.pt`                                                                        |
| Training Code     | `training/`                                                                      |
| Inference Code    | `test.py`, `inference/predict.py`, `app.py`                                      |
| Sample Inputs     | `sample_inputs/`                                                                 |
| Sample Outputs    | `sample_outputs/`                                                                |

---

## 🤖 AI Tools Used

| Tool               | Purpose                                |
| ------------------ | -------------------------------------- |
| ChatGPT            | Debugging, documentation, code support |
| GitHub Copilot     | Code assistance                        |
| Ultralytics YOLOv8 | Classification model                   |
| PyTorch            | Model backend                          |

---

## ✅ Final Confirmation

We confirm that judges can clone, install, run, test, and verify this project locally using the provided GitHub repository, model weights, source code, and instructions.


*"Technology should be a bridge, not a barrier."*



<div align="center">

<br>

<table align="center">
<tr>
<td align="center"><b>🔤 A–Z Braille</b><br>Full alphabet support</td>
<td align="center"><b>⚡ GPU Accelerated</b><br>YOLOv8 + MobileNetV3</td>
<td align="center"><b>📊 Animated Output</b><br>Confidence Visualization</td>
<td align="center"><b>🌍 Social Impact</b><br>Accessibility Focused</td>
</tr>
</table>

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2980B9,50:8E44AD,100:6C3483&height=120&section=footer&text=Thank%20You%20For%20Reviewing%20DotSpeak&fontSize=22&fontColor=ffffff&animation=fadeIn" width="100%"/>

</div>
