import socket
import sys


client  = socket.socket()
client.connect(('localhost',9999))
while True:
    imp = input("input:")
    if imp:
        client.send(imp.encode())
        data = client.recv(1024)
        print(data.decode())
    else:
        client.close()
        break
client.close()