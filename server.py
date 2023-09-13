import socket

HOST = '127.0.0.1'  # Listen on all available interfaces
PORT = 65010        # Port on which the server runs

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port
sock.bind((HOST, PORT))

print(f"Listening on {HOST}:{PORT}")

# Endless loop to receive and print data
while True:
    data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
    print(f"Received from {addr}: {data.decode('utf-8')}")
