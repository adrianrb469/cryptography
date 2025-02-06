from .utils import ALPHABET, clean_text

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
    message = input('\nEnter message: ')
    message = clean_text(message)
    
    print("\n--- Caesar Cipher ---")
    encrypted = caesar_cipher(message, encrypt=True)
    print(f'Encrypted: {encrypted}')
    decrypted = caesar_cipher(encrypted, encrypt=False)
    print(f'Decrypted: {decrypted}') 