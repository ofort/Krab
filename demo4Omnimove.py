import serial
import time
import RPi.GPIO as GPIO
from dynamixel import AX12A
from omnimove import omnimove

#  myOmnimove = omnimove([0x0002, 0x0011, 0x0010, 0x0012], 18)
myOmnimove = omnimove([2, 17, 16, 18], 18)

time.sleep(5)

myOmnimove.moveVector([1., 0.], 400)
time.sleep(2)
myOmnimove.stop()

myOmnimove.moveVector([-1., -1.], 400)
time.sleep(2)
myOmnimove.stop()

myOmnimove.moveVector([-1., -2.], 400)
time.sleep(2)
myOmnimove.stop()

myOmnimove.moveVector([1., 2.], 400)
time.sleep(2)
myOmnimove.stop()

myOmnimove.turnCw(400)
time.sleep(2)
myOmnimove.stop()

myOmnimove.turnCcw(400)
time.sleep(2)
myOmnimove.stop()

myOmnimove.movePolar([300., 25], 0)
time.sleep(2)
myOmnimove.stop()

myOmnimove.movePolar([-300., 25], 0)
time.sleep(2)
myOmnimove.stop()
