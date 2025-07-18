# 08_image_alignment.py

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load images
im1 = cv2.imread("form.jpg", cv2.IMREAD_COLOR)
im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2RGB)
im2 = cv2.imread("scanned-form.jpg", cv2.IMREAD_COLOR)
im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2RGB)

# Step 2: Convert to grayscale
im1_gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
im2_gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

# Step 3: Detect ORB keypoints and descriptors
MAX_NUM_FEATURES = 500
orb = cv2.ORB_create(MAX_NUM_FEATURES)
keypoints1, descriptors1 = orb.detectAndCompute(im1_gray, None)
keypoints2, descriptors2 = orb.detectAndCompute(im2_gray, None)

# Step 4: Match features
matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
matches = list(matcher.match(descriptors1, descriptors2))
matches.sort(key=lambda x: x.distance)
numGoodMatches = int(len(matches) * 0.1)
matches = matches[:numGoodMatches]

# Step 5: Draw matches (optional visualization)
im_matches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)
plt.figure(figsize=[40,10])
plt.imshow(im_matches)
plt.axis('off')
plt.title("Matched Keypoints")
plt.show()

# Step 6: Extract match point locations
points1 = np.zeros((len(matches), 2), dtype=np.float32)
points2 = np.zeros((len(matches), 2), dtype=np.float32)

for i, match in enumerate(matches):
    points1[i, :] = keypoints1[match.queryIdx].pt
    points2[i, :] = keypoints2[match.trainIdx].pt

# Step 7: Compute homography and warp
h, mask = cv2.findHomography(points2, points1, cv2.RANSAC)
height, width, channels = im1.shape
im2_reg = cv2.warpPerspective(im2, h, (width, height))

# Final output
plt.figure(figsize=[20,10])
plt.subplot(121); plt.imshow(im1); plt.axis('off'); plt.title("Original Form")
plt.subplot(122); plt.imshow(im2_reg); plt.axis('off'); plt.title("Aligned Scanned Form")
plt.show()
