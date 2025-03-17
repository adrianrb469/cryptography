#!/usr/bin/env python3
import socket
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64encode
import base64

with open('encryption.key', 'r') as f:
    KEY = base64.b64decode(f.read().strip())
    
HOST = '192.168.56.1'
PORT = 9443

def encrypt_message(message):
    iv = get_random_bytes(AES.block_size)
    
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    
    message_bytes = message.encode('utf-8')
    padded_message = pad(message_bytes, AES.block_size)
    encrypted_data = cipher.encrypt(padded_message)
    
    iv_b64 = b64encode(iv).decode('utf-8')
    encrypted_b64 = b64encode(encrypted_data).decode('utf-8')
    
    return {
        'iv': iv_b64,
        'encrypted': encrypted_b64
    }

def send_message(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((HOST, PORT))
        
        encrypted_package = encrypt_message(message)
        
        client_socket.send(json.dumps(encrypted_package).encode('utf-8'))
        
        response = client_socket.recv(1024).decode('utf-8')
        print(f"[*] Respuesta del servidor: {response}")
        
    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        client_socket.close()

def main():
    while True:
        message = input("Ingresa el mensaje a enviar (o 'salir' para terminar): ")
        if message.lower() == 'salir':
            break
        send_message(message)

if __name__ == "__main__":
    main() 