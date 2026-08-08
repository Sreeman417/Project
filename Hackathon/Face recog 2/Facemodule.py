import cv2
import os
import pickle
import numpy as np
from deepface import DeepFace
from tkinter import Tk, filedialog


class FaceModule:
    def __init__(self, db_path=r"D:\Python files\Hackathon\Face recog 2\sfaces_db.pkl", model_name="ArcFace"):
        self.db_path = db_path
        self.model_name = model_name
        self.face_db = self.load_db()

    # ---------------- Load/Save Database ---------------- #
    def load_db(self):
        if os.path.exists(self.db_path):
            with open(self.db_path, "rb") as f:
                return pickle.load(f)
        return {}

    def save_db(self):
        with open(self.db_path, "wb") as f:
            pickle.dump(self.face_db, f)

    # ---------------- Embedding Function ---------------- #
    def get_embedding(self, face_img):
        # Convert to RGB for DeepFace
        if face_img.shape[2] == 3:
            face_img_rgb = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
        else:
            face_img_rgb = face_img
        embedding = DeepFace.represent(
            face_img_rgb,
            model_name=self.model_name,
            enforce_detection=False
        )[0]["embedding"]
        embedding = np.array(embedding, dtype=np.float32)
        embedding = embedding / np.linalg.norm(embedding)  # normalize
        return embedding

    # ---------------- Add Face via Webcam ---------------- #
    def add_face(self, roll_no, num_samples=50):
        cap = cv2.VideoCapture(0)
        samples = 0

        face_dir = f"faces/{roll_no}"
        os.makedirs(face_dir, exist_ok=True)

        while samples < num_samples:
            ret, frame = cap.read()
            if not ret:
                continue

            faces = DeepFace.extract_faces(frame, enforce_detection=False)

            if len(faces) > 0:
                face_img = faces[0]["face"]

                if face_img is not None and face_img.size > 0:
                    face_img_uint8 = np.clip(face_img, 0, 255).astype(np.uint8)
                    embedding = self.get_embedding(face_img_uint8)

                    if roll_no not in self.face_db:
                        self.face_db[roll_no] = []
                    self.face_db[roll_no].append(embedding)

                    # save cropped face image
                    cv2.imwrite(os.path.join(face_dir, f"sample_{samples+1}.jpg"), face_img_uint8)
                    samples += 1
                    print(f"[INFO] Captured {samples}/{num_samples} samples for Roll No={roll_no}")

            # show live with counter
            cv2.putText(frame, f"Samples: {samples}/{num_samples}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("Add Face", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        self.save_db()
        return roll_no

    # ---------------- Add Face via File Picker ---------------- #
    def add_photo(self, roll_no):
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(
            title="Select a Photo",
            filetypes=[("Image files", "*.jpg *.jpeg *.png")]
        )
        if not file_path:
            print("[WARN] No file selected.")
            return None

        img = cv2.imread(file_path)
        if img is None:
            print("[ERROR] Could not read the image.")
            return None

        faces = DeepFace.extract_faces(img, enforce_detection=False)
        if len(faces) == 0:
            print("[WARN] No face detected in the selected photo.")
            return None

        face_img = faces[0]["face"]
        if face_img is None or face_img.size == 0:
            print("[WARN] Face extraction failed.")
            return None

        face_img_uint8 = np.clip(face_img, 0, 255).astype(np.uint8)
        embedding = self.get_embedding(face_img_uint8)

        if roll_no not in self.face_db:
            self.face_db[roll_no] = []
        self.face_db[roll_no].append(embedding)

        face_dir = f"faces/{roll_no}"
        os.makedirs(face_dir, exist_ok=True)
        cv2.imwrite(os.path.join(face_dir, os.path.basename(file_path)), face_img_uint8)

        self.save_db()
        print(f"[INFO] Photo added for Roll No={roll_no}")
        return roll_no

    # ---------------- Recognize Face with Box ---------------- #
    def recognize_face(self, frame, threshold=0.85):
        faces = DeepFace.extract_faces(frame, enforce_detection=False)

        if len(faces) > 0:
            face_img = faces[0]["face"]
            bbox = faces[0]["facial_area"]
            x, y, w, h = bbox["x"], bbox["y"], bbox["w"], bbox["h"]

            face_img_uint8 = np.clip(face_img, 0, 255).astype(np.uint8)
            embedding = self.get_embedding(face_img_uint8)

            best_match = None
            best_score = -1

            for roll_no, embeddings in self.face_db.items():
                for ref_emb in embeddings:
                    ref_emb = ref_emb / np.linalg.norm(ref_emb)  # normalize
                    sim = np.dot(embedding, ref_emb)
                    if sim > best_score:
                        best_score = sim
                        best_match = roll_no

            if best_score >= threshold:
                # Draw rectangle and roll number
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, str(best_match), (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                return best_match, frame

        return None, frame
