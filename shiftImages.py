import cv2 as cv2
import numpy as np
from Image import *

Tony = "Tony.JPG"
Luo = "Luo.JPG"
baseImage = Image(Luo)

def resize(image):
    height, width = image.shape[:2]
    return cv2.resize(image,(width,height))

#get Area as a ratio of an entire image instead of a ratio of pixels later ....
def getAreaRatio(image1, image2):
    return image1.getArea()/image2.getArea()

def adjustImage(toAdjust):
    print(toAdjust.getArea())
    ratio = getAreaRatio(toAdjust, baseImage)
    img = toAdjust.image
    
    width = int(img.shape[1] * ratio)
    height = int(img.shape[0] * ratio)
    img = cv2.resize(img, (width,height))
    
    toAdjust.setImage(img)
    toAdjust.update()
    print(toAdjust.getArea())


tonyImage = Image(Tony)
adjustImage(tonyImage)