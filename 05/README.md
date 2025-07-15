# 05 – Accessing Camera using OpenCV 🎥


This module demonstrates how to **access your system camera** or a **video file** using `OpenCV` in Python.

The script is designed to:
- Open your **default webcam** (or any other specified camera index)
- Accept a **video file path** as a command-line argument
- Display the live/video feed in a resizable OpenCV window
- Exit when `Esc` key is pressed

---

## 🧠 What You'll Learn
- How to work with `cv2.VideoCapture`
- Difference between webcam index and file input
- How to handle command-line arguments via `sys.argv`
- How to cleanly exit and release camera resources

---

## 🐍 Python File
📄 [`camera.py`](camera.py)

---

## 🧪 Usage Examples

```bash
# Open default webcam (index 0)
python camera.py

# Open a different camera (e.g., external webcam)
python camera.py 1

# Open a video file
python camera.py video.mp4

