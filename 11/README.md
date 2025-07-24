# Module-11 Face Detection 
---

<p align="left">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&duration=2500&pause=500&color=00FF80&center=false&vCenter=false&width=420&lines=Real-Time+Face+Detection;Deep+Learning+with+OpenCV+DNN;SSD+Model+%7C+Caffe+Based;No+Training%2C+Just+Inference;High+Confidence+Recognition" alt="Typing SVG" />
</p>


---

This project uses OpenCV's Deep Neural Network (DNN) module to detect faces in real-time from your webcam using a **pre-trained Caffe model**.

No need to train — just plug and run!  
Supports **high confidence face detection**, with bounding boxes and live inference time display.

---

## 📦 Files Used

- `deploy.prototxt`: Model architecture for the SSD face detector.
- `res10_300x300_ssd_iter_140000_fp16.caffemodel`: Pre-trained weights (300×300 SSD).
- `face_detection.py`: Main Python script to capture webcam input and perform detection.

---

## 🔧 How It Works

1. Frame is captured from the webcam.
2. Frame is flipped horizontally (mirror-like effect).
3. It's resized to **300×300** and converted to a blob for the DNN.
4. Blob is passed through the SSD model.
5. Output detections are filtered using a **confidence threshold**.
6. Bounding boxes and confidence values are drawn on the original frame.
7. Inference time is displayed for performance analysis.

---

## ⚙️ Setup

### 1. Install dependencies
```bash
pip install opencv-python
```


---
##  Navigation

[![➡️ Module 10](https://img.shields.io/badge/Module-10-000000?style=for-the-badge&logo=github&logoColor=00FF80)](https://github.com/Adityeah18/opencv/tree/main/10)
&nbsp;&nbsp;&nbsp;&nbsp;
[![➡️ Module 12](https://img.shields.io/badge/Module-12-000000?style=for-the-badge&logo=github&logoColor=00FF80)](https://github.com/Adityeah18/opencv/tree/main/12)

---

##  Author
<p align="left">
  <a href="https://github.com/aypy01" target="_blank">
    <img src="https://img.shields.io/badge/aypy01-000000?style=flat-square&logo=github&logoColor=00FF80" />
  </a>
</p>

<p align="left">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&duration=3000&pause=500&color=00FF80&center=false&vCenter=false&width=440&lines=Break+Things+First%2C+Understand+Later;Built+to+Debug%2C+Not+Repeat;Learning+What+Actually+Sticks;Code.+Observe.+Refine." alt="Typing SVG" />
</p>


---

##  License

This project is licensed under the [![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0).
rg/licenses/Apache-2.0).

