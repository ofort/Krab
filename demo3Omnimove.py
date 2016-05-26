import serial
import time
import RPi.GPIO as GPIO
from dynamixel import AX12A
from omnimove import omnimove

#  myOmnimove = omnimove([0x0002, 0x0011, 0x0010, 0x0012], 18)
myOmnimove = omnimove([2, 17, 16, 18], 18)

myOmnimove.moveForwardRel(0.5)
time.sleep(2)

myOmnimove.moveBackwardRel(0.5)
time.sleep(2)

myOmnimove.moveLeftRel(0.5)
time.sleep(1)

myOmnimove.moveRightRel(0.5)
time.sleep(1)

myOmnimove.stop()
time.sleep(1)

myOmnimove.turnCcwRel(0.5)
time.sleep(1)

myOmnimove.turnCwRel(0.5)
time.sleep(1)

print("stop")
myOmnimove.stop()
