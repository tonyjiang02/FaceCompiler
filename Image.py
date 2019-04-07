import cv2 as cv2


class Image:

    def getFace(self, cv2_img):
        face_cascade = cv2.CascadeClassifier(
            'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)  # grayscale
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:  # assume that only one face is detected
            return (x, y, w, h)
    
    def getMidpoint(self):  # midpoint of face
        Rectangle = self.Rectangle
        x = Rectangle[0]
        y = Rectangle[1]
        w = Rectangle[2]
        h = Rectangle[3]
        return x + w / 2, y + h / 2

    def getArea(self):  # area of face
        Rectangle = self.Rectangle
        w = Rectangle[2]
        h = Rectangle[3]
        return w * h

    def update(self):
        self.Rectangle = self.getFace(self.image)

    def imgParameters(self):  # width and height of entire image
        height, width = self.image.shape[:2]
        return width, height

    def setImage(self, cv2_img):
        self.image = cv2_img

    def showImage(self):
        cv2.imshow('image', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def saveImage(self, save_path):
        cv2.imwrite(save_path, self.image)

    def __init__(self, fileName):
        self.fileName = fileName
        self.image = cv2.imread(fileName)
        self.Rectangle = self.getFace(self.image)