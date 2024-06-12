import socket
if __name__=="__main__":
        sequence_id = 0
        my_IP = 64
        data_packet = ""
        sequences_served = False
        # Create the socket
        socket_send_uni = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Make the socket multicast-aware, and set TTL.
        socket_send.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 20) # Change TTL (=20) to suit
                # Create the socket
        socket_recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Set some options to make it multicast-friendly
        socket_recv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
                socket_recv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        except AttributeError:
                pass # Some systems don't support SO_REUSEPORT
        socket_recv.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_TTL, 20)
        socket_recv.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_LOOP, 1)

        # Bind to the port
        socket_recv.bind(('', 5005))
        socket_recv.settimeout
        while True:
                data = b""
                try:
                        data = socket_recv.recv(1024)
                        addresses = data[3:]
                        print("addresses: " + str([b for b in data]))
                        if sequence_id != data[0]:
                                sequence_id = data[0]
                                if data[1] > my_IP and not data[2] :
                                        print("Broadcasting packet with squence number"+ str(sequence_id))
                                        socket_send.sendto(data+bytearray([my_IP]),(("129.69.210.255",5005)))
                                elif data[1] > my_IP and data[2] and not sequences_served:
                                        socket_send.close()
                                        print("RREP"+ str(sequence_id))
                                        socket_send_uni.sendto(data,(("129.69.210."+str(addresses[addresses.index(my_IP)+1]),5005)))
                                else:
                                    if data[2]:
                                        print("creating entry")
                                        print("addresses: " + str([b for b in addresses]))
                                        sequence_id+=1
                                        rrep_flag = 0
                                        socket_send_uni.sendto(bytearray([sequence_id,int(addresses[-1]),rrep_flag,data_packet]),(("129.69.210."+str(addresses[addresses.index(my_IP)+1]),5005)))
                                    else:
                                        if not sequences_served:
                                            sequences_served = True
                                            sequence_id+=1
                                            socket_send_uni.sendto(bytearray([sequence_id,int(addresses[0]),1,my_IP])+addresses[::-1],(("129.69.210."+str(addresses[-1]),5005)))
                        else:
                                print("Rejected packet with sequence number"+ str(sequence_id))
                except socket.timeout:
                        pass
                except KeyboardInterrupt:
                        destination = int(input("Enter Destination IP last byte: "))
                        data_packet = str(input("Enter 1 byte of data for the packet: "))
                        sequence_id+=1
                        rrep_flag = 0
                        sequences_served  = False
                        socket_send.sendto(bytearray([sequence_id,destination,rrep_flag,my_IP]),(("129.69.210.255",5005)))
