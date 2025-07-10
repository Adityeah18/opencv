import cv2
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Image

# Load the image (even grayscale-looking images should be loaded in color for colored annotations)
image = cv2.imread("Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)

# Draw a line: from (200, 100) to (400, 100)
line_img = image.copy()
cv2.line(line_img, (200, 100), (400, 100), (0, 255, 255), thickness=5, lineType=cv2.LINE_AA)

# Draw a circle: center (920, 525), radius 100
image_circle = image.copy()
cv2.circle(image_circle, (920, 525), 100, (0, 0, 255), thickness=5, lineType=cv2.LINE_AA)

# Draw a rectangle: from top-left (500, 100) to bottom-right (700, 650)
image_rectangle = image.copy()
cv2.rectangle(image_rectangle, (500, 100), (700, 650), (255, 0, 255), thickness=5)

# Add text to the image
image_text = image.copy()
cv2.putText(image_text,
            text="Apollo 11 Saturn V Launch, July 16, 1969",
            org=(200, 700),
            fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=2.3,
            color=(0, 255, 0),
            thickness=3)

# Save all annotated versions
cv2.imwrite("annotated_line.jpg", line_img)
cv2.imwrite("annotated_circle.jpg", image_circle)
cv2.imwrite("annotated_rectangle.jpg", image_rectangle)
cv2.imwrite("annotated_text.jpg", image_text)

# Display one of the saved images (for notebook users)
Image(filename="annotated_text.jpg")
