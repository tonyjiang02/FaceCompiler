import cv2 as cv2


class Image:
    def __init__(self, fileName):
        def getFace(img):
            face_cascade = cv2.CascadeClassifier(
                'haarcascade_frontalface_default.xml')
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # grayscale
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                return (x, y, w, h)

        self.fileName = fileName
        self.image = cv2.imread(fileName)
        self.Rectangle = getFace(self.image)

    def getFace(self, img):
        face_cascade = cv2.CascadeClassifier(
            'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # grayscale
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            return (x, y, w, h)

    def update(self):
        img = self.image
        face_cascade = cv2.CascadeClassifier(
            'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # grayscale
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            self.Rectangle = (x, y, w, h)

    def imgParameters(self):
        height, width = self.image.shape[:2]
        return width, height

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

    def setImage(self, img):
        self.image = img

    def showImage(self):
        cv2.imshow('image', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def saveImage(self):
        cv2.imwrite("Adjusted.JPG", self.image)
