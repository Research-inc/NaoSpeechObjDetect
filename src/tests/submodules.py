import sys
sys.path.append("../")

from modules import detectWithSearchName, generateTextFromSpeech

detectWithSearchName('object.jpg', "book")

query = generateTextFromSpeech().lower()