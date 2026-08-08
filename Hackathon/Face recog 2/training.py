import cv2
from Facemodule import FaceModule
import pickle
class train():
    def __init__(self,name,roll):
        fm = FaceModule()
        self.face_recognized = fm.add_face(roll,num_samples = 50)
        print(self.face_recognized)
        self.details = "D:\Python files\Hackathon\Face recog 2\details.dat"
        with open(self.details,"ab") as f:
            pickle.dump([self.face_recognized,name],f)