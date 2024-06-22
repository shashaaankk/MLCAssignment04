import socket
if __name__=="__main__":

        sequence_id = 0     # Sequence ID
        my_IP = 64          # Last byte of WiFi IP of the current node #CHANGE HERE
        data_packet = ""    # Data to be sent
        myRouteDict = {}    # Dictionary stores the arriving routes

        # Creating datagram sockets (UDP)
        socket_send_uni = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Sending via unicast
        socket_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)      # Forward path 
        socket_recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  

        # Making the socket multicast-aware, and set TTL.
        socket_send.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)   # Broadcasting, Option changed to 1 
        socket_recv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # Bind to the address and port combination that is in use
        try:
                socket_recv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        except AttributeError:
                pass 

        socket_recv.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_TTL, 20)  # Multicast with TTL 20
        socket_recv.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_LOOP, 1)  # Receiving own multicast message

        socket_recv.bind(('', 5005))        # Binding to our port
        socket_recv.settimeout
        while True:
                data = b""
                try:
                        data = socket_recv.recv(1024)                      # Receiving 1024 bytes
                        addresses = data[3:]                               # Last Byte of address
                        print("Data frame: " + str([b for b in data]))
                        if sequence_id < data[0]:                          # Acceptence check
                                # Transmission
                                sequence_id = data[0]
                                if data[1] != my_IP and data[2] == 0 :     # data[1]: Last byte of Destination IP; data[2] == 0-> Broadcast; data[2] == 1-> RREP; data[2] == 2-> Using obtained route;
                                        print("Broadcasting packet with squence number"+ str(sequence_id))
                                        socket_send.sendto(data+bytearray([my_IP]),(("192.168.210.255",5005))) # Broadcast
                                elif data[1] != my_IP and data[2] == 1 :   # Route Reply via unicast
                                        print("RREP"+ str(sequence_id))    
                                        myRouteDict.put(int(addresses[-1]),addresses)
                                        socket_send_uni.sendto(data,(("192.168.210."+str(addresses[addresses.index(my_IP)-1]),5005)))
                                elif data[1] != my_IP and data[2] == 2:    # Data Transfer
                                       print("Data Transfer"+ str(sequence_id))
                                       addr_lst = myRouteDict.get(data[1])
                                       socket_send_uni.sendto(data,(("192.168.210."+str(addr_lst[addr_lst.index(my_IP)+1]),5005))) # Data Transfer 
                                # Reception         
                                else:
                                    if data[2]==1: #RREP Reception, Store address and Send Data
                                        print("Creating Entry")
                                        #print("Addresses: " + str([b for b in addresses]))
                                        myRouteDict[int(addresses[-1])] = addresses
                                        #print(myRouteDict)                                    
                                        for dest in myRouteDict:
                                            route = myRouteDict[dest]
                                            formatted_route = ", ".join(f'"{r}"' for r in route) 
                                            print(f'{dest} : [{formatted_route}]')
                                        sequence_id+=1 # Prepare to send Data
                                        rrep_flag = 2  # prepare to send Data
                                        #print(int(addresses[-1]))
                                        socket_send_uni.sendto(bytearray([sequence_id,int(addresses[-1]),rrep_flag])+data_packet.encode(),(("192.168.210."+str(addresses[addresses.index(my_IP)+1]),5005))) #Data
                                    elif data[2]==2: #Data Receiption
                                        print("Recieved data: "+addresses.decode())
                                    else:
                                        print("starting rrep") # Request Received, Sending RREP via Unicast
                                        sequence_id+=1
                                        socket_send_uni.sendto(bytearray([sequence_id,int(addresses[0]),1])+addresses+bytearray([my_IP]),(("192.168.210."+str(addresses[-1]),5005)))
                        else:               
                                print("Rejected packet with sequence number "+ str(sequence_id))
                except socket.timeout:
                        pass
                except KeyboardInterrupt:
                        destination = int(input("Enter Destination IP last byte: "))
                        data_packet = str(input("Enter 1 byte of data for the packet: "))  
                        sequence_id+=1
                        if myRouteDict.get(destination) is None:
                                rrep_flag = 0
                                socket_send.sendto(bytearray([sequence_id,destination,rrep_flag,my_IP]),(("192.168.210.255",5005)))
                        else:
                                rrep_flag = 2 
                                addr_lst = myRouteDict.get(destination)
                                socket_send_uni.sendto(bytearray([sequence_id,int(addr_lst[-1]),rrep_flag])+data_packet.encode(),(("192.168.210."+str(addr_lst[addr_lst.index(my_IP)+1]),5005)))
                          