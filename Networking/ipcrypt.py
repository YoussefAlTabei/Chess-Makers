import struct

# Encryption Key (16-byte)
KEY = 'Mina ba3ny pain '  # Example key, 16 bytes

# Rotation function (rotate left by r bits)
def rotl(b, r):
    return ((b << r) & 0xff) | (b >> (8 - r))

# Forward permutation function
def permute_fwd(state):
    (b0, b1, b2, b3) = state
    b0 += b1
    b2 += b3
    b0 &= 0xff
    b2 &= 0xff
    b1 = rotl(b1, 2)
    b3 = rotl(b3, 5)
    b1 ^= b0
    b3 ^= b2
    b0 = rotl(b0, 4)
    b0 += b3
    b2 += b1
    b0 &= 0xff
    b2 &= 0xff
    b1 = rotl(b1, 3)
    b3 = rotl(b3, 7)
    b1 ^= b2
    b3 ^= b0
    b2 = rotl(b2, 4)
    return (b0, b1, b2, b3)

# Backward permutation function
def permute_bwd(state):
    (b0, b1, b2, b3) = state
    b2 = rotl(b2, 4)
    b1 ^= b2
    b3 ^= b0
    b1 = rotl(b1, 5)
    b3 = rotl(b3, 1)
    b0 -= b3
    b2 -= b1
    b0 &= 0xff
    b2 &= 0xff
    b0 = rotl(b0, 4)
    b1 ^= b0
    b3 ^= b2
    b1 = rotl(b1, 6)
    b3 = rotl(b3, 3)
    b0 -= b1
    b2 -= b3
    b0 &= 0xff
    b2 &= 0xff
    return (b0, b1, b2, b3)

# XOR function to combine values
def xor4(x, y):
    return [(x[i] ^ y[i]) & 0xff for i in (0, 1, 2, 3)]

# Encrypt function
def encrypt(ip, key=KEY):
    """Encrypt an IP address using a 16-byte key"""
    k = [struct.unpack('<B', x.encode())[0] for x in key]  # Convert key to bytes
    try:
        state = [int(x) for x in ip.split('.')]  # Split IP into octets
    except ValueError:
        raise ValueError("Invalid IP format")
    
    # Perform XOR and permutations as per the encryption algorithm
    state = xor4(state, k[:4])
    state = permute_fwd(state)
    state = xor4(state, k[4:8])
    state = permute_fwd(state)
    state = xor4(state, k[8:12])
    state = permute_fwd(state)
    state = xor4(state, k[12:16])

    return '.'.join(str(x) for x in state)  # Return encrypted IP as a string

# Decrypt function
def decrypt(ip, key=KEY):
    """Decrypt an encrypted IP address using a 16-byte key"""
    k = [struct.unpack('<B', x.encode())[0] for x in key]  # Convert key to bytes
    try:
        state = [int(x) for x in ip.split('.')]  # Split encrypted IP into octets
    except ValueError:
        raise ValueError("Invalid IP format")
    
    # Perform reverse XOR and permutations as per the decryption algorithm
    state = xor4(state, k[12:16])
    state = permute_bwd(state)
    state = xor4(state, k[8:12])
    state = permute_bwd(state)
    state = xor4(state, k[4:8])
    state = permute_bwd(state)
    state = xor4(state, k[:4])

    return '.'.join(str(x) for x in state)  # Return decrypted IP as a string

# Test encryption and decryption
if __name__ == "__main__":
    original_ip = '192.168.1.1'
    print("Original IP:", original_ip)
    
    encrypted_ip = encrypt(original_ip)
    print("Encrypted IP:", encrypted_ip)
    
    decrypted_ip = decrypt(encrypted_ip)
    print("Decrypted IP:", decrypted_ip)
