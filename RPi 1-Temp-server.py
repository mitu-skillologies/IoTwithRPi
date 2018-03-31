import socket

s =socket.socket()
#create a socket object
s.bind(("192.168.43.44",65531)) #Bind to the port
s.listen(5)
c, addr = s.accept()

while True:
    print 'Got connection from', addr
    data = c.recv(1024)
    print (data)
c.close()

