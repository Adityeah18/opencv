#!/usr/bin/python

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

# Importation
import cv2
import sys
import numpy

PREVIEW = 0  # Preview Mode;Camera access
BLUR = 1  # Blurring Filter
FEATURES = 2  # Corner Feature Detector
CANNY = 3  # Canny Edge Detector

s = 0  # Acessing the camera
# CLA Conditions
if len(sys.argv) > 1:
    s = sys.argv[1]

image_filter = PREVIEW
alive = True

win_name = "Camera Filters"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
result = None

source = cv2.VideoCapture(s)

while alive:
    #Reading the video
    has_frame, frame = source.read()
    if not has_frame:  # Meaning video ends
        break

    #Frame is like src img
    frame = cv2.flip(frame, 1)  # flipping the frame horizontal to give natural camera

    if image_filter == PREVIEW:
        result = (
            frame  # Just executes the 0 of vedeo capture to just acessing the camera
        )
    elif image_filter == BLUR:
        result = cv2.blur(frame, ksize= (100, 100),anchor=(-2,2))  # blur takes src_image and ksize tuple of width and height as essential  ,anchor points tuple as optionale
    # corner features

    ##edge Dtection
    elif image_filter == CANNY:
        result = cv2.Canny(frame, 100, 120) #Canny takes 3 essential arg ; sorce image, Threshold min and threshold max
                                            #Threshold min Below 100 → ignored.(Black) ;Pixels with gradient > 150 → considered strong edges.(White)
                                            #Between min and max threshold, that need to be optimized as the  can form the continous lines
    #Feature Detection/Corner Detection
    elif image_filter == FEATURES:
        # --- Shi-Tomasi Corner Detection ---
        # Convert to grayscale since feature detectors work on intensity gradients
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        result = frame.copy()  # Create a copy to draw on (preserve original)

        # cv2.goodFeaturesToTrack uses Shi-Tomasi method under the hood
        corners = cv2.goodFeaturesToTrack(
            frame_gray,
            maxCorners=500,  # Max number of features to detect
            qualityLevel=0.3,  # Minimum quality: 0.2 means only strong corners are kept
            minDistance=10,  # Minimum distance between features
            blockSize=8 # Size of neighborhood considered for corner detection
        )

        if corners is not None:
            # Reshape to (N, 2) and convert to integers for drawing
            for x, y in numpy.float32(corners).reshape(-1, 2):
                x = int(x)
                y = int(y)
                # Draw green circles at each feature point
                cv2.circle(result, (x, y), 10, (0, 255, 0), 1)

    cv2.imshow(win_name, result)

    key = cv2.waitKey(1)  # 1miliseconds
    if (
        key == ord("Q") or key == ord("q") or key == 27
    ):  # exits when q is pressed #what's ord fuction?
        alive = False
    elif key == ord("P") or key == ord("p"):  # p for only previews
        image_filter = PREVIEW
    elif key == ord("C") or key == ord("c"):  # c for canny
        image_filter = CANNY
    elif key == ord("B") or key == ord("b"):  # b for blurr
        image_filter = BLUR
    elif key == ord("F") or key == ord("f"):  # f for corner features
        image_filter = FEATURES


source.release()
cv2.destroyWindow(win_name)
