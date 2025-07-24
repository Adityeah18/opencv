#  Module 10: Image Tracking with OpenCV GOTURN

---
<p align="left">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&duration=2800&pause=400&color=00FF80&center=false&vCenter=false&width=510&lines=Module+10%3A+Image+Tracking+with+OpenCV;Deep+Learning+%2B+Traditional+Tracking;Real-Time+GOTURN+Based+Tracking;.caffemodel+%7C+DNN+%7C+cv2.TrackerGOTURN;From+Surveillance+to+Self-Driving+Cars" alt="Typing SVG" />
</p>

---

Object tracking is a crucial part of modern computer vision applications — from surveillance to self-driving cars. This module demonstrates object tracking using OpenCV’s GOTURN tracker — which combines traditional tracking with deep learning (via `.caffemodel`).

---

##  Important Notice Before You Begin

> ⚠️ **This module uses the GOTURN tracker**, which requires a `.caffemodel` and `.prototxt` file. These files are not included in this repository due to GitHub's 100 MB limit.

Instead, download the goturn.caffemodel from this public GitHub repo:
 [https://github.com/Mogball/goturn-files](https://github.com/Mogball/goturn-files)

Place the following two file in the same directory as your Python script:
- `goturn.caffemodel`


 *Colab may not support GOTURN out of the box due to model size and OpenCV build limitations. It’s highly recommended to run this module locally using `opencv-contrib-python`.*

---

##  Requirements

```bash
pip install opencv-python opencv-contrib-python
```

---

##  Files Included

- `10_object_tracking.py` – Python script version of this module  
- `race_car.mp4` – Sample input video (must be placed in the same directory)
- `goturn.prototxt`
---

## ⚙️ Requirements

- Python 3.x  
- OpenCV with contrib modules:
> ⚠️ **Note:**  
> This script uses legacy tracker APIs that may not work properly in Google Colab.  
> It's recommended to run this **locally** with the `opencv-contrib-python` package to avoid tracker initialization errors.

```bash
pip install opencv-python opencv-contrib-python
```

1. **Import Libraries**
   - `cv2`, `IPython.display.Video`

2. **Preview the Input Video**
   - Load video using `cv2.VideoCapture()`
   - Read and display frames to get familiar with content

3. **Read First Frame**
   - Capture the first frame to initialize tracking

4. **Define Drawing and Text Functions**
   - `draw_rectangle(frame, bbox)` for visualization
   - `text(frame, txt, org)` to overlay labels

5. **Select Tracker Type**
   - Choose from: `'BOOSTING'`, `'MIL'`, `'KCF'`, `'CSRT'`, `'TLD'`, `'MEDIANFLOW'`, `'MOSSE'`
   - Initialize tracker using `cv2.legacy.TrackerXXX_create()`

6. **Set Bounding Box for Target**
   - Either manually using `cv2.selectROI()` or hardcoded as `(x, y, w, h)`

7. **Initialize Tracker**
   - Use `tracker.init(frame, bbox)` to lock onto the object

8. **Setup Video Writer**
   - Create `cv2.VideoWriter()` object with frame size and codec

9. **Start Tracking Loop**
   - Read frame by frame from video
   - Use `tracker.update(frame)` to get new bounding box
   - Draw bounding box and add text
   - Write each frame to output video
   - Show live tracking using `cv2.imshow()`

10. **Cleanup**
    - Release all video handles and destroy OpenCV windows
    - Print output file path or tracking status

---
##  Navigation

[![➡️ Module 09](https://img.shields.io/badge/Module-09-000000?style=for-the-badge&logo=github&logoColor=00FF80)](https://github.com/aypy01/opencv/tree/main/09)
&nbsp;&nbsp;&nbsp;&nbsp;
[![➡️ Module 11](https://img.shields.io/badge/Module-11-000000?style=for-the-badge&logo=github&logoColor=00FF80)](https://github.com/aypy01/opencv/tree/main/11)

---

## Author
 <p align="left">
  Created and maintained by 
  <a href="https://github.com/aypy01" target="_blank">&nbsp Aaditya Yadav</a>&nbsp 
  <a href="https://github.com/aypy01" target="_blank">
    <img src="https://img.shields.io/badge/aypy01-000000?style=flat-square&logo=github&logoColor=00FF80" alt="GitHub Badge"/>
  </a>
</p>

</p>
<p align="left">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&duration=3000&pause=500&color=00FF80&center=false&vCenter=false&width=440&lines=Break+Things+First%2C+Understand+Later;Built+to+Debug%2C+Not+Repeat;Learning+What+Actually+Sticks;Code.+Observe.+Refine." alt="Typing SVG" />
</p>

---

##  License

This project is licensed under the [![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0).


