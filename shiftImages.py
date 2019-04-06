import cv2
import numpy as np
from Image import *

Tony = "Tony.JPG"
Luo = "Luo.JPG"
baseImage = Image(Luo)

#get Area as a ratio of an entire image instead of a ratio of pixels later ....
def getAreaRatio(image1, image2):
    return image1.getArea()/image2.getArea()

def adjustImage(toAdjust):
    ratio = getAreaRatio(baseImage, toAdjust)
    img = toAdjust.image
    
    width = int(img.shape[1] * (ratio**(0.5)))
    height = int(img.shape[0] * (ratio**(0.5)))
    img = cv2.resize(img, (width,height))
    toAdjust.setImage(img)
    toAdjust.update()
    


tonyImage = Image(Tony)
adjustImage(tonyImage)
print(tonyImage.getArea())
print(baseImage.getArea())
tonyImage.saveImage()
baseImage.saveImage()