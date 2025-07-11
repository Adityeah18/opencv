# 04_image_enhancement.py
# Author: Aaditya
# License: Apache 2.0

import cv2
import numpy as np

# 1. Load and convert image from BGR to RGB
bgr_image = cv2.imread("New_Zealand_Coast.jpg")
rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

# 2. Brightness adjustment
brightness = np.ones(rgb_image.shape, dtype='uint8') * 50
rgb_image_bright = cv2.add(rgb_image, brightness)
rgb_image_dark = cv2.subtract(rgb_image, brightness)

# 3. Contrast adjustment (without clipping)
contrast_bright = np.ones(rgb_image.shape) * 1.2
contrast_dark = np.ones(rgb_image.shape) * 0.5
rgb_image_contrast_bright = cv2.multiply(np.float64(rgb_image), contrast_bright).astype(np.uint8)
rgb_image_contrast_dark = cv2.multiply(np.float64(rgb_image), contrast_dark).astype(np.uint8)

# 4. Contrast adjustment (with clipping)
rgb_image_contrast_bright_clip = np.clip(
    cv2.multiply(np.float64(rgb_image), contrast_bright), 0, 255
).astype(np.uint8)

# 5. Thresholding (Global)
src_image = cv2.imread("building-windows.jpg", cv2.IMREAD_GRAYSCALE)
_, threshold_image = cv2.threshold(src_image, 100, 255, cv2.THRESH_BINARY)

# 6. Adaptive thresholding
music_sheet_img = cv2.imread("Piano_Sheet_Music.png", cv2.IMREAD_GRAYSCALE)
_, music_sheet_thresh = cv2.threshold(music_sheet_img, 50, 255, cv2.THRESH_BINARY)
adaptive_thresh_img = cv2.adaptiveThreshold(
    music_sheet_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7
)

# 7. Bitwise operations with shape masks
rectangle_img = cv2.imread("rectangle.jpg", cv2.IMREAD_GRAYSCALE)
circle_img = cv2.imread("circle.jpg", cv2.IMREAD_GRAYSCALE)
and_mask = cv2.bitwise_and(rectangle_img, circle_img)
or_mask = cv2.bitwise_or(rectangle_img, circle_img)
xor_mask = cv2.bitwise_xor(rectangle_img, circle_img)

# 8. Bitwise operation application – Coca-Cola on checkerboard
coke_img_rgb = cv2.cvtColor(cv2.imread("coca-cola-logo.png"), cv2.COLOR_BGR2RGB)
background_img_rgb = cv2.cvtColor(cv2.imread("checkerboard_color.png"), cv2.COLOR_BGR2RGB)
background_img_rgb_resized = cv2.resize(background_img_rgb, (700, 700))

# Create binary mask and its inverse
img_gray = cv2.cvtColor(coke_img_rgb, cv2.COLOR_RGB2GRAY)
_, img_mask = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
img_mask_inv = cv2.bitwise_not(img_mask)

# Mask background and foreground
img_background = cv2.bitwise_and(background_img_rgb_resized, background_img_rgb_resized, mask=img_mask)
img_foreground = cv2.bitwise_and(coke_img_rgb, coke_img_rgb, mask=img_mask_inv)

# Combine foreground and background
result = cv2.add(img_background, img_foreground)
cv2.imwrite("logo_final.png", result[:, :, ::-1])
