import string

ALPHABET = 'abcdefghijklmnñopqrstuvwxyz'  

def clean_text(text: str) -> str:
    return ''.join(c for c in text.lower() if c in ALPHABET or c.isspace())

def caesar_cipher(message: str, encrypt: bool = True) -> str:
    while True:
        try:
            shift = int(input(f'Enter shift value (1-{len(ALPHABET)-1}): '))
            if 0 < shift < len(ALPHABET):
                break
            print(f"Shift must be between 1 and {len(ALPHABET)-1}")
        except ValueError:
            print("Please enter a valid number")
    
    if not encrypt:
        shift = -shift
        
    result = ''
    for c in message.lower():
        if c in ALPHABET:
            pos = (ALPHABET.index(c) + shift) % len(ALPHABET)
            result += ALPHABET[pos]
        else:
            result += c
    return result

if __name__ == "__main__":
    while True:
        print("\n1. Caesar Cipher")
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

        else:
            print("Invalid choice! Please select 1-4")