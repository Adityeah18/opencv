
"""
09_panorama.py

Panorama Stitching Using OpenCV

This script demonstrates automatic panorama creation by stitching multiple overlapping images using OpenCV.
"""

# Import required libraries
import cv2
import matplotlib.pyplot as plt
import math
import glob

# Step 1: Load and prepare images from 'boat/' folder
image_files = glob.glob('boat/*')
image_files.sort()

images = []
for file in image_files:
    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    images.append(img)

image_count = len(images)

# Step 2: Display loaded images in a grid
plt.figure(figsize=[30, 10])
cols = 3
rows = math.ceil(image_count / cols)

for i in range(image_count):
    plt.subplot(rows, cols, i + 1)
    plt.axis('off')
    plt.title(i)
    plt.imshow(images[i])

# Step 3: Stitch images into a panorama using OpenCV
stitcher = cv2.Stitcher_create()
status, panorama = stitcher.stitch(images)

if status == 0:
    plt.figure(figsize=[30, 10])
    plt.axis('off')
    plt.title("Panorama", loc='center')
    plt.imshow(panorama)
else:
    print(f"[Error] Stitching failed with status code: {status}")
