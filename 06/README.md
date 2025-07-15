# Module 06 – Writing Video with OpenCV   [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/10_raCfvwdSFa1DfJ_M6n8ySJfqkVJyjW?usp=sharing)


This module demonstrates how to write video files using OpenCV by capturing frames from an existing video and saving them in `.avi` and `.mp4` formats.

## Overview

The notebook walks through the following steps:

- Initializing a `VideoWriter` object with appropriate parameters (filename, codec, frame rate, frame size).
- Capturing frames from a video file.
- Writing each frame into new output video files.
- Releasing all resources to finalize the video files properly.

## File Structure

- `06_writing_video.ipynb` – Main Colab-compatible notebook with code and explanations.
- `race_car_out.mp4` – Output video file saved in MP4 format (available in the same directory after running the notebook).
- `race_ca_out.avi` – Output video file saved in AVI format.
- `06_writing_video.py` – Python script version of the notebook.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- A sample input video (`race_car.mp4` or similar) placed in the same directory for reading frames.

## How It Works

1. The input video is read frame by frame using `cv2.VideoCapture`.
2. Each frame is written to both `.avi` and `.mp4` formats using separate `cv2.VideoWriter` objects.
3. After all frames are processed, `release()` is called to finalize and save the videos.


## 🔗 Navigation

[![⬅️ Module 05](https://img.shields.io/badge/Module-05-blue?style=for-the-badge&logo=github)](https://github.com/Adityeah18/opencv/tree/main/05)
&nbsp;&nbsp;&nbsp;
[![➡️ Module 07](https://img.shields.io/badge/Module-07-blue?style=for-the-badge&logo=github)](https://github.com/Adityeah18/opencv/tree/main/07)

---

## 🧑‍💻 Author

**Aaditya**  
[GitHub Profile](https://github.com/Adityeah18)

---

## 📜 License

This project is licensed under the [![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0).


