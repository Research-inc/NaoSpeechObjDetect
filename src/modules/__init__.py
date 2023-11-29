import sys

from .communicator import readCommunicator, writeCommunicator

#Condition check to see if python is 3 or not and import accordingly.
if sys.version_info > (3,6):
    from .objectdetect import detectWithSearchName
    from .SpeechRec import generateTextFromSpeech
else:
    from .naomove import pointArm, pointArmBasedOnQuad