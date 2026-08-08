class train():
    def __init__(self,name,roll):
        import cv2
        import os
        import numpy as np
        import csv
        # Load Haar Cascade
        self.details = "D:\Python files\Hackathon\Face recog 1\details.csv"
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        with open(self.details,"a") as f:
            pass
        self.o = 0
        # Person's name
        person_name = name.strip()
        DATASET_PATH = "dataset"
        person_folder = os.path.join(DATASET_PATH, person_name)

        # Make folder if it doesn't exist
        os.makedirs(person_folder, exist_ok=True)

        # Start webcam
        cap = cv2.VideoCapture(0)
        count = 0
        print("[INFO] Starting face capture. Press 'q' to quit.")

        while True:
            ret, frame = cap.read()
            if not ret:
                print("[ERROR] Failed to grab frame from webcam.")
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            if len(faces) == 0:
                cv2.putText(frame, "No face detected", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            for (x, y, w, h) in faces:
                # Draw rectangle
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                # Crop and resize face
                face_roi = gray[y:y+h, x:x+w]
                face_resized = cv2.resize(face_roi, (200, 200))

                # Save image
                file_name = os.path.join(person_folder, f"{count}.jpg")
                success = cv2.imwrite(file_name, face_resized)

                if success:
                    print(f"[INFO] Saved {file_name}")
                    self.o = 1
                    count += 1
                else:
                    print(f"[ERROR] Could not save {file_name}")

            cv2.imshow("Face Capture", frame)

            if cv2.waitKey(1) & 0xFF == ord('q') or count >= 50:
                break
        if self.o:
            with open(self.details,"a",newline = "") as f:
                writer = csv.writer(f)
                writer.writerow([name,roll])
        cap.release()
        cv2.destroyAllWindows()
        print(f"[INFO] Finished. Saved {count} face images to {person_folder}")
        ###############################################
        DATASET_PATH = "dataset"
        IMG_SIZE = (200, 200)  # width x height

        faces = []
        labels = []
        label_map = {}

        for idx, person in enumerate(os.listdir(DATASET_PATH)):
            person_folder = os.path.join(DATASET_PATH, person)
            if not os.path.isdir(person_folder):
                continue

            label_map[idx] = person
            for file in os.listdir(person_folder):
                img_path = os.path.join(person_folder, file)
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                if img is None:
                    continue

                # Resize to fixed size
                img_resized = cv2.resize(img, IMG_SIZE)
                faces.append(img_resized)
                labels.append(idx)

        print(f"[INFO] Loaded {len(faces)} images for training.")

        faces = np.array(faces)
        labels = np.array(labels)

        # Train LBPH recognizer
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces, labels)

        # Save model + labels
        recognizer.save("face_model.yml")
        np.save("labels.npy", label_map)

        print("[INFO] Training complete. Model saved as face_model.yml and labels.npy")

