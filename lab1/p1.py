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
        
        choice = input("\nEnter choice (1-4): ")
        
        if choice == '4':
            break
            
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
            print("Invalid choice! Please select 1-4")