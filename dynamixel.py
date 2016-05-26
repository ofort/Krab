import serial
import time
import math
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

port = serial.Serial("/dev/ttyAMA0", baudrate=1000000, timeout=3.0)

class AX12A(object):
	def __init__(self, idmotor = 0, pindir = 18):
		self._pindir = pindir
		self._idmotor = idmotor
		
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self._pindir, GPIO.OUT)
		GPIO.output(self._pindir, GPIO.HIGH)

		self.goalAngle = 1
		self.goalSpeed = 2
		self.cw = 0
		self.ccw = 1
		self._sync = False
		return
	
	def sendMotor(self, trame):
		GPIO.output(18, GPIO.LOW)
		port.write( bytearray(trame) )
		time.sleep(0.1)
		GPIO.output(18, GPIO.HIGH)
		return

	def makeTrame(self, codes = []):
		codes = [self._idmotor] + [len(codes) + 1] + codes
		n = 0
		for i in codes:
			n = n + i
		n = (~n & 0xFF)
		return [0xFF, 0xFF] + codes + [n]
	
	def setMode(self, mode = 1):
		if mode == self.goalAngle:
			trame = self.makeTrame([0x03, 0x06, 0x00, 0x00, 0xFF, 0x03])
			self.sendMotor(trame)
		if mode == self.goalSpeed:
			trame = self.makeTrame([0x03, 0x06, 0x00, 0x00, 0x00, 0x00])
			self.sendMotor(trame)
		return
	
	def setSpeed(self, speed, sens):
		if sens == self.cw:
			speed = speed | 0x0400
		speedL = speed & 0xFF
		speedH = (speed >> 8) & 0xFF
		cmd = 0x03			# commande write
		if self._sync:
			cmd = 0x04		# commande write register (pour synchroniser)
		trame = self.makeTrame([cmd, 0x20, speedL, speedH ])
		self.sendMotor(trame)
		return
	
	def setSignedSpeed(self, speed) :
		if speed >= 0 :
			sens = self.cw
		else :
			sens = self.ccw
		speed = abs(speed)

		if sens == self.cw:
			speed = speed | 0x0400
		speedL = speed & 0xFF
		speedH = (speed >> 8) & 0xFF
		cmd = 0x03			# commande write
		if self._sync:
			cmd = 0x04		# commande write register (pour synchroniser)
		trame = self.makeTrame([cmd, 0x20, speedL, speedH ])
		self.sendMotor(trame)
		return
	


	def setAngle(self, angle):
		angleL = angle & 0xFF
		angleH = (angle >> 8) & 0xFF
		cmd = 0x03			# commande write
		if self._sync:
			cmd = 0x04		# commande write register (pour synchroniser)
		trame = self.makeTrame([cmd, 0x1E, angleL, angleH ])
		self.sendMotor(trame)
		return

	def setSync(self, sync = False):
		self._sync = sync
		return
	
	def sendSync(self):
		self.sendMotor([0xFF, 0xFF, 0xFE, 0x02, 0x05, 0xFA])
		return

	def changeID(self, newID):
		trame = self.makeTrame([0x03, 0x03, newID])
		self.sendMotor(trame)
		self._idmotor = newID
		return
