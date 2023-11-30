import sys
sys.path.append("../")

from modules import walk, walkWithDirection, readCommunicator

NAO_IP = "192.168.171.80"  # Replace with the actual IP address of your Nao robot
#NAO_IP = "192.168.171.151"  # Replace with the actual IP address of your Nao robot

try:
    while True:
        direction = str(readCommunicator())
        walkWithDirection(NAO_IP, direction)
        #quadrant algorithm is changed to walk algorithm
except KeyboardInterrupt:
    pass
