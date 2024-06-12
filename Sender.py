import socket
#import numpy
UDP_IP = "192.168.210.255"
UDP_PORT = 5005
MESSAGE = b"Hello World"

sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP
s = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 10) # Change TTL (=20) to suit
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
sock.bind((UDP_IP, UDP_PORT))

while True:
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    #data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    #print("received message: %s" % data)
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)



