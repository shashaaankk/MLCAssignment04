# UDP multicast examples, Hugo Vincent, 2005-05-14.
import socket

def send(data, port=50000, addr='239.192.1.100'):
        """send(data[, port[, addr]]) - multicasts a UDP datagram."""
        # Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Make the socket multicast-aware, and set TTL.
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 20) # Change TTL (=20) to suit
        # Send the data
        s.sendto(data, (addr, port))

def recv(port=50000, addr="239.192.1.100", buf_size=1024):
        """recv([port[, addr[,buf_size]]]) - waits for a datagram and returns the data."""

        # Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Set some options to make it multicast-friendly
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        except AttributeError:
                pass # Some systems don't support SO_REUSEPORT
        s.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_TTL, 20)
        s.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_LOOP, 1)

        # Bind to the port
        s.bind(('', port))
        # Set some more multicast options
        intf = socket.gethostbyname(socket.gethostname())
        s.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(intf))
        #s.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(addr) + socket.inet_aton(intf))

        # Receive the data, then unregister multicast receive membership, then close the port
        data, sender_addr = s.recvfrom(buf_size)
        #s.setsockopt(socket.SOL_IP, socket.IP_DROP_MEMBERSHIP, socket.inet_aton(addr) + socket.inet_aton('0.0.0.0'))
        s.close()
        return data

if __name__=="__main__":
        sequence_id = 0
        my_IP = 64
        # Create the socket
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
                        print("recieved message: " + str(data[2:].decode()))
                        if sequence_id != data[0]:
                                sequence_id = data[0]
                                if data[1] != my_IP:
                                        print("Braodcasting packet with squence number"+ str(sequence_id))
                                        socket_send.sendto(data,(("129.69.210.255",5005)))
                        else:
                                print("Rejected packet with squence number"+ str(sequence_id))
                except socket.timeout:
                        pass
                except KeyboardInterrupt:
                        destination = int(input("Enter Destination IP last byte: "))
                        data_packet = str(input("Enter 1 byte of data for the packet: "))
                        sequence_id+=1
                        socket_send.sendto(bytearray([sequence_id,destination])+data_packet.encode(),(("129.69.210.255",5005)))
