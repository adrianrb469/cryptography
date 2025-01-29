import random
import string

class CryptoUtils:
    # Base64 character set and padding
    B64_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    PADDING = '='

    @staticmethod
    def ascii_to_binary(text):
        return ''.join(format(b, '08b') for b in text.encode())

    @staticmethod
    def base64_to_binary(b64_text):
        bytes_data = CryptoUtils.b64_decode(b64_text)
        return ''.join(format(b, '08b') for b in bytes_data)

    @staticmethod
    def binary_to_base64(binary_str):
        bytes_data = bytes(int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8))
        return CryptoUtils.b64_encode(bytes_data)

    @staticmethod
    def binary_to_ascii(binary_str):
        bytes_data = bytes(int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8))
        return bytes_data.decode(errors='replace')

    @staticmethod
    def base64_to_ascii(b64_text):
        return CryptoUtils.binary_to_ascii(CryptoUtils.base64_to_binary(b64_text))

    @staticmethod
    def xor_binary(bin1, bin2):
        # Make sure both binary strings are of the same length
        repeated_bin2 = bin2 * (len(bin1) // len(bin2) + 1)
        
        result = []
        for b1, b2 in zip(bin1, repeated_bin2):
            xored_bit = str(int(b1) ^ int(b2))
            result.append(xored_bit)
            
        return ''.join(result)

    @staticmethod
    def generate_key(length):
        return ''.join(random.choice(string.printable.strip()) for _ in range(length))

    @staticmethod
    def b64_encode(data_bytes):
        encoded = []
        for i in range(0, len(data_bytes), 3):
            chunk = data_bytes[i:i+3]
            binary = ''.join(format(b, '08b') for b in chunk)
            
            # Pad with zeros if needed
            while len(binary) % 6 != 0:
                binary += '0'
            
            # Convert 6-bit groups to Base64 characters
            for j in range(0, len(binary), 6):
                index = int(binary[j:j+6].ljust(6, '0'), 2)
                encoded.append(CryptoUtils.B64_CHARS[index])
            
        # Add padding
        padding = (3 - (len(data_bytes) % 3)) % 3
        return ''.join(encoded) + CryptoUtils.PADDING * padding

    @staticmethod
    def b64_decode(b64_str):
        b64_str = b64_str.rstrip(CryptoUtils.PADDING)
        binary_str = []
        
        for char in b64_str:
            index = CryptoUtils.B64_CHARS.index(char)
            binary_str.append(format(index, '06b'))
        
        full_binary = ''.join(binary_str)
        bytes_data = bytearray()
        
        for i in range(0, len(full_binary), 8):
            byte_bits = full_binary[i:i+8].ljust(8, '0')
            bytes_data.append(int(byte_bits[:8], 2))
        
        # Remove padding bytes
        padding = len(b64_str) % 4
        if padding:
            del bytes_data[-padding:]
            
        return bytes(bytes_data)

def main():
    crypto = CryptoUtils()
    while True:
        print("\n1. ASCII→Bin\n2. B64→Bin\n3. Bin→B64\n4. Bin→ASCII\n5. B64→ASCII\n6. XOR\n7. Gen Key\n8. Fixed Cipher\n9. Dynamic Cipher\n10. Exit")
        choice = input("Choice: ")

        if choice == '1':
            print(crypto.ascii_to_binary(input("Text: ")))
        elif choice == '2':
            print(crypto.base64_to_binary(input("B64: ")))
        elif choice == '3':
            print(crypto.binary_to_base64(input("Bin: ")))
        elif choice == '4':
            print(crypto.binary_to_ascii(input("Bin: ")))
        elif choice == '5':
            print(crypto.base64_to_ascii(input("B64: ")))
        elif choice == '6':
            b1 = input("Bin1: ")
            b2 = input("Bin2: ")
            print(crypto.xor_binary(b1, b2))
        elif choice == '7':
            print(crypto.generate_key(int(input("Length: "))))
        elif choice == '8':
            text = input("Text: ")
            key = crypto.generate_key(16)
            cipher = crypto.binary_to_base64(crypto.xor_binary(
                crypto.ascii_to_binary(text),
                crypto.ascii_to_binary(key)
            ))
            print(f"Cipher: {cipher}\nKey: {key}")
        elif choice == '9':
            text = input("Text: ")
            key = crypto.generate_key(len(text))
            cipher = crypto.binary_to_base64(crypto.xor_binary(
                crypto.ascii_to_binary(text),
                crypto.ascii_to_binary(key)
            ))
            print(f"Cipher: {cipher}\nKey: {key}")
        elif choice == '10':
            break

if __name__ == "__main__":
    main()