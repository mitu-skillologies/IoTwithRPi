# LED FADE IN & OUT | USE PIEZO TOO

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

p = GPIO.PWM(18,100)
p.start(0)

try:
	while True: 
		for i in range(100):
				p.ChangeDutyCycle(i)
				time.sleep(0.01)
		for i in range (100):
				p.ChangeDutyCycle(100-i)
				time.sleep(0.01)
except KeyboardInterrupt:
	pass
	p.stop()
	GPIO.cleanup()

