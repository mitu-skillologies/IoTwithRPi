import RPi.GPIO as GPIO
import time,signal,sys
GPIO.setmode(GPIO.BCM)
pinTrigger=18
pinEcho=24

def close(signal,frame):
	print("\nTurning off ultrsonic detection")
	GPIO.cleanup()
	sys.exit(0)

signal.signal(signal.SIGINT,close)
GPIO.setup(pinTrigger,GPIO.OUT)
GPIO.setup(pinEcho,GPIO.IN)

while True:
	GPIO.output(pinTrigger,True)
	time.sleep(0.00001)
	GPIO.output(pinTrigger,False)

	startTime=time.time()
	stopTime=time.time()

	while 0==GPIO.input(pinEcho):
		startTime=time.time()
	
	while 1==GPIO.input(pinEcho):
		stopTime=time.time()

	TimeElapsed=stopTime-startTime
	distance=(TimeElapsed*34300)/2

	print("Distance : %.1f cm" %distance)
	time.sleep(1)
	
 
