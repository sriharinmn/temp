import socket, ssl

context = ssl.create_default_context()

# For exam/demo (skip certificate verification)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

s = socket.socket()
conn = context.wrap_socket(s, server_hostname='localhost')

conn.connect(('localhost', 8080))

while True:
    msg = input("You: ")
    conn.send(msg.encode())

    data = conn.recv(1024).decode()
    print("Server:", data)