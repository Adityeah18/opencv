#  08_image_alignment    [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1J6z4CvhrfaSn6wbyiMIIl5A2uE3aLymB?usp=sharing)

This notebook demonstrates how to align a scanned document image with its original using **Homography** in OpenCV.

Homography is a powerful tool used to correct perspective distortion — useful in scenarios like scanned forms, camera-skewed photos, or flat document alignment.



---

##  Files Included

- `08_image_alignment.ipynb` – Main Colab notebook
- `08_image_alignment.py` – Python script version of the notebook
- `form.jpg` – The original reference image
- `scanned-form.jpg` – The misaligned (scanned) version to be corrected

---

##  What You’ll Learn

- How to use **ORB** to detect and describe key features
- Matching features using **Hamming distance**
- Filtering good matches and estimating a **Homography matrix**
- Warping the scanned image to align with the reference

---

##  No Deep Theory Needed

This notebook is beginner-friendly and focuses on practical implementation over heavy math. If you're new to computer vision, this is a great place to start understanding how real-world image alignment works.

---

##  Example Use Cases

- Digitizing old documents
- Aligning images before OCR
- Augmented reality overlays
- Perspective correction in photos

---

##  Requirements

- Python 3.x
- OpenCV
- NumPy
- Matplotlib

You can run everything on Colab without installing anything locally.


---

## 🧑‍💻 Author

**Aaditya**  
[GitHub Profile](https://github.com/Adityeah18)

---

## 📜 License

This project is licensed under the [![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0).


