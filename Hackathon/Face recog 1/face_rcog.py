class facerecog():
    def __init__(self):
        import cv2
        import numpy as np
        import csv
        import os
        from datetime import datetime
        import pickle

        # Load trained model
        self.markedroll = "D:\Python files\Hackathon\Face recog 1\markedroll.dat"
        self.details = "D:\Python files\Hackathon\Face recog 1\details.csv"
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("face_model.yml")
        label_map = np.load("labels.npy", allow_pickle=True).item()
        with open(self.markedroll,"ab") as f:
            pass
        self.marked_rollno = []
        """with open("names.dat","rb") as f:
            while True:
                try:
                    marked_rollno = pickle.load(f)
                except:
                    break"""
                    
        # Haar cascade
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.l = []
        # Attendance file
        attendance_file = "D:\Python files\Hackathon\Face recog 1\sattendance.csv"

        # Create file if not exists
        if not os.path.exists(attendance_file):
            with open(attendance_file, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Name", "Date", "Time","Rollno."])

        # Keep track of marked names
        self.rollno = 0
        cap = cv2.VideoCapture(0)

        print("[INFO] Starting face recognition. Press 'q' to quit.")

        while True:
            with open(self.markedroll,"rb") as f:
                while True:
                    try:
                        self.marked_rollno = pickle.load(f)
                    except:
                        break
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                roi = gray[y:y+h, x:x+w]
                label, confidence = recognizer.predict(roi)

                if confidence < 40:  # lower's more confident
                    name = label_map[label]
                    with open(self.details,"r") as f:
                        reader = csv.reader(f)
                        for i in list(reader):
                            if i[0] == name:
                                self.rollno = i[1]
                else:
                    name = "Unknown"

                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, f"{name}", (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

                # Mark attendance
                if name != "Unknown" and self.rollno not in self.marked_rollno:
                    with open(self.markedroll,"rb") as f:
                        while True:
                            try:
                                self.l = pickle.load(f)
                            except:
                                break
                        a = open(self.markedroll,"wb")
                        self.l.append(self.rollno)
                        pickle.dump(self.l,a)
                        a.close()
                        #print(self.l)
                        
                    now = datetime.now()
                    date = now.strftime("%Y-%m-%d")
                    time = now.strftime("%H:%M:%S")

                    with open(attendance_file, "a", newline="") as f:
                        writer = csv.writer(f)
                        """with open(self.details,"r") as b:
                            reader1 = csv.reader(b)
                            for i in list(reader1):
                                if str(i[0]) == name:
                                    print(i[1])
                                    self.rollno = i[1]"""

                        writer.writerow([name,date,time,self.rollno])
                        """with open("names.dat","wb") as x:
                            marked_rollno.append(rollno)
                            pickle.dump(marked_rollno,x)"""
                        print(f"[INFO] Attendance marked for {name}")
                    

            cv2.imshow("Face Recognition Attendance", frame)

            if (cv2.waitKey(1) & 0xFF == ord('q')) or (cv2.waitKey(1) & 0xFF == ord('Q')):
                break

        cap.release()
        cv2.destroyAllWindows()