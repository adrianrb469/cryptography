from utils.nami_chacha import chacha20_decrypt

# Came from ./ONEPIECE/Water_7/Carpenters_Cafe/Casa_de_Iceburg/
hex_flag = "39b854c26445f476e6dde867552535bd89e902eaa35e6e0ebafa3d9f906f51fecf284cd897"

student_id = "21691"

ciphertext_bytes = bytes.fromhex(hex_flag)

try:
    decrypted_flag = chacha20_decrypt(ciphertext_bytes, student_id)
    print(f"Decrypted Flag: {decrypted_flag}")
except Exception as e:
    print(f"An error occurred during decryption: {e}")
