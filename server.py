import socket

s= socket.socket()

s.bind(('localhost',8787))

s.listen(4)

print('waiting for connection')

while True:
    a, address= s.accept()
    p = a.recv(1024).decode()
    print("connected with", address,p)

    a.send(bytes("toh kese he app log ",'utf-8'))
    a.close()

