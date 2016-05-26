import serial
import time
import RPi.GPIO as GPIO
from dynamixel import AX12A
from omnimove import omnimove

#  myOmnimove = omnimove([0x0002, 0x0011, 0x0010, 0x0012], 18)
myOmnimove = omnimove([2, 17, 16, 18], 18)

time.sleep(10)

myOmnimove.moveVector([1., 0.], 50)
time.sleep(30)
myOmnimove.stop()
myOmnimove.moveVector([1., 0.], 100)
time.sleep(30)
myOmnimove.stop()
myOmnimove.moveVector([1., 0.], 200)
time.sleep(30)
myOmnimove.stop()
myOmnimove.moveVector([1., 0.], 400)
time.sleep(30)
myOmnimove.stop()
myOmnimove.moveVector([1., 0.], 600)
time.sleep(30)
myOmnimove.stop()
myOmnimove.moveVector([1., 0.], 800)
time.sleep(30)
myOmnimove.stop()
myOmnimove.moveVector([1., 0.], 1000)
time.sleep(30)
myOmnimove.stop()
