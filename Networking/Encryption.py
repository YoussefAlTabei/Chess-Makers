import socket
import Networking.ipcrypt as ipcrypt
import random
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
def Generate_room_code():
    '''
    Encrypts the local IP address and generates a room code.
    Returns:
        str: A hexadecimal string representing the generated room code.
    '''
    encrypted_ip = (ipcrypt.encrypt(get_local_ip())).split('.')
    print("Encrypted IP:", encrypted_ip)
    encrypted_ip = [hex(int(x)) for x in encrypted_ip]
   # print(encrypted_ip)
    rand = random.randrange(1, 16)
   # print("Random number:", rand)
    encrypted_ip = [hex(int(x, 16) - rand) for x in encrypted_ip]
    encrypted_ip.insert(0,rand)
    room_code = ""
    for e in encrypted_ip:
        if type(e) == int:
            room_code += hex(e).strip("0x")
        #pass
        else:
            room_code += e[2:]
    print("Room code:", room_code , "length :", len(room_code))
    return room_code
code = Generate_room_code()

def decrypt_room_code(code):
    '''
    Decrypts the room code to retrieve the original IP address.
    Args:
        code (str): The room code to decrypt.
    Returns:    
        str: The decrypted IP address.
    '''
    key = int(code[0], 16)
    #print("Key:", key)
    code = code[1:]
    ip_lst = []
    for i in range(0,len(code),2):
       # print(i)
        ip_lst.append(code[i:(i+2)])
        #code = code[(i+2):]
    #print(ip_lst)
    ip_lst = [hex(int(x, 16) + key) for x in ip_lst]
    #print(ip_lst)
    ip_lst = [int(x, 16) for x in ip_lst]
  #  print(ip_lst)
    ip = '.'.join(map(str, ip_lst))
   # print(ip)
    IP = ipcrypt.decrypt(ip)
    print("Decrypted IP:", IP)
    return IP
print(decrypt_room_code(code))