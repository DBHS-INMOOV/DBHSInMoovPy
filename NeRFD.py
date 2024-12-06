import cv2
import mediapipe as mp
import json
import numpy as np
import math

# Initialize MediaPipe FaceMesh
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Open webcam
cap = cv2.VideoCapture(0)
face_landmarks = []

# Loads known faces from JSON file
def load_known_faces():
    try:
        with open('known_faces.json', 'r') as file:
            known_faces = json.load(file)
        return known_faces
    except FileNotFoundError:
        return {}

# Save new faces to the JSON file
def save_known_faces(known_faces):
    with open('known_faces.json', 'w') as file:
        json.dump(known_faces, file)

# Function to calculate the Euclidean distance between two points
def euclidean_distance(landmarks1, landmarks2):
    distance = 0.0
    for l1, l2 in zip(landmarks1, landmarks2):
        distance += (l1['x'] - l2['x'])**2 + (l1['y'] - l2['y'])**2 + (l1['z'] - l2['z'])**2
    return math.sqrt(distance)

def recognition(frame, known_faces):
    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    # If no faces are detected, return an empty list and don't crash the program
    if not results.multi_face_landmarks:
        return []

    for landmarks in results.multi_face_landmarks:
        face_landmarks = []
        for landmark in landmarks.landmark:
            face_landmarks.append({
                'x': landmark.x,
                'y': landmark.y,
                'z': landmark.z
            })

        # Compare with known faces
        identified = False
        for name, known_landmarks in known_faces.items():
            # Compare distance with known face
            distance = euclidean_distance(face_landmarks, known_landmarks)
            if distance < 0.5:  # Threshold to consider a match
                cv2.putText(frame, f"Recognized: {name}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                identified = True

        if not identified:
            cv2.putText(frame, "Stranger Danger", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Draw landmarks on the face
        mp_drawing.draw_landmarks(frame, landmarks, mp_face_mesh.FACEMESH_CONTOURS)

    return face_landmarks

# Initialize the face mesh model
with mp_face_mesh.FaceMesh(
        max_num_faces=10,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as face_mesh:

    known_faces = load_known_faces()  # Load known faces from the file

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        face_landmarks = recognition(frame, known_faces)

        # Ask to add a new face to the database when the 'a' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('a') and face_landmarks:
            name = input("Enter name of the person: ")
            known_faces[name] = face_landmarks
            save_known_faces(known_faces)  # Save updated faces to the file
            print(f"{name} added to the database.")

        # Display the frame
        cv2.imshow("SKIBIDI INMOOV", frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()