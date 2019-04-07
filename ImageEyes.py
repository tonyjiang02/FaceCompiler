import cv2 as cv2
import numpy as np

class ImageEyes:
    def getEyes(self, img):
        Rectarray = []
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # grayscale
        faces = face_cascade.detectMultiScale(gray,1.1,5)
        for (x1,y1,w1,h1) in faces:
            print (x1)
            cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)
            newgray = gray[y1:y1+h1,x1:x1+w1]
            eyes = eye_cascade.detectMultiScale(newgray)
            for (x, y, w, h) in eyes:
                Rectarray.append((x+x1,y+y1,w,h))
        print(Rectarray)
        return Rectarray

    def paintEyes(self):
        rectArr = self.Rectarray
        for (ex,ey,ew,eh) in rectArr:
            cv2.rectangle(self.image,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.imshow('img',self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def update(self): #updates image after resizing face to be in center
        img = self.image
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # grayscale
        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

        Rectarray = []
        for (x, y, w, h) in eyes:
            Rectarray.append(x, y, w, h)
        self.Rectarray = Rectarray

    def imgParameters(self):
        height, width = self.image.shape[:2]
        return width, height

    def getMidpoints(self):  # midpoints of eyes
        rectarr = self.Rectarray
        midpoints = []
        for rectangle in rectarr:
            x = rectangle[0]
            y = rectangle[1]
            w = rectangle[2]
            h = rectangle[3]
            midpoints.append([x + w/2, y + h/2])
        return midpoints
    def setImage(self, img):
        self.image = img

    def showImage(self):
        cv2.imshow('image', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def saveImage(self):
        # cv2.imwrite("Adjusted.JPG", self.image)
        pass
    def test(self):
        print('hello')
    def __init__(self, fileName):
        self.fileName = fileName
        self.image = cv2.imread(fileName)
        self.Rectarray = self.getEyes(self.image)
        self.midpoints = self.getMidpoints()