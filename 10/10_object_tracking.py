#Tracking object starts with intialt object detectio then to tracking that object in futher frames
#There are various Tracker cases in open cv.
#Hightlight Medianflow: good for slow motions, Mosse= Fastest tracking

#Reqired Libraries
import cv2
import os
import sys
import matplotlib.pyplot as plt
from IPython.display import Video


#Displaying Preview
preview_video = cv2.VideoCapture("race_car.mp4")
while True:
    ret, frame = preview_video.read()
    if not ret:
        break
    cv2.imshow("Preview", frame)
    #Keys for closing the window
    key = cv2.waitKey(25) & 0xFF
    if key in [ord('q'), ord('Q'), 27]:  # Quit on 'q', 'Q', or ESC
        break
#Cleaning the processes
preview_video.release()
# Close the video screen
cv2.destroyAllWindows()

#Reading Video
input_video = cv2.VideoCapture('race_car.mp4')
ret, frame = input_video.read()



#Function to draw the rectancle of object/car
def draw_rectangle(frame, bbox): #Frame=image, bbox=left upper point and right bottom point
    pt1 = (int(bbox[0]), int(bbox[1]))
    pt2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
    cv2.rectangle(frame, pt1, pt2, (180, 0, 255) ,thickness=2,lineType=1)

def text(frame, txt,org, color=(50,170,222)):
    cv2.putText(
        frame,  # Original fame
        txt,
        org,
        cv2.FONT_HERSHEY_SIMPLEX,  # Font style
        fontScale=1.2,  # Font size
        color=color,
        thickness=3,
        )

#Trackers
tracker_types = ['BOOSTING', 'MIL', 'KCF', 'CSRT', 'TLD', 'MEDIANFLOW', 'MOSSE']

tracker_type = tracker_types[6]  # Mosse

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
elif tracker_type == 'MEDIANFLOW': #Good for slow motion videos
    tracker = cv2.legacy.TrackerMedianFlow_create()
elif tracker_type == 'MOSSE': #For fastest motion
    tracker = cv2.legacy.TrackerMOSSE_create()
else:
    raise ValueError(f"Unknown tracker type: {tracker_type}")

#Bound Box
# Lets user select the bounding box manually
#bbox = cv2.selectROI("Select Object to Track", frame, fromCenter=False, showCrosshair=False)
#cv2.destroyWindow("Select Object to Track")

#Lets the bounding box create automatically by refrece co-ordinates
bbox = (1300, 405, 160, 120)
tracker.init(frame, bbox) #Making the bound box on designated cordinates in each frame by caliing the tracker which been selected


# Get frame size dynamically
height, width, channel = frame.shape #Works only when video is color
#If video is grayscale
#height,width=frame.shape

#Writing the video using cv2 VideoWriter
video_name = f"race_car-{tracker_type}.mp4"
output_video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), 10, (width, height))


while True:
    ok, frame = input_video.read() #Read return 2 value , a return value when the video is executed by frame and each frame
    if not ok:
        break

    success, bbox = tracker.update(frame)#if there no break then the same 'ok value beacuse the sucess and frame become the bound x
    #Updates doe sdetects according to selected model and track in bbox and in writing

    # Text Display
    if success:
        draw_rectangle(frame, bbox)
        text(frame, f"{tracker_type} Tracker", org=(10,30))
    else:
        text(frame, "Tracking Failed", org=(10,30), color=(0, 0, 255))
    #Write the video
    output_video.write(frame)
    #Displaying the written video
    cv2.imshow("Tracking Output", frame)

    #Keys arguments
    key = cv2.waitKey(25) & 0xFF
    if key in [ord('q'), ord('Q'), 27]:  # Quit on 'q', 'Q', or ESC
        break

#Cleaning prccessing memory
input_video.release()
output_video.release()
#Closingthe output screens
cv2.destroyAllWindows()

print("Tracking completed :", video_name)
