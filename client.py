import socket

a = socket.socket()

a.connect(('localhost', 8787))
name = input('enter your name')

a.send(bytes(name, 'utf-8'))

print(a.recv(1024).decode())
