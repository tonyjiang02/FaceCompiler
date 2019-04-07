from ImageEyes import *
import numpy as np
import cv2 as cv2
import math
path = "images/MateoTilted.JPG"
image = ImageEyes(path)

def adjustAngle(image):
    midpoints = image.midpoints
    xDiff = midpoints[0][0] - midpoints[1][0]
    yDiff = midpoints[0][1] - midpoints[1][1]
    angle = np.arctan(yDiff/xDiff)
    h= image.image.shape[0]
    w = image.image.shape[1]
    R = cv2.getRotationMatrix2D((h/2,w/2),(angle * 180 / math.pi),1)
    rotated = cv2.warpAffine(image.image,R,(h,w))
    cv2.imwrite("rotated.jpg", rotated)
adjustAngle(image)
# image.paintEyes()