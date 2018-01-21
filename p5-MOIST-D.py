# SOIL MOISTURE SENSOR (DIGITAL)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)

try:
	while True:
		i=GPIO.input(18)
		if i==0:
			print("wet")
			time.sleep(0.1)
		elif i==1:
			print("dry")
			time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit(0)
