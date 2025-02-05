from utils import ALPHABET, clean_text
from caesar import caesar_cipher
from affine import affine_cipher
from vigenere import vigenere_cipher

if __name__ == "__main__":
    while True:
        print("\n1. Caesar Cipher")
        print("2. Affine Cipher")
        print("3. Vigenère Cipher")
        print("4. Exit")
        print("5. Run Tests")
        
        choice = input("\nEnter choice (1-4): ")
        
        if choice == '4':
            break
            
        if choice == '5':
            print("\n=== Running Cipher Tests ===")
            
            # Test Caesar Cipher
            test_msg = "HELLO WORLD"
            print("\nCaesar Cipher Test:")
            print(f"Original: {test_msg}")
            enc = caesar_cipher(test_msg, encrypt=True)
            dec = caesar_cipher(enc, encrypt=False)
            print(f"Encrypted: {enc}")
            print(f"Decrypted: {dec}")
            
            # Test Affine Cipher
            print("\nAffine Cipher Test:")
            print(f"Original: {test_msg}")
            enc = affine_cipher(test_msg, encrypt=True)
            dec = affine_cipher(enc, encrypt=False)
            print(f"Encrypted: {enc}")
            print(f"Decrypted: {dec}")
            
            # Test Vigenère Cipher
            test_key = "KEY"
            print("\nVigenère Cipher Test:")
            print(f"Original: {test_msg}")
            print(f"Key: {test_key}")
            enc = vigenere_cipher(test_msg, test_key, encrypt=True)
            dec = vigenere_cipher(enc, test_key, encrypt=False)
            print(f"Encrypted: {enc}")
            print(f"Decrypted: {dec}")
            continue
            
        message = input('\nEnter message: ')
        message = clean_text(message)  
        
        if choice == '1':
            print("\n--- Caesar Cipher ---")
            encrypted = caesar_cipher(message, encrypt=True)
            print(f'Encrypted: {encrypted}')
            decrypted = caesar_cipher(encrypted, encrypt=False)
            print(f'Decrypted: {decrypted}')
        
        elif choice == '2':
            print("\n--- Affine Cipher ---")
            encrypted = affine_cipher(message, encrypt=True)
            print(f'Encrypted: {encrypted}')
            decrypted = affine_cipher(encrypted, encrypt=False)
            print(f'Decrypted: {decrypted}')
            
        elif choice == '3':
            print("\n--- Vigenère Cipher ---")
            key = input('Enter key (letters only): ')
            key = clean_text(key)
            encrypted = vigenere_cipher(message, key, encrypt=True)
            print(f'Encrypted: {encrypted}')
            decrypted = vigenere_cipher(encrypted, key, encrypt=False)
            print(f'Decrypted: {decrypted}')

        elif choice == '4':
            break

        else:
            print("Invalid choice! Please select 1-5")