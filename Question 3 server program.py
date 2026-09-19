import socket

HOST = "127.0.0.1"
PORT = 5000

try:
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((HOST, PORT))

    # Listen for incoming connections
    server_socket.listen(1)

    print("Server is waiting for a connection...")

    # Accept a client connection
    client_socket, address = server_socket.accept()

    print("Connected to:", address)

    # Receive message
    message = client_socket.recv(1024).decode()

    print("Message received:", message)

    # Close connections
    client_socket.close()
    server_socket.close()

except socket.error as error:
    print("Network error:", error)

