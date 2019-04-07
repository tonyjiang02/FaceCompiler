from Image import *
import numpy as np


# get Area as a ratio of an entire image instead of a ratio of pixels later ....
def shiftImageBySquare(frompath, baseImage, topath):
    image = Image(frompath)
    adjustImage(image)
    createImage(topath, baseImage, topath)


def getAreaRatio(image1, image2):
    return image1.getArea() / image2.getArea()


def adjustImage(toAdjust):
    ratio = getAreaRatio(baseImage, toAdjust)
    img = toAdjust.image

    width = int(img.shape[1] * (ratio ** (0.5)))
    height = int(img.shape[0] * (ratio ** (0.5)))
    img = cv2.resize(img, (width, height))
    toAdjust.setImage(img)
    toAdjust.update()


def createImage(topath, baseImage, image1):
    wh = baseImage.imgParameters()
    width = wh[0]
    height = wh[1]
    blankImage = np.zeros((height, width, 3), np.uint8)
    midpointBase = baseImage.getMidpoint()
    midpointImage = image1.getMidpoint()

    xDifference = midpointBase[0] - midpointImage[0]
    yDifference = midpointBase[1] - midpointImage[1]
    wh1 = image1.imgParameters()
    width1 = wh1[0]
    height1 = wh1[1]
    print(blankImage.shape)
    print(image1.image.shape)
    print(width1, height1)
    for xcoord in range(0, width):
        for ycoord in range(0, height):
            oldx = int(xcoord - xDifference)
            oldy = int(ycoord - yDifference)
            if oldy >= 0 and oldx >= 0 and oldy<height1 and oldx<width1:
                blankImage[ycoord][xcoord] = image1.image[oldy][oldx]
    cv2.imwrite(topath, blankImage)
