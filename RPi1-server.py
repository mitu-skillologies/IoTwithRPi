import socket

s =socket.socket()
#create a socket object
s.bind(("192.168.43.17",65531)) #Bind to the port
while True:
    s.listen(5)

    c, addr = s.accept()
    print 'Got connection from', addr
    data = c.recv(1024)
    print (data)
    c.close()
    
