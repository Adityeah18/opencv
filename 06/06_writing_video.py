# 06_writing_video.py

import cv2

# Load input video
src_vid = './race_car.mp4'
video = cv2.VideoCapture(src_vid)

if not video.isOpened():
    print("Error: Could not open video.")
    exit()

# Read first frame (optional, for checking video)
ret, frame = video.read()
if not ret:
    print("Error: Could not read first frame.")
    exit()

# Get frame dimensions (convert from float to int)
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Initialize VideoWriter objects for AVI and MP4 formats
out_avi = cv2.VideoWriter(
    'race_ca_out.avi',
    cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
    10,
    (frame_width, frame_height)
)

out_mp4 = cv2.VideoWriter(
    'race_car_out.mp4',
    cv2.VideoWriter_fourcc(*'mp4v'),
    10,
    (frame_width, frame_height)
)

# Reset video to beginning after reading first frame
video.set(cv2.CAP_PROP_POS_FRAMES, 0)

# Write each frame to output files
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    out_avi.write(frame)
    out_mp4.write(frame)

# Release resources
video.release()
out_avi.release()
out_mp4.release()
