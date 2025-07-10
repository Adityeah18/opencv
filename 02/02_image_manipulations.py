import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 1. Load grayscale image
cb_img = cv2.imread('checkerboard_18x18.png', 0)
plt.imshow(cb_img, cmap='gray')
plt.title("Grayscale Image")
plt.show()

# 2. Access and modify pixels
print("Pixel (0,0):", cb_img[0, 0])
print("Pixel (6,5):", cb_img[6, 5])

cb_img_mod = cb_img.copy()
cb_img_mod[2, 2] = 255
cb_img_mod[2, 3] = 250
cb_img_mod[3, 2] = 200
cb_img_mod[3, 3] = 150
plt.imshow(cb_img_mod, cmap='gray')
plt.title("Modified Pixels")
plt.show()

# 3. Load color image and convert to RGB
img_color = cv2.imread("New_Zealand_Boat.jpg", cv2.IMREAD_COLOR)
img_rgb = img_color[:, :, ::-1]
plt.imshow(img_rgb)
plt.title("Original RGB Image")
plt.show()

# 4. Crop region
cropped = img_rgb[200:400, 300:600]
plt.imshow(cropped)
plt.title("Cropped Region")
plt.show()

# 5. Resize (Method 1 - Scale factor)
resized_scale = cv2.resize(cropped, None, fx=3, fy=3)
plt.imshow(resized_scale)
plt.title("Resized (Scale Factor)")
plt.show()

# 6. Resize (Method 2 - Specific dimensions)
resized_dims = cv2.resize(cropped, dsize=(200, 300), interpolation=cv2.INTER_AREA)
plt.imshow(resized_dims)
plt.title("Resized (Dimensions)")
plt.show()

# 7. Resize with aspect ratio
new_width = 200
aspect_ratio = new_width / cropped.shape[1]
new_height = int(cropped.shape[0] * aspect_ratio)
resized_aspect = cv2.resize(cropped, (new_width, new_height))
plt.imshow(resized_aspect)
plt.title("Resized (Aspect Ratio Preserved)")
plt.show()

# 8. Flipping
flip_vert = cv2.flip(img_rgb, 0)
flip_horz = cv2.flip(img_rgb, 1)
flip_both = cv2.flip(img_rgb, -1)

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1); plt.imshow(flip_vert); plt.title("Vertical Flip")
plt.subplot(1, 3, 2); plt.imshow(flip_horz); plt.title("Horizontal Flip")
plt.subplot(1, 3, 3); plt.imshow(flip_both); plt.title("Flip Both")
plt.tight_layout()
plt.show()

# 9. Saving images
cv2.imwrite("vertical_flip.png", flip_vert[:, :, ::-1])
cv2.imwrite("cropped_region.png", cropped[:, :, ::-1])
cv2.imwrite("resized_aspect_ratio.png", resized_aspect[:, :, ::-1])
cv2.imwrite("resized_image.png", resized_dims[:, :, ::-1])
