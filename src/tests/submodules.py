import sys
sys.path.append("../")

from modules import detectWithSearchName, generateTextFromSpeech

quad = detectWithSearchName('object.jpg', "book")

query = generateTextFromSpeech().lower()