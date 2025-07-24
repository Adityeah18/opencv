

#                          License Agreement
#                         3-clause BSD License
#
#       Copyright (C) 2018, Xperience.AI, all rights reserved.
#
# Third party copyrights are property of their respective owners.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#   * Neither the names of the copyright holders nor the names of the contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# This software is provided by the copyright holders and contributors "as is" and
# any express or implied warranties, including, but not limited to, the implied
# warranties of merchantability and fitness for a particular purpose are disclaimed.
# In no event shall copyright holders or contributors be liable for any direct,
# indirect, incidental, special, exemplary, or consequential damages
# (including, but not limited to, procurement of substitute goods or services;
# loss of use, data, or profits; or business interruption) however caused
# and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of
# the use of this software, even if advised of the possibility of such damage.

# Imprting Libraries
import cv2
import sys

#s=0 =web camera access
#s=1 video refrence path
s = 0
if len(sys.argv) >1:
    s = sys.argv[1]

#VideoCapture Function of opencv which is running 12_facedetection.py file
# Default camera index (0 = internal webcam) 1 meaning video refrence
source = cv2.VideoCapture(s)

#Heading
win_name = 'Camera Preview'
#Accesing camera
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

# Load the pre-trained face detection model (DNN-based)
#dnn=deep neural network
# 'deploy.prototxt' defines the model architecture
# Reading network from caffemodel algorithm
# 'res10_300x300_ssd_iter_140000_fp16.caffemodel' contains the pre-trained weights
net = cv2.dnn.readNetFromCaffe("deploy.prototxt",
                               "res10_300x300_ssd_iter_140000_fp16.caffemodel")

#Less the threshold more the sensetivity, but even more can detect wrong face so it should be balanced
conf_threshold = 0.8

while cv2.waitKey(1) != 27  : #27==ESC
    has_frame, frame = source.read() # Reading the frame from accessing the webcam
    if not has_frame:
        break
    #Fliiping the imageg so its conventional camera
    frame = cv2.flip(frame,1) #code 0 = x axis flip, -1 = x&y both flip, ;1=y axis flip

    # Get frame dimensions
    frame_height = frame.shape[0]
    frame_width = frame.shape[1]
    ##Note that the size of resolution here is the webcam resolution no matter what the frame size is here its will resized to 300x300 in blob algo

    # Create a 4D blob from a frame.
    blob=cv2.dnn.blobFromImage(frame, #Convert the frame to a 4D blob (input for DNN)
                               scalefactor=1,
                               size=(300,300), #size = (300,300) expected input size of the model (width, height) 3See here no mattertheframe size of webcam ,it 'll be resized to this
                               mean=[104,117,123], # - mean subtraction for normalization (BGR mean values)
                               swapRB=False, #Caffe-based face detection model, the model was trained on BGR, so swap =False ; if RGB then True
                               crop=False, #REsize is still there just not cropping
                               )
    # Run a model
    # Set the blob as input to the network
    net.setInput(blob)

    # Perform forward pass (inference)
    detections = net.forward() # net.forward does the real detectio
    #print(detections.shape) #Returns(1, 1, 200, 7) Output shape = (1, 1, N, 7), where N is the number of detections (max 200)

    for i in range(detections.shape[2]):# the 2nd index is the real confidence returns by forward pass
        confidence = detections[0, 0, i, 2] #i = confidence from neural network
        if confidence > conf_threshold:#matching the i patameter with neural models to detect the face here

            # Convert normalized coordinates to absolute pixel values
            x_left_bottom = int(detections[0, 0, i, 3] * frame_width)
            y_left_bottom = int(detections[0, 0, i, 4] * frame_height)
            x_right_top = int(detections[0, 0, i, 5] * frame_width)
            y_right_top = int(detections[0, 0, i, 6] * frame_height)

            #making the rectangle with the points
            cv2.rectangle(frame,(x_right_top, y_right_top), (x_left_bottom, y_left_bottom), (124, 0, 200),thickness=2)

            # Display confidence label above bounding box
            label = "Confidence: %.3f" % confidence #Printing the value of i
            label_size, base_line = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)

            # Draw filled rectangle behind text
            cv2.rectangle(frame, (x_left_bottom, y_left_bottom - label_size[1]),
                                (x_left_bottom + label_size[0], y_left_bottom + base_line),
                                (255, 150, 255), cv2.FILLED)
            # Put the text label
            cv2.putText(frame, label, (x_left_bottom, y_left_bottom),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
            
            # What's happening in above algorithm step by step:
            '''What Happens Step-by-Step:
            You capture a frame from webcam (say 1280×720).

            You resize it to 300×300 just for the DNN model using blobFromImage(...).

            The model returns detections in normalized coordinates (between 0 and 1).

            You scale those back to the 1280×720 frame for drawing rectangles.

            You display the frame in original resolution with rectangles over it.'''

    # Returns (ticks, timings) — ticks need to be converted using cv2.getTickFrequency()
    t, _ = net.getPerfProfile() # t= is the inference time to detect a face by algo
    label = 'Inference time: %.2f ms' % (t * 1000.0 / cv2.getTickFrequency())

    # Display inference time on frame
    cv2.putText(frame, label, (0, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255))

    # Show final output in window
    cv2.imshow(win_name, frame)

# Cleanup: release camera and destroy window
#And the empty the memory which is used while processing
source.release()
cv2.destroyWindow(win_name)
