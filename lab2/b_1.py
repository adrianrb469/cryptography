import base64

def decrypt_image(file_path, key, output_file):
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()

    decrypted_data = bytearray()
    for i, byte in enumerate(encrypted_data):
        decrypted_data.append(byte ^ key[i % len(key)])  # Make sure key is same length as encrypted data!

    with open(output_file, 'wb') as f:
        f.write(decrypted_data)


if __name__ == '__main__':
    decrypt_image('imagen_xor.png', b'cifrados_2025', 'original_image.png')
