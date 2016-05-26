import serial
import time
import RPi.GPIO as GPIO
from dynamixel import AX12A

mot1 = AX12A(1, 18)
mot2 = AX12A(2, 18)

mot1.setSync(True)			# passe en mode synchronisation
mot2.setSync(True)

mot1.setMode(mot1.goalAngle)	# passe en mode angle
mot2.setMode(mot2.goalAngle)

mot1.setSpeed(0x0100, mot1.cw)
mot2.setSpeed(0x03FF, mot2.cw)
mot1.sendSync()			# un seul suffit car envoi en broadcast


mot1.setAngle(0x0000)
mot2.setAngle(0x03FF)
mot1.sendSync()			# un seul suffit car envoi en broadcast, les 2 moteurs démarrent synchronisés 

time.sleep(2)

mot1.setAngle(0x03FF)
mot2.setAngle(0x0000)
mot1.sendSync()

time.sleep(2)

mot1.setMode(mot1.goalSpeed)	#passe en mode vitesse
mot2.setMode(mot2.goalSpeed)

mot1.setSpeed(0x03FF, mot1.cw)
mot2.setSpeed(0x0200, mot2.cw)
mot1.sendSync()			# un seul suffit car envoi en broadcast

time.sleep(2)


mot1.setSpeed(0x0000, mot1.cw)
mot2.setSpeed(0x0000, mot2.cw)
mot1.sendSync()			# un seul suffit car envoi en broadcast


mot1.setMode(mot1.goalAngle)
mot2.setMode(mot2.goalAngle)

mot1.setSpeed(0x00F0, mot1.cw)
mot2.setSpeed(0x00F0, mot2.cw)
mot1.sendSync()			# un seul suffit car envoi en broadcast

mot1.setAngle(0x03FF)
mot2.setAngle(0x0000)
mot1.sendSync()
