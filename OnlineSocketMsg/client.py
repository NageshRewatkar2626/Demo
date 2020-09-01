import socket
import sys  
import time

s = socket.socket()  
host = input(str("please enter host name : "))
port =1234
# try:
s.connect((host,port))
print("connected to server")

# except:
    # print("connection server failed")

while 1:
    incoming_msg = s.recv(1024)
    incoming_msg = incoming_msg.decode()
    print("Server:>>",incoming_msg)

    msg = input(str("You:>>"))
    msg = msg.encode()
    s.send(msg)
