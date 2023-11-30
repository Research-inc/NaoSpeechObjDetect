import sys
from .communicator import readCommunicator, writeCommunicator
#Condition check to see if python is 3 or not and import accordingly.
if sys.version_info > (3,6):
    from .objectdetect import detectWithSearchName, detectWithSearchName_v2, magnifier, closenessHelper, isObjectPresent
    from .SpeechRec import generateTextFromSpeech
else:
    from .naomove import pointArm, pointArmBasedOnQuad, walk, walkWithDirection