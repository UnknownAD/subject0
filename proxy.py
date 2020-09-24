#!/usr/bin/python3
import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=int(__import__('sys').argv[1])
server.bind(("localhost",port))
print(port)
server.listen(3)
conn,addr=server.accept()
print(f"$ Well ...we have a new guess --> {addr[0]}:{addr[1]}")
while True:
    cmd=input("$ ")
    if len(cmd)>0:
        conn.send(bytes(cmd,"ascii"))
        res=conn.recv(2048).decode('ascii')
        if len(res)>0:
            print(res)
