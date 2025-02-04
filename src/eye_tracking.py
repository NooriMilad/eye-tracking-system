import cv2
import mediapipe as mp

class EyeTracker:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh()
        self.cap = cv2.VideoCapture(0)

    def get_eye_position(self):
        ret, frame = self.cap.read()
        if not ret:
            return None

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # Extract eye coordinates (example for left eye)
                left_eye = face_landmarks.landmark[159]
                return (left_eye.x, left_eye.y)
        return None

    def start_tracking(self):
        while True:
            eye_pos = self.get_eye_position()
            if eye_pos:
                print(f"Eye position: {eye_pos}")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()