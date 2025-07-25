# 12_object_detection.py

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load COCO Class Labels
with open('coco_class_labels.txt') as file:
    labels = file.read().strip().split('\n')

# Load the pre-trained model (weights and config)
net = cv2.dnn.readNetFromTensorflow(
    'frozen_inference_graph.pb',
    'ssd_mobilenet_v2_coco_2018_03_29.pbtxt'
)

# Detect objects in an image using the loaded model
def detect(net, img):
    blob = cv2.dnn.blobFromImage(
        img, scalefactor=1, size=(300, 300),
        mean=(0, 0, 0), swapRB=True, crop=False
    )
    net.setInput(blob)
    return net.forward()

# Display text label above detected object
def display_text(img, text, x, y):
    textSize = cv2.getTextSize(text, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8, thickness=1)
    dim = textSize[0]
    baseline = textSize[1]

    cv2.rectangle(
        img,
        (x, y - dim[1] - baseline),
        (x + dim[0], y + baseline),
        (125, 0, 125),
        cv2.FILLED
    )

    cv2.putText(
        img, text, (x, y - 5),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=0.7,
        color=(0, 255, 0),
        thickness=2
    )

# Draw bounding boxes and display labels
def display_objects(img, objects, threshold=0.3):
    rows, cols = img.shape[:2]

    for i in range(objects.shape[2]):
        classId = int(objects[0, 0, i, 1])
        score = float(objects[0, 0, i, 2])

        x = int(objects[0, 0, i, 3] * cols)
        y = int(objects[0, 0, i, 4] * rows)
        w = int(objects[0, 0, i, 5] * cols - x)
        h = int(objects[0, 0, i, 6] * rows - y)

        if score > threshold:
            display_text(img, labels[classId], x, y)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)

    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(30, 10))
    plt.imshow(rgb_img)
    plt.axis('off')
    plt.show()

# Sample Image 1
img_1 = cv2.imread('street.jpg')
detected_1 = detect(net, img_1)
display_objects(img_1, detected_1)

# Sample Image 2 (Lower threshold)
img_2 = cv2.imread('giraffe-zebra.jpg')
detected_2 = detect(net, img_2)
display_objects(img_2, detected_2, threshold=0.1)

# Sample Image 3
img_3 = cv2.imread('baseball.jpg')
detected_3 = detect(net, img_3)
display_objects(img_3, detected_3)

# Sample Image 4 (High threshold for false positive reduction)
img_4 = cv2.imread('soccer.jpg')
detected_4 = detect(net, img_4)
display_objects(img_4, detected_4, threshold=0.8)

# End of script
