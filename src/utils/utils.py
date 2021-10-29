import os
import cv2
import pickle
import pyttsx3
from dotenv import load_dotenv
load_dotenv()

base_dir = os.getenv("BASE_DIR")

def load_recognise():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("train.yml")

    labels = {"person_name": 1}
    with open("labels.pickle", "rb") as f:
        labels = pickle.load(f)
        labels = {v: k for k, v in labels.items()}

    return (recognizer, labels)


def text_to_speech():
    engine = pyttsx3.init()
    rate = engine.getProperty("rate") # 'rate' is redundant
    engine.setProperty("rate", 175)

    return (engine, rate)


def detect_face():
    face_cascade = cv2.CascadeClassifier(
        os.path.join(base_dir, 'haarcascade/haarcascade_frontalface_default.xml')
    )
    cap = cv2.VideoCapture(0)

    return (face_cascade, cap)



