# Module-12 Object Detection with OpenCV & TensorFlow[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1bwXSm513ES0e4PdQNQ4eAPomZTll1hPY?usp=sharing)

---

<p align="left">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&duration=2500&pause=500&color=00FF80&center=false&vCenter=false&width=600&lines=Load+and+Parse+COCO+Labels;Read+TensorFlow+Frozen+Graphs;Detect+Objects+Using+OpenCV+DNN;Visualize+Boxes+and+Labels+on+Images" alt="Typing SVG" />
</p>

---

A hands-on beginner-friendly project that demonstrates how to perform real-time object detection using **OpenCV's DNN module** and a **pre-trained TensorFlow model** (SSD MobileNet v2 on COCO dataset).

This notebook walks you through:
- Loading and parsing COCO class labels
- Reading model weights and configuration using TensorFlow's frozen graph
- Running object detection on an image
- Displaying predictions with bounding boxes and labels

---

##  Files Required

All files should be placed in the **same directory** as the notebook. Here's what you need:

- `coco_class_labels.txt` – COCO dataset class names
- `ssd_mobilenet_v2_coco_2018_03_29.pbtxt` – Configuration file for the model  
- `street.jpg` – Sample image to test detection (you can also use your own image)

###  Download Model Weights

You only need to download the model weights manually:

- `frozen_inference_graph.pb` – Pre-trained TensorFlow model weights  
  👉 [Download it here](https://github.com/TannerGilbert/Tensorflow-Object-Detection-API-train-custom-Mask-R-CNN-model/blob/master/frozen_inference_graph.pb)

Just drop this file in the same directory as your notebook and you're good to go.


##  Key Concepts Covered

- What is a DNN and why use `cv2.dnn`?
- How `blobFromImage` converts images for neural network processing
- Understanding outputs from the model (`classId`, `score`, bounding box coords)
- Tuning confidence thresholds for better detection accuracy
- Drawing labeled rectangles on detected objects

##  How to Use

1. Upload all required files
2. Run each code cell step-by-step
3. Customize detection thresholds or input images
4. Analyze the output — bounding boxes and labels will be shown inline

---

##  Model Used

- **Model**: SSD MobileNet v2  
- **Dataset**: COCO (Common Objects in Context)  
- **Framework**: TensorFlow + OpenCV DNN  
- [Model source (weights)](https://github.com/TannerGilbert/Tensorflow-Object-Detection-API-train-custom-Mask-R-CNN-model/blob/master/frozen_inference_graph.pb)

---

##  Beginner Tips

- The lower the threshold → the more sensitive the detection (may lead to false positives)
- You can swap out the model with any TensorFlow-supported architecture (as long as `.pb` and `.pbtxt` are provided)
- Make sure image color channels are handled properly (`BGR` vs `RGB`)

---

##  Navigation

[![➡️ Module 11](https://img.shields.io/badge/Module-11-000000?style=for-the-badge&logo=github&logoColor=00FF80)](https://github.com/aypy01/opencv/tree/main/11)
&nbsp;&nbsp;&nbsp;&nbsp;
[![➡️ Module 13](https://img.shields.io/badge/Module-13-000000?style=for-the-badge&logo=github&logoColor=00FF80)](https://github.com/aypy/opencv/tree/main/13)

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
![street](street.jpg)


