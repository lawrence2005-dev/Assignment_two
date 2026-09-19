import socket

HOST = "127.0.0.1"
PORT = 5000

try:
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((HOST, PORT))

    # Message to send
    message = "Hello from client!"

    # Send message
    client_socket.send(message.encode())

    print("Message sent successfully.")

    # Close the connection
    client_socket.close()

except socket.error as error:
    print("Network error:", error)
