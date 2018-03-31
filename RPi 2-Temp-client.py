import socket
import sys
import Adafruit_DHT

s = socket.socket()
port = 65531
s.connect(("192.168.43.17", port))
while True:
    hum, temp = Adafruit_DHT.read_retry(11, 4)
    print('Temp:%f Humidity: ' %(temp))
    s.send(str(temp))
s.close
