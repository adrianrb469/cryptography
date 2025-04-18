from binascii import unhexlify
from utils.zoro_rc4 import rc4_decrypt

# Came from: ~/ONEPIECE/East_Blue/Shells_Town/Casa_de_Helmeppo/
encrypted_hex = "8d2829fc80da28979d3afaa5001df42dfd31519bd18d85b53dec8e7edde4ca9e44175769d5"
encrypted_bytes = unhexlify(encrypted_hex)

carne = "21691"
decrypted = rc4_decrypt(encrypted_bytes, carne)
print(f"{decrypted.decode('utf-8', errors='ignore')}")