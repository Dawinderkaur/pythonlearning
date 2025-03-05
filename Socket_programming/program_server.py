#Simple Server-Client program
#------------------------------------------------ Server------------------------------------------
# A server has a bind() method which binds it to a specific IP and port so that it can listen to incoming requests on that IP and port.
# A server has a listen() method which puts the server into listening mode.
# This allows the server to listen to incoming connections.
# And last a server has an accept() and close() method.
# The accept method initiates a connection with the client and the close method closes the connection with the client.

# first of all import the socket library
import socket

# next create a socket object
s = socket.socket()
print ("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345, but it can be anything
port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print ("socket bind to %s" %port)

# put the socket into listening mode
# 5 here means that 5 connections are kept waiting if the server is busy
# and if a 6th socket tries to connect then the connection is refused.
s.listen(5)
print ("socket is listening")

# a forever loop until we interrupt it or
# an error occurs
while True:

    # Establish connection with client.
    client_socket, client_address = s.accept()
    print ('Got connection from', client_address )

    # send a thankyou message to the client. encoding to send byte type.
    client_socket.send('Thank you for connecting'.encode())

    # Close the connection with the client
    client_socket.close()

    # Breaking once connection closed
    break

# make a while loop and start to accept all incoming connections and
# close those connections after a thankyou message to all connected sockets