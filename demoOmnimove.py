import serial
import time
import RPi.GPIO as GPIO
from dynamixel import AX12A
from omnimove import omnimove

#  myOmnimove = omnimove([0x0002, 0x0011, 0x0010, 0x0012], 18)
myOmnimove = omnimove([2, 17, 16, 18], 18)

print("Forward")
myOmnimove.moveForward(50)
time.sleep(20)
#print("backward")
#myOmnimove.moveBackward(0x00FF)
#time.sleep(3)
#print("Left")
#myOmnimove.moveLeft(0x00FF)
#time.sleep(3)
#print("Right")
#myOmnimove.moveRight(0x00FF)
#time.sleep(3)
#print("stop")
#myOmnimove.stop()

#time.sleep(3)

#myOmnimove.moveForwardRel(0.2)
#time.sleep(2)
#myOmnimove.moveForwardRel(0.5)
#time.sleep(2)

#print("stop")
#myOmnimove.stop()
