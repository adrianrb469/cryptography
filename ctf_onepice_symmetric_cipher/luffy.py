def xor_cipher(text: bytes, key: bytes):
    repeated_key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
    return bytes([a ^ b for a, b in zip(text, repeated_key)])

def bytes_to_string(bytes_data: bytes):
    return bytes_data.decode('utf-8')

# Came from: ./East_Blue/Arlong_Park/Casa_de_Genzo/flag.txt 
hex_string = "747d777e6e51090f09060501550d0205570f0e0607000f0a0703070f08535103570c020402"

xored = xor_cipher(bytes.fromhex(hex_string), b"21691")

print(bytes_to_string(xored))
