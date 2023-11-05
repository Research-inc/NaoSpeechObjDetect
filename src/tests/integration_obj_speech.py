import sys
sys.path.append("../")

from modules import detectWithSearchName, generateTextFromSpeech


query = generateTextFromSpeech().lower()

detectWithSearchName('object.jpg', str(query))
