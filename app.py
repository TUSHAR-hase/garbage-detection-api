from flask import Flask, request, jsonify
from ultralytics import YOLO
import cv2
import numpy as np
import base64
import os

app = Flask(__name__)

# Load trained YOLO model

model = YOLO("best.pt")

# ---------- 1️⃣ Image Upload Detection ----------

@app.route("/detect-image", methods=["POST"])
def detect_image():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"})

    file = request.files["image"]

    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

    results = model(img,conf=0.1)

    detections = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls)
            conf = float(box.conf)
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            detections.append({
                "class": model.names[cls],
                "confidence": conf,
                "box": [x1, y1, x2, y2]
            })

    return jsonify(detections)

# ---------- 2️⃣ Live Camera Frame Detection ----------

@app.route("/detect-frame", methods=["POST"])
def detect_frame():
    data = request.json

    img_data = base64.b64decode(data["image"])

    np_arr = np.frombuffer(img_data, np.uint8)

    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    results = model(frame,conf=0.1)

    detections = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls)
            conf = float(box.conf)
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            detections.append({
                "class": model.names[cls],
                "confidence": conf,
                "box": [x1, y1, x2, y2]
            })

    return jsonify(detections)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
