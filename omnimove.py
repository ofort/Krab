"""Classe représentant un véhicule holonome a 4 roues MECANUM

	composé de 4 roues-moteurs : omniMotor[] 0 à 3"""

"""
Motor 0 : front right wheel
Motor 1 : rear right wheel
Motor 2 : rear left wheel
Motor 3 : front left wheel

Motors		 0	 1	 2	 3
___________________________________________
Forward		cw	CW	CCW 	CCW
Backward	CW	CCW	CW	CW
TurnCW	 	CCW 	CCW 	CCW 	CCW
TurnCCW 	CW  	CW	CW	CW
Right		CW	CCW 	CCW   	CW
Left		CCW 	CW	CW  	CCW
"""

from dynamixel import AX12A
import math

class omnimove(object):

	def __init__(self, idsmotors = [1, 2, 3, 4], pindir = 18):
		#definir les moteurs
		self._idsMotors = idsmotors
		self._pindir = 18
		self.motors = []
		i = 0
		for mot in self._idsMotors:
			self.motors.append(AX12A(mot, self._pindir))
			self.motors[i].setMode(self.motors[i].goalSpeed)
			self.motors[i].setSync(True) #Les moteurs démarrent et stoppent de manière synchronisée
			i += 1
		return

	def _speed(self, relSpeed):    #Compute absolute speed from relative speed
		if relSpeed < 0:
			speed = 0
		elif relSpeed > 100:
			speed = 1023
		else :
			speed = int(relSpeed * 1023)

		return speed

	def moveForward(self, speed = 0):    #move forward at absolute speed
		self.motors[0].setSpeed(speed, self.motors[0].cw)
		self.motors[1].setSpeed(speed, self.motors[1].cw)
		self.motors[2].setSpeed(speed, self.motors[2].ccw)
		self.motors[3].setSpeed(speed, self.motors[3].ccw)

		self.motors[0].sendSync()
		return

	def moveForwardRel(self, relSpeed = 0): #move forward at a fraction of max speed
		speed = self._speed(relSpeed)  	    #Compute absolute speed from relative speed
		self.motors[0].setSpeed(speed, self.motors[0].cw)
		self.motors[1].setSpeed(speed, self.motors[1].cw)
		self.motors[2].setSpeed(speed, self.motors[2].ccw)
		self.motors[3].setSpeed(speed, self.motors[3].ccw)

		self.motors[0].sendSync()
		return

	def moveBackward(self, speed = 0):
		self.motors[0].setSpeed(speed, self.motors[0].ccw)
		self.motors[1].setSpeed(speed, self.motors[1].ccw)
		self.motors[2].setSpeed(speed, self.motors[2].cw)
		self.motors[3].setSpeed(speed, self.motors[3].cw)

		self.motors[0].sendSync()
		return

	def moveBackwardRel(self, relSpeed = 0):
		speed = self._speed(relSpeed)    #Compute absolute speed from relative speed
		self.motors[0].setSpeed(speed, self.motors[0].ccw)
		self.motors[1].setSpeed(speed, self.motors[1].ccw)
		self.motors[2].setSpeed(speed, self.motors[2].cw)
		self.motors[3].setSpeed(speed, self.motors[3].cw)

		self.motors[0].sendSync()
		return

	def moveLeft(self, speed = 0):
		self.motors[0].setSpeed(speed, self.motors[0].cw)
		self.motors[1].setSpeed(speed, self.motors[1].ccw)
		self.motors[2].setSpeed(speed, self.motors[2].ccw)
		self.motors[3].setSpeed(speed, self.motors[3].cw)

		self.motors[0].sendSync()
		return

	def moveLeftRel(self, relSpeed = 0):
		speed = self._speed(relSpeed)    #Compute absolute speed from relative speed
		self.motors[0].setSpeed(speed, self.motors[0].cw)
		self.motors[1].setSpeed(speed, self.motors[1].ccw)
		self.motors[2].setSpeed(speed, self.motors[2].ccw)
		self.motors[3].setSpeed(speed, self.motors[3].cw)

		self.motors[0].sendSync()
		return

	def moveRight(self, speed = 0):
		self.motors[0].setSpeed(speed, self.motors[0].ccw)
		self.motors[1].setSpeed(speed, self.motors[1].cw)
		self.motors[2].setSpeed(speed, self.motors[2].cw)
		self.motors[3].setSpeed(speed, self.motors[3].ccw)

		self.motors[0].sendSync()
		return

	def moveRightRel(self, relSpeed = 0):
		speed = self._speed(relSpeed)    #Compute absolute speed from relative speed
		self.motors[0].setSpeed(speed, self.motors[0].ccw)
		self.motors[1].setSpeed(speed, self.motors[1].cw)
		self.motors[2].setSpeed(speed, self.motors[2].cw)
		self.motors[3].setSpeed(speed, self.motors[3].ccw)

		self.motors[0].sendSync()
		return

	def turnCw(self, speed = 0):
		self.motors[0].setSpeed(speed, self.motors[0].ccw)
		self.motors[1].setSpeed(speed, self.motors[1].ccw)
		self.motors[2].setSpeed(speed, self.motors[2].ccw)
		self.motors[3].setSpeed(speed, self.motors[3].ccw)

		self.motors[0].sendSync()
		return

	def turnCwRel(self, relSpeed = 0):
		speed = self._speed(relSpeed)    #Compute absolute speed from relative speed
		self.motors[0].setSpeed(speed, self.motors[0].ccw)
		self.motors[1].setSpeed(speed, self.motors[1].ccw)
		self.motors[2].setSpeed(speed, self.motors[2].ccw)
		self.motors[3].setSpeed(speed, self.motors[3].ccw)

		self.motors[0].sendSync()
		return

	def turnCcw(self, speed = 0):
		self.motors[0].setSpeed(speed, self.motors[0].cw)
		self.motors[1].setSpeed(speed, self.motors[1].cw)
		self.motors[2].setSpeed(speed, self.motors[2].cw)
		self.motors[3].setSpeed(speed, self.motors[3].cw)

		self.motors[0].sendSync()
		return

	def turnCcwRel(self, relSpeed = 0):
		speed = self._speed(relSpeed)    #Compute absolute speed from relative speed
		self.motors[0].setSpeed(speed, self.motors[0].cw)
		self.motors[1].setSpeed(speed, self.motors[1].cw)
		self.motors[2].setSpeed(speed, self.motors[2].cw)
		self.motors[3].setSpeed(speed, self.motors[3].cw)

		self.motors[0].sendSync()
		return

	def stop(self):
		self.motors[0].setSpeed(0x0000, self.motors[0].cw)
		self.motors[1].setSpeed(0x0000, self.motors[1].cw)
		self.motors[2].setSpeed(0x0000, self.motors[2].cw)
		self.motors[3].setSpeed(0x0000, self.motors[3].cw)

		self.motors[0].sendSync()
		return

	def moveVector(self, vector = [1., 0], speed = 0):  #default = moveFront()
		vectorLength = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
		for i in range(2):
			vector[i] /= vectorLength
			vector[i] *= speed
			vector[i] = int(vector[i])

		self.motors[0].setSignedSpeed(int(vector[0]) - int(vector[1])) # CW donc 0 - 1
		self.motors[1].setSignedSpeed(int(vector[0]) + int(vector[1])) # CW
		self.motors[2].setSignedSpeed(int(vector[1]) - int(vector[0])) # CCW 
		self.motors[3].setSignedSpeed(-1*(int(vector[1]) + int(vector[0]))) # CCW

		self.motors[0].sendSync()
		return

	def movePolar(self, vector = [1., 0], unit = 0):  #default = moveFront()
		# unit = 0 : degre
		# unit = 1 : radian
		_Pi = math.atan(1.)
		
		if unit == 0:     #si angle en degré
			vector[0] = _Pi * vector[0] / 360

		vectorLength = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
		v0 = vector[0] * math.cos(vector[1])
		v1 = vector[0] * math.sin(vector[1])

		self.motors[0].setSignedSpeed(int(v0) - int(v1)) # CW donc 0 - 1
		self.motors[1].setSignedSpeed(int(v0) + int(v1)) # CW
		self.motors[2].setSignedSpeed(int(v1) - int(v0)) # CCW 
		self.motors[3].setSignedSpeed(-1*(int(v1) + int(v0))) # CCW

		self.motors[0].sendSync()
		return

