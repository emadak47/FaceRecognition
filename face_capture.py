import cv2
import os
from dotenv import load_dotenv
load_dotenv()

def faceCapture(user_name, num_images):
    base_dir = os.path.dirname(os.path.abspath(__file__))

    faceCascade = cv2.CascadeClassifier(
        os.path.join(base_dir, 'haarcascade/haarcascade_frontalface_default.xml')
    )

    video_capture = cv2.VideoCapture(0)

    if not os.path.exists(os.path.join(base_dir, 'data/{}'.format(user_name))):
        os.mkdir(os.path.join(base_dir, 'data/{}'.format(user_name)))

    cnt = 1
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (80, 50)
    fontScale = 0.7
    fontColor = (102, 102, 225)
    lineType = 2

    # Open camera
    while cnt <= num_images:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        msg = "Saving {}'s Face Data [{}/{}]".format(user_name, cnt, num_images)
        cv2.putText(frame, msg,
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    lineType)



        # Display the resulting frame
        cv2.imshow('Video', frame)
        cv2.setWindowProperty('Video', cv2.WND_PROP_TOPMOST, 1)
        # Store the captured images in `data/Jack`
        cv2.imwrite(
            os.path.join(base_dir, "data/{}/{}{:03d}.jpg".format(user_name, user_name, cnt)),
            frame
        )
        cnt += 1

        key = cv2.waitKey(100)

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    user_name = "Aayush"
    num_images = 400

    faceCapture(user_name, num_images)
