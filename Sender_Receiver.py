# UDP multicast examples, Hugo Vincent, 2005-05-14.
import socket

if __name__=="__main__":
        sequence_id = 0
        my_IP = 63 #Change this to IP of node
        # Create the socket
        socket_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #IPv4, UDP : Sender
        socket_recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #IPv4, UDP : Receiver
        # Make the socket multicast-aware, and set TTL.
        socket_send.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) #Broadcasting, Option changed to 1
        # Multicast compatible, Enabling binding to the address and port combination that is in use
        socket_recv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
                socket_recv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        except AttributeError:
                pass 

        socket_recv.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_TTL, 20) # Multicast with TTL 20
        socket_recv.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_LOOP, 1) # Receiving own multicast message

        socket_recv.bind(('', 5005)) # Bind to our port
        socket_recv.settimeout
        while True:
                data = b""
                try:
                        data = socket_recv.recv(1024) # Receiving 1024 bytes
                        print("Recieved message: " + str(data[2:].decode()))
                        if sequence_id != data[0]:    # Not Seen the packet before, Accept
                                sequence_id = data[0]
                                if data[1] != my_IP: # Transmit further else do nothing
                                        print("Braodcasting packet with squence number "+ str(sequence_id))
                                        socket_send.sendto(data,(("192.168.210.255",5005))) #Broadcasting 
                        else: # Seen the packet before, Reject
                                print("Rejected packet with squence number"+ str(sequence_id))
                except socket.timeout:
                        pass
                except KeyboardInterrupt:
                        destination = int(input("Enter Destination IP last byte: "))
                        data_packet = str(input("Enter 1 byte of data for the packet: "))
                        sequence_id+=1
                        socket_send.sendto(bytearray([sequence_id,destination])+data_packet.encode(),(("192.168.210.255",5005))) #Broadcasting
