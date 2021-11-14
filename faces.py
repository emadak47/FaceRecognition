import cv2
import pyttsx3
import pickle
from src.utils import get_user_id_from_name
from src.Customer import Customer
from src.Log import Log


def login_system():
    #1 Load recognize and read label from model
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("train.yml")

    labels = {"person_name": 1}
    with open("labels.pickle", "rb") as f:
        labels = pickle.load(f)
        labels = {v: k for k, v in labels.items()}

    # create text to speech
    engine = pyttsx3.init()
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 175)

    # Define camera and detect face
    face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    #2 Open the camera and start face recognition
    face_identify_counter = 0
    while face_identify_counter < 200:
        face_identify_counter += 1
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3)

        for (x, y, w, h) in faces:
            print(x, w, y, h)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            # predict the id and confidence for faces
            id_, conf = recognizer.predict(roi_gray)

            #2.1 If the face is recognized
            if conf >= 60:
                # print(id_)
                # print(labels[id_])
                font = cv2.QT_FONT_NORMAL
                id = 0
                id += 1
                name = labels[id_]
                current_name = name
                color = (255, 0, 0)
                stroke = 2
                cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))

                # Find the customer's information in the database.
                customer_id = get_user_id_from_name(current_name)

                # If the customer's information is not found in the database
                if customer_id == -1:
                    print("The customer", current_name, "is NOT FOUND in the database.")

                # If the customer's information is found in the database
                else:

                    customer = Customer(customer_id)
                    response = customer.get_user_details()

                    # Update the data in LogHistory
                    log = Log(customer_id)
                    log.insert_log()

                    hello = ("Hello ", current_name, "Welcom to the iKYC System")
                    print(hello)
                    engine.say(hello)
                    # engine.runAndWait()

                    cap.release()
                    cv2.destroyAllWindows()
                    return customer_id


            #2.2 If the face is unrecognized
            else: 
                color = (255, 0, 0)
                stroke = 2
                font = cv2.QT_FONT_NORMAL
                cv2.putText(frame, "UNKNOWN", (x, y), font, 1, color, stroke, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))
                hello = ("Your face is not recognized")
                print(hello)
                engine.say(hello)
                # engine.runAndWait()

        cv2.imshow('iKYC System', frame)
        cv2.setWindowProperty('iKYC System', cv2.WND_PROP_TOPMOST, 1)
        k = cv2.waitKey(20) & 0xff
        if k == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()
    return -1

if __name__ == '__main__':
    print(login_system())
