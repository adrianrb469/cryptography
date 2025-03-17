#!/usr/bin/env python3
import socket
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode
import base64

with open('encryption.key', 'r') as f:
    KEY = base64.b64decode(f.read().strip())

HOST = '10.100.6.75'
PORT = 6000

def decrypt_message(encrypted_data, iv):
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    return decrypted_data.decode('utf-8')

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"[*] Escuchando en {HOST}:{PORT}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"[*] Conexión aceptada de {address[0]}:{address[1]}")
        
        try:
            data = client_socket.recv(4096).decode('utf-8')
            if not data:
                continue
                
            encrypted_package = json.loads(data)
            
            iv = b64decode(encrypted_package['iv'])
            encrypted_data = b64decode(encrypted_package['encrypted'])
            
            decrypted_message = decrypt_message(encrypted_data, iv)
            print(f"[*] Mensaje descifrado: {decrypted_message}")
            
            client_socket.send("Mensaje recibido y descifrado correctamente".encode('utf-8'))
            
        except Exception as e:
            print(f"[!] Error: {e}")
        finally:
            client_socket.close()

if __name__ == "__main__":
    main() 