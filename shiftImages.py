import cv2 as cv2
import numpy as np

def find_midpoint(image):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread('Tony.jpg')
    faces = face_cascade.detectMultiScale(1.3, 5)
    return (faces.x + faces.w/2, faces.y + faces.l/2)
        
    #return cv2.rectangle(get the midpoint)
    
print(find_midpoint('Tony.jpg'))