import cv2 as cv2
import numpy as np

class ImageEyes:
    def getEyes(self, img):
        grayscale_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # grayscale

        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(grayscale_image,1.1,5)
        
        rectarray = []
        for (x1,y1,w1,h1) in faces:
            face_grayscale = grayscale_image[y1:y1+h1,x1:x1+w1]
            eyes = eye_cascade.detectMultiScale(face_grayscale, 1.1, 8)
            for (x, y, w, h) in eyes:
                rectarray.append((x+x1,y+y1,w,h))
        
        if len(rectarray)==2:
            return rectarray
        else:
            print("no eyes found")
            return 0

    def paintEyes(self):
        for (x,y,w,h) in self.Rectarray:
            cv2.rectangle(self.image,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('img',self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def update(self): #updates image after resizing face to be in center
        img = self.image
        self.Rectarray = self.getEyes(img)

    def imgParameters(self):
        height, width = self.image.shape[:2]
        return width, height

    def getMidpoints(self):  # midpoints of eyes
        rectarr = self.Rectarray
        if(rectarr ==0):
            return 0
        midpoints = []
        for rectangle in rectarr:
            x = rectangle[0]
            y = rectangle[1]
            w = rectangle[2]
            h = rectangle[3]
            midpoints.append([x + w/2, y + h/2])
        return midpoints
    
    def getDistance(self):  # distances between eyes
        x1 = self.Rectarray[0][0]
        x2 = self.Rectarray[1][0]
        y1 = self.Rectarray[0][1]
        y2 = self.Rectarray[1][1]
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def setImage(self, cv2_img):
        self.image = cv2_img

    def getMidpointOfLine(self):
        x1 = self.Rectarray[0][0]
        x2 = self.Rectarray[1][0]
        y1 = self.Rectarray[0][1]
        y2 = self.Rectarray[1][1]
        return (
            (x1 + x2) / 2,
            (y1 + y2) / 2
        )

    def showImage(self):
        cv2.imshow('image', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def saveImage(self, save_path):
        cv2.imwrite(save_path, self.image)

    def __init__(self, fileName):
        self.fileName = fileName
        self.image = cv2.imread(fileName)
        self.Rectarray = self.getEyes(self.image)
        self.midpoints = self.getMidpoints()
        self.distance = self.getDistance()