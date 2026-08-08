import cv2
from Facemodule import FaceModule
import csv
from datetime import datetime
import pickle
class recog():
    def __init__(self):
        self.details = "D:\Python files\Hackathon\Face recog 2\details.dat"
        self.attendance = "D:\Python files\Hackathon\Face recog 2\sattendance.csv"
        self.markedroll = "D:\Python files\Hackathon\Face recog 2\markedroll.dat"
        with open(self.markedroll,"ab") as f:
            pass
        fm = FaceModule()
        cam = cv2.VideoCapture(0)
        while True:
            name = ""
            self.ex = 0
            connection,frame = cam.read()
            if not connection :
                print("NO connection cam")
                break
            roll,r = fm.recognize_face(frame)
            with open(self.details,"rb") as f:
                while True:
                    try:
                        l = pickle.load(f)
                        if str(l[0]) == str(roll):
                            name = l[1]
                    except EOFError:
                        break
            with open(self.markedroll,"rb") as a: 
                while True:
                    try:
                        l = pickle.load(a)
                        if l[0] == str(roll):
                            self.ex = 1
                    except EOFError:
                        break
                if self.ex == 0:
                    with open(self.attendance,"a",newline="") as f:
                        self.now = datetime.now()
                        self.date = self.now.date()
                        self.time = self.now.time()
                        writer = csv.writer(f)
                        if name != "" and roll !="":
                            writer.writerow([roll,name,self.date,self.time])
                    with open(self.markedroll,"ab") as f:
                        pickle.dump([roll],f)


            cv2.imshow("DeepFace Recognition", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        cam.release()
        cv2.destroyAllWindows()
