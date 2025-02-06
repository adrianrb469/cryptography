from .utils import ALPHABET, clean_text
from typing import Optional

def caesar_cipher(message: str, shift: Optional[int] = None, encrypt: bool = True) -> str:
    if shift is None:
        shift = int(input(f'Enter shift value (1-{len(ALPHABET)-1}): '))
        while not (0 < shift < len(ALPHABET)):
            print(f"Shift must be between 1 and {len(ALPHABET)-1}")
            shift = int(input(f'Enter shift value (1-{len(ALPHABET)-1}): '))
    
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