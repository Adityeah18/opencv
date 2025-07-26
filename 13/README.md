#  Module 13: Human Pose Estimation with OpenCV  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1jb_7r_Eo1CuuwKgF6A1nGujSBO-qRrk4?usp=sharing)

---
<p align="left">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&duration=2700&pause=400&color=00FF80&center=false&vCenter=false&width=520&lines=What+Pose+Estimation+Really+Is;Preprocessing+Images+with+blobFromImage();Using+OpenCV+with+Caffe+Models;Extracting+Confidence+Maps;Drawing+Human+Skeletons+with+Code" alt="Typing SVG" />
</p>


---
This module covers 2D human pose estimation using OpenCV's deep learning module (`cv2.dnn`) and a pre-trained Caffe-based OpenPose model. It detects 15 key body joints and draws a skeleton over the input image.

This is the final standalone module before jumping into project-based learning.

---

##  What This Repo Contains

- `pose_estimation.py` — full Python script version of this module
- A Colab notebook link to run it interactively (below)
- Sample image(s) to test the model
- Cleanly structured code with inline comments and markdown explanations

Everything needed is included in this repo **except** the Caffe model file — linked below.



##  What You'll Learn

- What pose estimation is and how it's applied in computer vision
- How to preprocess images using `cv2.dnn.blobFromImage()`
- How to use OpenCV with a pre-trained Caffe model
- How to extract and threshold confidence maps
- How to connect keypoints into a human skeleton overlay

---

##  Model Download

Download the required pre-trained weights here:

**[pose_iter_160000.caffemodel](https://huggingface.co/camenduru/openpose/resolve/f4a22b0e6fa2a4a2b1e2d50bd589e8bb11ebea7c/pose_iter_160000.caffemodel)**

> You only need this file — the rest of the setup (including `.prototxt`) is included.

---
##  Navigation

[![➡️ Module 12](https://img.shields.io/badge/Module-12-000000?style=for-the-badge&logo=github&logoColor=00FF80)](https://github.com/aypy01/opencv/tree/main/12)
&nbsp;&nbsp;&nbsp;&nbsp;
[![➡️ Credit ](https://img.shields.io/badge/Credits-000000?style=for-the-badge&logo=github&logoColor=00FF80)](https://github.com/aypy01/opencv/tree/main/01)
&nbsp;&nbsp;&nbsp;&nbsp;


##  End of Line

That’s it.  
Not just the end of Module 13  but the **final checkpoint** of the whole OpenCV course.

We began with raw pixels, blurred some faces, warped a few perspectives, drew stickmen on still images, and learned how to make machines see  or at least pretend to.

And now? You’re not reading a tutorial anymore.  
You’re standing at the edge, looking at *what you can build next*.

> “Culture shouldn't exist only for those who can afford it.”  
> — Hakita, Developer of ULTRAKILL

OpenCV, these notebooks, the models, the code  it’s all here because people shared what they knew.  
Open source isn’t just about free code  it's about **lowering the entry barriers**. For devs like me. Like you. For anyone with more curiosity than compute.

Because **not everything has to be monetized**, and not every lesson needs a paywall.  
Helping others climb is still the best kind of version control.

See you beyond the matrix.  
— Aaditya Yadav 🟢🟣

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

