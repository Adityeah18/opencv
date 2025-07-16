# Module 07 – Image Filtering & Edge Detection

 **Filename:** `07_camera_filters.py`  

---

##  What This Script Does

This Python script accesses your webcam or video file and lets you apply different filters in real time using **OpenCV**.  
It includes:

- Preview (raw feed)
- Blur (mean filter)
- Canny Edge Detection
- Shi-Tomasi Feature Detection (corner points)

---

## 🔄 Filter Switching – Hotkeys

| Key Press | Mode                      | Description                                       |
|-----------|---------------------------|---------------------------------------------------|
| `P`       | Preview                   | Just shows the camera feed                       |
| `B`       | Blur                      | Applies a mean filter (cv2.blur)                 |
| `C`       | Canny Edge Detection      | Detects edges using gradients                    |
| `F`       | Feature Detection         | Detects corners using Shi-Tomasi method          |
| `Q` / `Esc` | Quit                    | Closes the window                                |

---

##  Key Learnings

###  **Why is feature detection done in grayscale?**
Feature detectors like Shi-Tomasi rely on **pixel intensity gradients**, not color. So:
- Frame is converted using `cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)`
- Detection is done on this grayscale image
- But **drawing is done on the color image**, so the circles show up in color.

###  **Why were words detected better than faces?**
- Text has **sharp corners and high contrast**
- Faces have **soft gradients** with less contrast (especially under bad lighting)
- Feature detection prefers hard edges and intensity jumps, so text wins

###  **Why were circles few and large?**
- The **number of circles** is controlled by:
  - `qualityLevel`: lower values (e.g. `0.01`) = more features
  - `minDistance`: lower values = more features allowed closer together
- The **circle size** is drawn manually:
  ```python
  cv2.circle(result, (x, y), 10, (0, 255, 0), 1)
## 🔗 Navigation

[![⬅️ Module 06](https://img.shields.io/badge/Module-06-blue?style=for-the-badge&logo=github)](https://github.com/Adityeah18/opencv/tree/main/06)
&nbsp;&nbsp;&nbsp;
[![➡️ Module 08](https://img.shields.io/badge/Module-08-blue?style=for-the-badge&logo=github)](https://github.com/Adityeah18/opencv/tree/main/08)

---

## 🧑‍💻 Author

**Aaditya**  
[GitHub Profile](https://github.com/Adityeah18)

---

## 📜 License

This project is licensed under the [![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0).

