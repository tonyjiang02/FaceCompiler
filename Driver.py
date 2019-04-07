import os
from shiftImagesByEyes import *
from ImageEyes import *

fromdirectory = "images"
todirectory = "adjustedimages"
baseImage = Image("images/Base.JPG")

for image in os.listdir(fromdirectory):
    frompath = fromdirectory + "/" + image
    topath = todirectory + "/adjusted_" + image
    print(frompath, topath)
    shiftImagesByEyes(topath, baseImage, frompath)


