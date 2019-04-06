import cv2 as cv2
import numpy as np

def getMidpoint(img):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        img = cv2.imread(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #grayscale
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces: 
                return (x + w/2, y + h/2)
print(getMidpoint("Tony.JPG"))
