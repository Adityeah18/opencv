# Step 1: Import Required Libraries
import cv2
import matplotlib.pyplot as plt
import numpy

# Step 2: Load and Convert Input Image
image = cv2.imread('Tiger_Woods_crop.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.axis('off')

# Step 3: Load Pre-trained Caffe Model (Download model first!)
# Prototxt defines the network structure
# Caffe model contains the trained weights
net = cv2.dnn.readNetFromCaffe(
    'pose_deploy_linevec_faster_4_stages.prototxt',
    'pose_iter_160000.caffemodel'  # Download from HuggingFace or CMU OpenPose page
)

# Step 4: Define Keypoints and Pose Pairs
n_points = 15
pose_pairs = [
    [0, 1], [1, 2], [2, 3], [3, 4],
    [1, 5], [5, 6], [6, 7],
    [1, 14], [14, 8], [8, 9], [9, 10],
    [14, 11], [11, 12], [12, 13]
]

# Step 5: Get Image Dimensions
width = image.shape[0]
height = image.shape[1]

# Step 6: Create Input Blob for the Model
blob = cv2.dnn.blobFromImage(
    image,
    scalefactor=1/255,
    size=(368, 368),
    mean=(0, 0, 0),
    swapRB=True,
    crop=False
)
net.setInput(blob)

# Step 7: Forward Pass to Get Confidence Maps
output = net.forward()

# Visualize Confidence Maps
plt.figure(figsize=(20, 5))
for i in range(n_points):
    map = output[0, i, :, :]
    display_map = cv2.resize(map, dsize=(width, height), interpolation=cv2.INTER_LINEAR)
    plt.subplot(2, 8, i + 1)
    plt.axis('off')
    plt.imshow(display_map, cmap='jet')

# Step 8: Extract Keypoints from Confidence Maps
scale_X = width / output.shape[3]
scale_y = height / output.shape[2]

threshold = 0.1
points = []

for i in range(n_points):
    proba_map = output[0, i, :, :]
    min_val, prob, min_loc, point = cv2.minMaxLoc(proba_map)

    x = scale_X * point[0]
    y = scale_y * point[1]

    if prob > threshold:
        points.append((int(x), int(y)))
    else:
        points.append(None)

# Step 9: Draw the Skeleton on Top of the Image
skeleton = image.copy()
for pair in pose_pairs:
    part_a = pair[0]
    part_b = pair[1]

    if points[part_a] and points[part_b]:
        cv2.line(skeleton, points[part_a], points[part_b], color=(255, 255, 0), thickness=2, lineType=cv2.LINE_AA)
        cv2.circle(skeleton, points[part_a], radius=6, color=(255, 0, 0), thickness=-2, lineType=cv2.FILLED)

# Display Final Pose Skeleton
plt.figure(figsize=(10, 10))
plt.imshow(skeleton, aspect='equal')
plt.axis('off')
plt.title("Pose Skeleton")
plt.show()

# --- Final Signoff ---

'''

> “Culture shouldn't exist only for those who can afford it.”  
> — Hakita (ULTRAKILL)

Open source is the way out of that. Not everything should cost. Not every idea should stay behind a paywall.

So fork this, break it, improve it, and share your version.


Until then:
Stay real. Stay weird.
And above all — *let no algorithm predict your story*.

— Aaditya Yadav 🟢🟣
'''
