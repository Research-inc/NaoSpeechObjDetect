import sys
sys.path.append("../")

from modules import detectWithSearchName_v2, isObjectPresent, magnifier, closenessHelper, generateTextFromSpeech, writeCommunicator

import numpy as np
import cv2 as cv
import time
query = generateTextFromSpeech().lower()

prev_height = None
new_height = None
prev_detect = None
prev_direction = "partialright"
num_failed_detects = 0

def directionHelper(quad):
    if quad == "first":
        direction = "partialright"
    elif quad == "second":
        direction = "partialright"
    elif quad == "third":
        direction = "partialleft"
    else:
        direction = "partialleft"
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
        num_failed_detects = 0
        writeCommunicator("forward")
        prev_direction = directionHelper(quad)
        time.sleep(2)

    else:
        if num_failed_detects < 12:
            writeCommunicator(prev_direction)
            time.sleep(2)
            num_failed_detects += 1

    # Display the resulting frame
    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

