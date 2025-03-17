#!/usr/bin/env python3
from Crypto.Random import get_random_bytes
import base64

def generate_key():
    key = get_random_bytes(32)
    
    key_b64 = base64.b64encode(key).decode('utf-8')
    
    with open('encryption.key', 'w') as f:
        f.write(key_b64)
    
    print("[*] New AES-256 key generated and saved to 'encryption.key'")
    print("[*] Key (base64):", key_b64)

if __name__ == "__main__":
    generate_key() 