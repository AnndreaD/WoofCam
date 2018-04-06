#! /usr/bin/python3

import socket
import os
import select


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="158.38.101.215"
port =5001
s.connect((host,port))

def _checkdata_():
    is_readable = [s]
    is_writable = []
    is_error =[]
    r,w,e = select.select(is_readable,is_writable,is_error)
    if r:
        _getdata_()
    else:
        sleep(100)
    
def _senddata_(str):
   s.send(str.encode())

def _getdata_():
    data = ''
    data = s.recv(1024).decode()
    print (data)

    if 'turn' in data:
      os.system("python3 servo.py")
      _senddata_('treat given')
    elif 'stream' in data:
        os.system("sudo service motion start")
    elif 'stop' in data:
        os.system("sudo service motion stop")
    elif 'quit' in data:
   	    s.close()

while True:
    _checkdata_()
    
    