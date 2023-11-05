import sys
sys.path.append("../")

from modules import detectWithSearchName, generateTextFromSpeech


query = generateTextFromSpeech().lower()

quad = detectWithSearchName('object.jpg', str(query))
