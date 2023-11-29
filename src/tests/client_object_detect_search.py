import sys
sys.path.append("../")

from modules import detectWithSearchName, writeCommunicator

query = "bottle"

quad = detectWithSearchName('test1.jpeg', str(query))

writeCommunicator(quad)
