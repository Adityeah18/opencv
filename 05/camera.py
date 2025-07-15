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

#Importing the essential libraires
import cv2
import sys

#Ss=0 means if theres's no cla then the 0 index cla executes which is the 'filename.py'
s = 0
#We can provide cla too starting from index 1 to many
if len(sys.argv) > 1:
    s = sys.argv[1:]

#Videocapture is the function of cv2 to acess the camera
source = cv2.VideoCapture(s)

#Title to show while previewing
win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

while cv2.waitKey(1) != 27: # Escape ASCII =27
    has_frame, frame = source.read() #has_fram=meaning have some image sequence
    if not has_frame: #Meaning in the end
        break
    cv2.imshow(win_name, frame)

source.release()
cv2.destroyWindow(win_name) #as while loop breaks the window gets close
