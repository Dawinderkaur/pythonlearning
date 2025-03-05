# Example of a script for connecting to google
# programming in Python
import socket # for socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print ("Socket successfully created")
except socket.error as err:
	print ("socket creation failed with error %s" %(err))

# default port for socket
port = 80

try:
	host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror: #getaddrinfo()
	# this means could not resolve the host
	print ("there was an error resolving the host")
	sys.exit()

# connecting to the server
s.connect((host_ip, port))

print ("the socket has successfully connected to google")

# For sending data the socket library has a sendall function.
# This function allows you to send data to a server to which the socket is connected
# and the server can also send data to the client using this function.