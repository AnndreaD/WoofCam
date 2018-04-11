#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import time

s = socket.socket()         # Create a socket object
host = '158.38.101.215' # Get local machine name
port = 5001                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(1)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   time.sleep(10)
   c.send('turn')
   time.sleep(10)
   c.send('turn')
c.close()                # Close the connection


