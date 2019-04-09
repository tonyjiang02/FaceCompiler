import cv2 as cv2


class Picture:

    # initializing class

    def init_face(self):  # only works if only 1 face is detected
        grayscale = cv2.cvtColor(self.cv2_image, cv2.COLOR_BGR2GRAY)  # grayscale
        face_cascade = cv2.CascadeClassifier(
            'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(grayscale, 1.3, 5)  # faces is an array of tuples

        if len(faces) == 1:
            return faces
        else:
            raise Exception("Error! There is not exactly one face detected in image: " + self.path)

    def init_eyes(self):  # re-uses result from get_face
        grayscale = cv2.cvtColor(self.cv2_image, cv2.COLOR_BGR2GRAY)  # grayscale
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        bounded_image = grayscale[
                          self.f_param["y"]:self.f_param["y"] + self.f_param["h"],
                          self.f_param["x"]:self.f_param["x"] + self.f_param["w"]
        ]
        eyes_shifted = eye_cascade.detectMultiScale(bounded_image, 1.1, 8)
        eyes = []
        for eye in eyes_shifted:
            eyes.append(
                (eye[0] + self.f_param["x"],
                 eye[1] + self.f_param["y"],
                 eye[2],
                 eye[3]
                 )
            )
        return eyes

    def init_f_mpoint(self):
        return (  # single midpoint of face
            self.face["x"] + self.f_param["w"] / 2,
            self.f_param["y"] + self.f_param["h"] / 2
        )

    def init_e_mpoints(self):
        e_mpoints = []
        if self.eyes is not None:
            for eye in self.eyes:
                x = eye[0]
                y = eye[1]
                w = eye[2]
                h = eye[3]
                e_mpoints.append(  # appends a tuple representing the midpoint
                    (x + w/2,
                     y + h/2)
                )
        return e_mpoints

    def init_pivot(self):  # pivot point for each picture to match
        pass

    def __init__(self, path):
        # system level variables
        self.path = path

        # cv2 varibles
        self.cv2_image = cv2.imread(path)

        # self-defined variables
        self.face = self.init_face()  # face, throws error if there is not exactly 1 face
        self.f_param = {
            "x": self.face[0][0],
            "y": self.face[0][1],
            "w": self.face[0][2],
            "h": self.face[0][3],
        }
        self.face_area = self.f_param["w"] * self.f_param["h"]

        self.eyes = self.init_eyes()  # eyes
        if self.eyes is not None and len(self.eyes) == 2:  # only creates eye parameters if there are 2 eyes
            self.e_param = {
                "x1": self.eyes[0][0],
                "x2": self.eyes[0][1],
                "y1": self.eyes[0][2],
                "y2": self.eyes[0][3],
                "w1": self.eyes[1][0],
                "w2": self.eyes[1][1],
                "h1": self.eyes[1][2],
                "h2": self.eyes[1][3],
            }
            self.e_mpoints = self.init_e_mpoints()
            self.eye_displacement = (  # distance formula
                (
                        (self.e_mpoints[0][0] - self.e_mpoints[0][1])**2 +
                        (self.e_mpoints[1][0] - self.e_mpoints[1][1])**2
                )*0.5
            )

    # interface to the rest of system

    def paint(self):
        cv2.rectangle(self.cv2_image,  # face rectangle
                      (self.f_param["x"], self.f_param["y"]),
                      (self.f_param["x"] + self.f_param["w"], self.f_param["y"] + self.f_param["h"]),
                      (0, 0, 255), 10)

        if self.eyes is not None:
            for eye in self.eyes:
                x = eye[0]
                y = eye[1]
                w = eye[2]
                h = eye[3]
                cv2.rectangle(self.cv2_image, (x, y), (x+w, y+h), (0, 255, 0), 10)
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('image', 600, 600)
        cv2.imshow('image', self.cv2_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
