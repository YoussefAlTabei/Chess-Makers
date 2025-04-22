import socket

HOST = '0.0.0.0'
PORT = 65432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("Waiting for a connection...")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

try:
    while True:
        # Host sends first
        msg = input("Your move: ")
        if msg.lower() in ('exit', 'quit'):
            print("Exiting game.")
            break
        conn.sendall(msg.encode())

        # Then receives
        data = conn.recv(1024).decode()
        if not data:
            print("Client disconnected.")
            break
        print(f"Opponent played: {data}")
except Exception as e:
    print(f"Error: {e}")
finally:
    conn.close()
    server_socket.close()
