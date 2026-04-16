import socket, ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

bindsocket = socket.socket()
bindsocket.bind(('localhost', 8080))
bindsocket.listen(1)

print("SSL Server waiting...")

newsocket, addr = bindsocket.accept()
conn = context.wrap_socket(newsocket, server_side=True)

print("Connected:", addr)

while True:
    data = conn.recv(1024).decode()
    print("Client:", data)

    msg = input("You: ")
    conn.send(msg.encode())