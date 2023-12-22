import numpy as np
import cv2 as cv
import tifffile as tiff

# This is an sample program for performing hyperspectral analysis using the LuminaScope system.
# This software is distributed under the Apache 2.0 License.
# For this analysis we need the three main libraries above.
# They are numpy, opencv-python, and tifffile in that order.

# Opening tiff file from file location
# File location is variable and depends on folders
img = cv.imread('autumn.tif')

# Show image
# syntax: Picture name, variable
cv.imshow('Autumn', img)

# Reading videos
# capture = cv.VideoCapture('Videos/dog.mp4')
# while True:
#   isTrue, frame = capture.read()
#   cv.imshow('Video', frame)
#   if cv.waitkey(20) & 0xFF==ord('d')
#       break
# capture.relase()
# cv.destroyAllWindows()

# Rescaling images
# Works on images, videos, and live video
# def rescaleFrame(frame, scale=0.75):
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)

#     dimensions = (width, height)
#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Changing live video resolution
# def changeRes(width,height):
#     capture.set(3, width)
#     capture.set(4,height)

# Isolate blue, green. red image
# resulting images show concentration/intensity of r,b,g values
b,g,r = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

# Calculate histogram of color? levels


# Crop image by indexing pixel ranges
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

# Smooth image

# Threshhold image

# Calculate phasor with fast fourier transform

# Hyperspectral analysis

cv.waitKey(0)