from utils import ALPHABET

def vigenere_cipher(text, key, encrypt=True):
    result = ""
    key = key.upper()
    key_length = len(key)
    key_as_int = [ALPHABET.find(i) for i in key] 
    
    for i, char in enumerate(text):
        if char in ALPHABET:
            key_idx = key_as_int[i % key_length] # Makes the key repeat if it's shorter than the text!
            
            char_idx = ALPHABET.find(char)
            
            if encrypt:
                new_idx = (char_idx + key_idx) % len(ALPHABET)
            else:
                new_idx = (char_idx - key_idx) % len(ALPHABET)
                
            result += ALPHABET[new_idx]
        else:
            result += char
            
    return result 