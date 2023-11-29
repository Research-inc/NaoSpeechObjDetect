import sys
sys.path.append("../")

from modules import detectWithSearchName, generateTextFromSpeech, writeCommunicator

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

query = None

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imwrite("output.jpg", frame)

    #speech recognition
    if not query:
        query = generateTextFromSpeech().lower()
    else:
        quad = detectWithSearchName('output.jpg', str(query))
        if quad is not None: #to check if the object is detected or not. If detected, there will be some value
            frame = cv.imread("result.jpg")
            writeCommunicator(quad) #write which quad is it to the communicator module


    # Display the resulting frame
    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

