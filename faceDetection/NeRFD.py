import cvzone
import pickle
from cvzone.FaceMeshModule import FaceMeshDetector
import cv2
import numpy as np


cap = cv2.VideoCapture(0)

FMD = FaceMeshDetector()



with open('model.pkl','rb') as f:
   Behaviour_model = pickle.load(f)


# taking video frame by frame
while cap.isOpened():
    rt,frame = cap.read()

    img , faces = FMD.findFaceMesh(frame)
    cvzone.putTextRect(frame, ('Person'), (10, 80))
    if faces:
        face = faces[0]
        face_data = list(np.array(face).flatten())
       

        try:
            # feeding newpoints to model for prediction
            result = Behaviour_model.predict([face_data])
            cvzone.putTextRect(frame, str(result[0]), (250, 80))
            print(result)

            # resultproba = Behaviour_model.predict_proba([face_data])
            # print(resultproba)

        except Exception as e:
            pass
        
        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv2.imshow('SKIBIDI INMOOV', frame)
    cv2.waitKey(1)