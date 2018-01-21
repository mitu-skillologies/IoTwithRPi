# TEMPERATURE & HUMIDITY SENSOR - Adafruit's DHT 11

import Adafruit_DHT as dht

while True: 
	h,t =dht .read_retry(11,4)
	print "Humidity",h
	print "Temp:",t
