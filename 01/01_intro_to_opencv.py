# -*- coding: utf-8 -*-
"""01_intro_to_opencv.ipynb

##Importation of Libraries

Before we begin working with images, let's import the essential Python libraries:
"""

# Commented out IPython magic to ensure Python compatibility.
import cv2
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from IPython.display import Image

"""##Displaying image using the IPython"""

#Image of 18x18 pixels
Image(filename='checkerboard_18x18.png')#the image is in the same directory

#Similarrly diplaying the the 84x84 pixel images
Image(filename='checkerboard_84x84.jpg') #See the format is jpg

"""##Reading using OpenCV
To load images in OpenCV, we use the `cv2.imread()` function. It requires:

- A **filename** (as a string) — this is mandatory  
- A **flag** — optional, used to specify how the image should be read:
  - `0` — load in **grayscale**
  - `1` — load in **color** (default, BGR format)
  - `-1` — load with **alpha channel** (if present)

---

###  Reading an Image in Grayscale
In the example below, we load a simple checkerboard image in grayscale mode. This converts the image to a 2D NumPy array of pixel intensity values.
"""

#Reading image as grayscale
cb_img=cv2.imread('checkerboard_18x18.png',0)
#Print the array of the checkredboad
print(cb_img)

#Displayng the shape and using numpy
print("Image size is:",cb_img.shape) #Shape tells the dimention of array, if grayscale the 2-D if color then 3-D

#Displaying the data type of the image
print("The data type is: ",cb_img.dtype)

#Displaying the images using the matplotlib
plt.imshow(cb_img) #Using matplotlib.pyplot function imshow

"""⚠️ **Notice:**  
We didn't tell `imshow()` that the image is grayscale, so it applied its default color scheme. To display it properly:

"""

#For gray the image using matplotlib
plt.imshow(cb_img,cmap='gray')

"""Now let’s read another image — a slightly **blurred (fuzzy)** version of the checkerboard. By comparing the pixel values and visual output, we can observe how **image sharpness** is affected at the array level.

This image is also read in **grayscale**, so the resulting array will contain only intensity values from **0 (black)** to **255 (white)**.
"""

#Another example
cb_img_fuzzy=cv2.imread('checkerboard_fuzzy_18x18.jpg',0)#The image is in same directory ,having same name /reading using cv2

#For printing arrays
print(cb_img_fuzzy)
#For dispalying using the matplotlib
plt.imshow(cb_img_fuzzy,'gray')

"""**What's Happening?**


- The "fuzzy" appearance is caused by **varying intensity values** between adjacent pixels.
- Unlike a sharp checkerboard with clear black-and-white patches (0 and 255), a fuzzy image has **gradual transitions** — pixel values might range anywhere between 0–255.
- Grayscale images in OpenCV are stored as **8-bit unsigned integers (`uint8`)**, meaning each pixel uses 8 bits = 1 byte = **values from 0 to 255**.

##Wroking with Color


Sometimes, instead of using `OpenCV` or `matplotlib`, you may want to display an image directly in the notebook using **IPython’s display tools**. This is especially useful for showing logos, reference images, or examples without any processing.

Here’s how to display a color image (like a Coca-Cola logo) that's in your current working directory:
"""

#Reading the color image cocacola using IPython
Image(filename='coca-cola-logo.png') #Image is with same name in similar directory

"""### Exploring Image Dimensions and Channels</font>

Now let's read a **color image** using OpenCV and explore its structure using NumPy.

When loading with flag `1`, OpenCV reads the image in **color mode** (BGR). The resulting image is stored as a **3D NumPy array**:  

- The first two dimensions represent **height** and **width**  
- The third dimension represents the **number of color channels** (usually 3 for BGR)

We'll also inspect:
- `.size`: total number of elements (pixels × channels)
- `.shape`: image dimensions and channels

"""

#Read and showing the chaneels of the image using numpy
coke_img=cv2.imread("coca-cola-logo.png",1)#See reading in coloe so the 1,0=gray

