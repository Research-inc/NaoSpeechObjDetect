import sys
sys.path.append("../")

from modules import detectWithSearchName_v2, isObjectPresent, magnifier, closenessHelper, generateTextFromSpeech, writeCommunicator

import numpy as np
import cv2 as cv

query = generateTextFromSpeech().lower()

prev_height = None
new_height = None
prev_detect = None

def directionHelper(quad):
    if quad == "first":
        direction = "angleright"
    elif quad == "second":
        direction = "right"
    elif quad == "third":
        direction = "left"
    else:
        direction = "angleleft"
    return direction


cap = cv.VideoCapture(0)


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
    print(query)
    if isObjectPresent('output.jpg', str(query)): #to check if the object is detected or not. If detected, there will be some value
        quad, width, height = detectWithSearchName_v2('output.jpg', str(query))
        frame = cv.imread("result.jpg")
        prev_detect = True
        if prev_height is None:
            prev_height = height
            new_height = height
        else:
            prev_height = new_height
            new_height = height
            direction = directionHelper(quad)
            magnification = magnifier(prev_height, new_height)
            writeCommunicator(direction)
            if direction == "left" or direction == "right":
                if magnification < 1.5:
                    writeCommunicator("forward")#write which quad is it to the communicator module

    else:
        prev_detect = False
    # Display the resulting frame
    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

