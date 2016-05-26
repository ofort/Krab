import serial
import time
import RPi.GPIO as GPIO
from dynamixel import AX12A
from omnimove import omnimove

#  myOmnimove = omnimove([0x0002, 0x0011, 0x0010, 0x0012], 18)
myOmnimove = omnimove([2, 17, 16, 18], 18)

myOmnimove.moveForwardRel(0.2)
time.sleep(1)
myOmnimove.moveForwardRel(0.5)
time.sleep(1)
myOmnimove.moveForwardRel(1)
time.sleep(1)
print("stop")
time.sleep(1)
myOmnimove.moveBackwardRel(1)
time.sleep(1.3)

print("stop")
myOmnimove.stop()
