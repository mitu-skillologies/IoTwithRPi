import httplib, urllib
import time, Adafruit_DHT
sleep = 60 # how many seconds to sleep between posts to the channel
key = '0G07MA3RRN5F5SI4'  # Thingspeak channel to update
# Channel No: 336236
def thermometer():
    while True:
        h, t = Adafruit_DHT.read_retry(11,4)
	print "Temp:", t
        params = urllib.urlencode({'field1': t, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print response.status, response.reason
            data = response.read()
            conn.close()
        except:
            print "connection failed"

thermometer()