#Printing size of image (size meaning how many total pixel is there)
print("Image size:",coke_img.size)

#Print image shape: (height, width, channels)
print("Image shpae:",coke_img.shape)

"""for example: shape = (700, 700, 3)

- Height = 700 pixels  
- Width = 700 pixels  
- Channels = 3 (Blue, Green, Red)  
- So: `700 × 700 × 3 = 1,470,000` total values (bytes, if dtype is `uint8`)

###Displaying the image

Using the matplotlib
plt.imshow(coke_img) #The blue image comes using matplotlib as matplotlib as whenwe converted the coke_img using cv2 it resverse the color code
In cv2 the format of color is BGR and not RGB
So we either have to format while the reading the image beforehand or we have to change the index whgile matplotlib display
"""

#Using the matplotlib
plt.imshow(coke_img) #

"""### Reversing Color Channels with NumPy</font>

Instead of using `cv2.cvtColor()` to convert from BGR to RGB, we can also reverse the color channels manually using **NumPy slicing**.

OpenCV stores color images as 3D arrays with the third dimension being `[Blue, Green, Red]`.  
We can reverse this third dimension using slicing: `image[:, :, ::-1]`  
This results in `[Red, Green, Blue]`, which matches the expected format for `matplotlib`.

This method is lightweight and avoids importing additional functions.

"""

#changing the channel format using the index
coke_img_channels_reversed=coke_img[:,:,::-1]# Reverse the channel order: BGR → RGB using slicing
plt.imshow(coke_img_channels_reversed)

"""### Splitting and Merging Color Channels</font>

OpenCV allows you to split a color image into its individual channels — **Blue**, **Green**, and **Red** — using `cv2.split()`. You can also merge them back into a full color image using `cv2.merge()`.

This is useful when analyzing or manipulating a specific color channel.

---

###  Step 1: Splitting Channels
We’ll read an image of a lake and split it into its B, G, R components.

---

###  Step 2: Displaying Each Channel

We’ll display each channel in grayscale to show intensity levels:
- Brighter areas mean higher intensity in that channel.

---

###  Step 3: Merging Channels Back (as RGB)

Since OpenCV uses BGR, and we split into B, G, R — we need to **reorder** to R, G, B when merging if we want it to display correctly in `matplotlib`.


"""

#Using cv2.split() and cv2.merge()

#Splitting the image into BGR
img_NZ_bgr=cv2.imread("New_Zealand_Lake.jpg",1) # 1 for reading it in color,
b,g,r=cv2.split(img_NZ_bgr)

#Show the channel in RGB using matplotlib
plt.figure(figsize=[30,6])
plt.subplot(141);plt.imshow(r,cmap='gray');plt.title("Red Channel")
plt.subplot(142);plt.imshow(g,cmap='gray');plt.title("Green Channe")
plt.subplot(143);plt.imshow(b,cmap='gray');plt.title("Blue Channel")

#Merging th rgb channel
img_NZ_merged=cv2.merge((r,g,b))
#Showing the merged output
plt.subplot(144);plt.imshow(img_NZ_merged);plt.title("Merged image") #The merge image is similar to original but different/Same Same but difflent

"""###Understanding Bits in Images: Grayscale vs RGB</font>

When working with image processing, it's important to understand how images are stored in memory, particularly how many **bits** each pixel uses and why.

---

  Grayscale Images

-  **1 channel** per pixel (intensity only)
-  Each channel uses **8 bits (1 byte)**
-  Value range: `0 – 255`  
-  Total = **8 bits per pixel**

---
  RGB / BGR Color Images

- **3 channels** per pixel (Red, Green, Blue or Blue, Green, Red in OpenCV)
-  Each channel uses **8 bits**
- Total = `8 × 3 = 24 bits = 3 bytes` per pixel
- Hence, called a **24-bit image**

###Converting the different color spaces
"""

#Using cv2.cvtColor() function

