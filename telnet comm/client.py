import socket

s = socket.socket()
s.connect(('localhost', 8080))

while True:
    msg = input("You: ")
    s.send(msg.encode())

    data = s.recv(1024).decode()
    print("Server:", data)