import socket

HOST = '192.168.1.104'  # Replace with actual host IP
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

try:
    while True:
        # Client receives first
        data = client_socket.recv(1024).decode()
        if not data:
            print("Server disconnected.")
            break
        print(f"Opponent played: {data}")

        # Then sends
        msg = input("Your move: ")
        if msg.lower() in ('exit', 'quit'):
            print("Exiting game.")
            break
        client_socket.sendall(msg.encode())
except Exception as e:
    print(f"Error: {e}")
finally:
    client_socket.close()
