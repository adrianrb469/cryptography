from .utils import ALPHABET, clean_text, mod_inverse, gcd

def affine_cipher(message: str, encrypt: bool = True) -> str:
    while True:
        try:
            a = int(input('Enter multiplicative key (must be coprime with alphabet length): '))
            if gcd(a, len(ALPHABET)) != 1:
                print("Key must be coprime with alphabet length")
                continue
            b = int(input('Enter additive key: '))
            if 0 <= b < len(ALPHABET):
                break
            print(f"Additive key must be between 0 and {len(ALPHABET)-1}")
        except ValueError:
            print("Please enter valid numbers")
    
    if not encrypt:
        a_inv = mod_inverse(a, len(ALPHABET))
        a, b = a_inv, (-a_inv * b) % len(ALPHABET)
        
    result = ''
    for c in message.lower():
        if c in ALPHABET:
            pos = (a * ALPHABET.index(c) + b) % len(ALPHABET)
            result += ALPHABET[pos]
        else:
            result += c
    return result

if __name__ == "__main__":
    message = input('\nEnter message: ')
    message = clean_text(message)
    
    print("\n--- Affine Cipher ---")
    encrypted = affine_cipher(message, encrypt=True)
    print(f'Encrypted: {encrypted}')
    decrypted = affine_cipher(encrypted, encrypt=False)
    print(f'Decrypted: {decrypted}') 