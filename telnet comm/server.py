import socket

s = socket.socket()
s.bind(('localhost', 8080))
s.listen(1)

print("Waiting for connection...")
conn, addr = s.accept()
print("Connected to", addr)

while True:
    data = conn.recv(1024).decode()
    print("Client:", data)

    msg = input("You: ")
    conn.send(msg.encode())