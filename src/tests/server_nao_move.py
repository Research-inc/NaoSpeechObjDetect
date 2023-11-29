import sys
sys.path.append("../")

from modules import pointArm, pointArmBasedOnQuad, readCommunicator

NAO_IP = "192.168.171.80"  # Replace with the actual IP address of your Nao robot
#NAO_IP = "192.168.171.151"  # Replace with the actual IP address of your Nao robot


quad = str(readCommunicator())

pointArmBasedOnQuad(NAO_IP, quad, 0.0)

