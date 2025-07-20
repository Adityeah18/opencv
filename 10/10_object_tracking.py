#Tracking object starts with intialt object detectio then to tracking that object in futher frames
#There are various Tracker cases in open cv.
#Hightlight Medianflow: good for slow motions, Mosse= Fastest tracking

import cv2
import sys

#Reading the Video

input_video = cv2.VideoCapture("race_car.mp4")
ret, frame = input_video.read() #CV2.videocapture read

if not ret:
    sys.exit("ERROR : Could not open the video.")

#Trackers
tracker_types = ['BOOSTING', 'MIL', 'KCF', 'CSRT', 'TLD', 'MEDIANFLOW', 'MOSSE', 'GOTURN']
# Change index here to switch tracker
tracker_type = tracker_types[7]

if tracker_type == 'BOOSTING':
    tracker = cv2.legacy.TrackerBoosting_create()
elif tracker_type == 'MIL':
    tracker = cv2.legacy.TrackerMIL_create()
elif tracker_type == 'KCF':
    tracker = cv2.legacy.TrackerKCF_create()
elif tracker_type == 'CSRT':
    tracker = cv2.legacy.TrackerCSRT_create()
elif tracker_type == 'TLD':
    tracker = cv2.legacy.TrackerTLD_create()
elif tracker_type == 'MEDIANFLOW':
    tracker = cv2.legacy.TrackerMedianFlow_create()
elif tracker_type == 'MOSSE':
    tracker = cv2.legacy.TrackerMOSSE_create()
elif tracker_type == 'GOTURN':
    tracker = cv2.TrackerGOTURN_create()
else:
    raise ValueError(f"Unknown tracker type: {tracker_type}")

#Bounding box
#Manual selection of obejct from 1st frame
#bbox=cv2.selectROI('Tracker',frame,showCrosshair=True)

#Co-ordinate selection of object
bbox = (1300, 405, 160, 120) # x, y, width, height

#Initialising the trackers
tracker.init(frame, bbox)

#Frame by Frame Traking
while True:
    ret, frame = input_video.read()
    if not ret:
        break

    #updating the frame by frame with tracker associated which initialised
    ok, bbox = tracker.update(frame)
    #Making Reactangle aroung the bound box co-ordinate for visual representation
    if ok:
        pt1 = (int(bbox[0]), int(bbox[1])) # top-left ;x-=1300,y=405
        pt2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))#Bottom right,x=1600+160(width);y=405+120(height
        cv2.rectangle(frame, pt1, pt2, color=(180,0,255), thickness=3)

    cv2.putText(
        frame, #image
        tracker_type, #Text of Tracker Name
        (25, 50),#col and row to show the text in
        cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=1.2,
        color=(0, 255, 125),
        thickness=3,
    )

    #Displaying Window
    cv2.imshow("Tracking", frame)

    #Key exit
    key = cv2.waitKey(25) & 0xFF #Key response i 0.25 seconds
    if key in [ord('q'), ord('Q'), 27]: #quite sif key q,or ESC
        break

#Close the window
input_video.release() #Reloccates the memory by clearing the processes
cv2.destroyAllWindows() #Closing the opened window tab after completion of video , or error in program



