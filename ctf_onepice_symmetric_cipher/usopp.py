from utils.usopp_cipher import decrypt

b64_flag = "a77742694e4957811d303a3d8294897a1e6b0a65c94819dc101e24b315fe9082ee1956d938"

flag = decrypt(b64_flag)

print(flag)
