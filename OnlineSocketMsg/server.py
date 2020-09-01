import socket
import sys  
import time

s = socket.socket()  
host = socket.gethostname()
print("server wil start on host : ",host)
port = 1234
s.bind((host,port))
print("server is bind sucessful")
s.listen(1)
conn,addr = s.accept()
print(addr,'has connected')

while 1:
    msg = input(str("You:>>"))
    msg = msg.encode()
    conn.send(msg)
    incoming_msg = s.recv(1024)
    incoming_msg = incoming_msg.decode()
    print("Client:>>",incoming_msg)
   
