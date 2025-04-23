import socket
import ipcrypt
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't have to connect; just helps get the local IP used for outgoing
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

print("Local IP:", get_local_ip())

encrypted_ip = (ipcrypt.encrypt(get_local_ip())).split('.')
print("Encrypted IP:", encrypted_ip)
encrypted_ip = [hex(int(x)) for x in encrypted_ip]
print(encrypted_ip)