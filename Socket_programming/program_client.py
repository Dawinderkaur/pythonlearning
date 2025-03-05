# Client side program
# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1', port))

# receive data from the server and decoding to get the string.
print(s.recv(1024).decode())
# close the connection
s.close()

# s.recv()
# is a method of the socket object s.
# It receives up to 1024 bytes of data from the socket.
# The 1024 is the buffer size, meaning it will read up to 1024 bytes at a time. If the data is larger, it will need multiple calls to recv().
#
# .decode()
# The received data is in bytes format (b'some data'), which isn't human-readable.
# .decode() converts it from bytes to a string using UTF-8 encoding by default.