#As the problem of image in bgr format so theres a  simple fuction which can do that we do not have to do all that to just reversing the format or color changing
#Using cv2.COLOR_BGR2RGB
img_NZ_rgb=cv2.cvtColor(img_NZ_bgr,cv2.COLOR_BGR2RGB)
plt.imshow(img_NZ_rgb)

"""###Converting to HSV Color Space

The **HSV color model** (Hue, Saturation, Value) is often more intuitive for color manipulation than RGB or BGR.

- **Hue (H):** The type of color (e.g., red, blue) — ranges from 0 to 179 in OpenCV  
- **Saturation (S):** Intensity or purity of the color — 0 means gray, 255 means full color  
- **Value (V):** Brightness of the color — 0 is black, 255 is full brightness
"""

#Changing Hue Saturation Value HSV

#Using another function of cvtColor =cv2.COLOR_BGR2HSV

img_hsv=cv2.cvtColor(img_NZ_bgr,cv2.COLOR_BGR2HSV)

#Splitting the images into hsv
h,s,v=cv2.split(img_hsv)

#Showing the channels

plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(h,cmap='gray');plt.title("H Channel")
plt.subplot(142);plt.imshow(s,cmap='gray');plt.title("S Channel")
plt.subplot(143);plt.imshow(v,cmap='gray');plt.title("V Channel")

#For showing original image if the convertion from bgr to rgb is not done
#plt.subplot(144);plt.imshow(cv2.cvtColor(img_NZ_bgr,cv2.COLOR_BGR2RGB));plt.title("Original")

#Original image can also be done as this coz we conveted the image in rgb
plt.subplot(144);plt.imshow(img_NZ_rgb);plt.title("Original")

"""###Modifying HSV Channels</font>

One of the powerful advantages of using HSV is that you can **modify color characteristics** directly by manipulating the **Hue (H)**, **Saturation (S)**, or **Value (V)** channels.

---

 **Example**: Shifting the Hue

In this example, we slightly increase the hue values by 10 units to shift the color tones.

📌 Important Note:  
After modifying the HSV channels, we must **merge them back** into a full HSV image, and **then convert it to RGB** again for display.

This is necessary because:
- Our previous `img_NZ_rgb` was based on the **original** HSV image.
- Now you've **modified the H channel**, so your image data has changed.
- Therefore, you need to **re-convert** the **new HSV image** to RGB again — otherwise the display will not reflect your changes.

---

"""

#Modifying the channels

# Modify the Hue channel (shift hue by +10)
h_new=h+10
# Merge updated HSV channels
img_NZ_merged=cv2.merge((h_new,s,v))
# Convert new HSV image to RGB for display
img_NZ_rgb=cv2.cvtColor(img_NZ_merged,cv2.COLOR_HSV2RGB)

#Show the channel
plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(h_new,cmap='gray');plt.title("H Channel")
plt.subplot(142);plt.imshow(s,cmap='gray');plt.title("S Channel")
plt.subplot(143);plt.imshow(v,cmap='gray');plt.title("V Channel")
plt.subplot(144);plt.imshow(img_NZ_rgb);plt.title("Modified")

"""##Saving Images with OpenCV

---


"""

cv2.imwrite("new_zealand.png",img_NZ_bgr) #Why bgr open correct image while what i converted above as rgb is not?

Image(filename='new_zealand.png')

"""> **Why use `img_NZ_bgr` instead of `img_NZ_rgb` when saving?**
OpenCV expects images in **BGR format** when saving using `cv2.imwrite()`.If you try to save an image that has been converted to **RGB** (like `img_NZ_rgb` for displaying with `matplotlib`), the saved file will have **incorrect colors**, because OpenCV does not automatically detect or fix the color order. That's why saving `img_NZ_bgr` works correctly — it maintains the expected BGR format for OpenCV.

```
#  **Tip**
If you ever convert BGR → RGB for display and want to save that edited version, make sure to convert it **back to BGR** before saving:
```
"""
