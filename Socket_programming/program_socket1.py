#----------------------------------------------Socket Programming/ IPC Communication-----------------------------------------------
# It is way of connecting two nodes on a network to communicate with each other
# Socket programming allows two or more devices to communicate over a network (LAN, WAN, or the Internet).
# The network can be a logical, local network and physical network to connect external network
# Python provides the socket module to create client-server applications.

# Basics of Sockets:
# A Socket is an endpoint for sending or receiving data across a network.

# Types of Sockets:
# 1. TCP Sockets (SOCK_STREAM) -> Reliable, connection-based communication
# 2. UDP Sockets (SOCK_DGRAM) -> Fast, connectionless communication

# ------------------------------------------1. Creating a TCP Server -----------------------------------------

import socket

# Create a socket object (IPv4, TCP)
# created socket instance and passed it two parameters
# AF_INET refers to the address-family ipv4.
# The SOCK_STREAM means connection-oriented TCP protocol
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an IP and Port
server_socket.bind(("127.0.0.1", 12345))

#Listen for incoming connections
server_socket.listen(1)
print("Server is listening on port 12345....")

#Accept client connection
client_socket, client_address = server_socket.accept()
print(f"Connection establish with {client_address}")

#Receive data
data = client_socket.recv(1024).decode()
print(f"Client says: {data}")

#Send response
client_socket.send("Hello, Client!".encode())

#Close connection
client_socket.close()
server_socket.close()

#------------------------------------------------ 2: Creating a TCP Client---------------------------------------------
import socket

# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("127.0.0.1", 12345))

# Send data to the server
client_socket.send("Hello, Server!".encode())

# Receive response
response = client_socket.recv(1024).decode()
print(f"Server says: {response}")

# Close connection
client_socket.close()

#-------------------------------------------3. Creating a Simple UDP Server & Client-------------------------------
#UDP Server
import socket

# Create UDP socket
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_DGRAM for UDP

# Bind to an IP and Port
udp_server.bind(("127.0.0.1", 12345))

print("UDP Server is listening...")

# Receive data
data, client_addr = udp_server.recvfrom(1024)
print(f"Received from {client_addr}: {data.decode()}")

# Send response
udp_server.sendto("Hello, UDP Client!".encode(), client_addr)

# Close socket
udp_server.close()

#UDP Client
import socket

# Create UDP socket
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data to server
udp_client.sendto("Hello, UDP Server!".encode(), ("127.0.0.1", 12345))

# Receive response
data, server_addr = udp_client.recvfrom(1024)
print(f"Server says: {data.decode()}")

# Close socket
udp_client.close()


#--------------------------------------------4. Key Socket Methods----------------------------------------------------
# | Method | Description |
# |---------|------------|
# | `socket()` | Creates a new socket |
# | `bind()` | Binds socket to an address and port |
# | `listen()` | Waits for client connections (TCP) |
# | `accept()` | Accepts a client connection |
# | `connect()` | Connects to a server |
# | `send()` / `sendto()` | Sends data over a socket |
# | `recv()` / `recvfrom()` | Receives data from a socket |
# | `close()` | Closes the socket |


#---------------------------------------5. Advanced Socket Programming------------------------------------------------
# - **Multithreading** for handling multiple clients.
# - **Non-blocking sockets** for asynchronous communication.
# - **Secure Sockets Layer (SSL)** for encryption.
# - **WebSockets** for real-time communication.

