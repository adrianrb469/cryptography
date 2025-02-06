from collections import Counter
from typing import List, Tuple
from crypto.utils import ALPHABET, mod_inverse, gcd
from crypto.vigenere import vigenere_cipher
import os

SPANISH_FREQ = {
    'a': 11.525, 'b': 2.215, 'c': 4.019, 'd': 5.010, 'e': 12.181,
    'f': 0.692, 'g': 1.768, 'h': 0.703, 'i': 6.247, 'j': 0.493,
    'k': 0.011, 'l': 4.967, 'm': 3.157, 'n': 6.712, 'o': 8.683,
    'p': 2.510, 'q': 0.877, 'r': 6.871, 's': 7.977, 't': 4.632,
    'u': 2.927, 'v': 1.138, 'w': 0.017, 'x': 0.215, 'y': 1.008,
    'z': 0.467, 'á': 0.502, 'é': 0.433, 'í': 0.725, 'ñ': 0.311,
    'ó': 0.827, 'ú': 0.168, 'ü': 0.012
}

def calculate_frequency_score(text: str) -> float:
    freq = Counter(c for c in text.lower() if c in ALPHABET)
    total = sum(freq.values())
    score = 0
    for char, count in freq.items():
        observed_freq = (count / total) * 100
        expected_freq = SPANISH_FREQ.get(char, 0)
        score += abs(observed_freq - expected_freq)
    return score  # Lower score = better match

def try_caesar(ciphertext: str, k: int = 5) -> List[Tuple[int, str, float]]:
    results = []
    for shift in range(1, len(ALPHABET)):
        decrypted = ""
        for c in ciphertext:
            if c in ALPHABET:
                pos = (ALPHABET.index(c) - shift) % len(ALPHABET)
                decrypted += ALPHABET[pos]
            else:
                decrypted += c
        score = calculate_frequency_score(decrypted)
        results.append((shift, decrypted, score))
    return sorted(results, key=lambda x: x[2])[:k]

def try_affine(ciphertext: str, k: int = 5) -> List[Tuple[int, int, str, float]]:
    results = []
    for a in range(1, len(ALPHABET)):
        if gcd(a, len(ALPHABET)) != 1:
            continue
        for b in range(len(ALPHABET)):
            decrypted = ""
            a_inv = mod_inverse(a, len(ALPHABET))
            for c in ciphertext:
                if c in ALPHABET:
                    pos = (a_inv * (ALPHABET.index(c) - b)) % len(ALPHABET)
                    decrypted += ALPHABET[pos]
                else:
                    decrypted += c
            score = calculate_frequency_score(decrypted)
            results.append((a, b, decrypted, score))
    return sorted(results, key=lambda x: x[3])[:k]

def try_vigenere(ciphertext: str, max_key_length: int = 6, k: int = 10) -> List[Tuple[str, str, float]]:
    results = []
    for key_length in range(2, max_key_length + 1):  
        possible_key = ['p', 'a'] + ['a'] * (key_length - 2)  
        # ! We know first two characters
        for i in range(2, key_length):
            best_char = 'a'
            best_score = float('inf')
            for _ in range(10):  
                for c in ALPHABET:
                    possible_key[i] = c
                    key = ''.join(possible_key)
                    decrypted = vigenere_cipher(ciphertext, key, encrypt=False)
                    score = calculate_frequency_score(decrypted)
                    if score < best_score:
                        best_score = score
                        best_char = c
            possible_key[i] = best_char
        key = ''.join(possible_key)
        decrypted = vigenere_cipher(ciphertext, key, encrypt=False)
        score = calculate_frequency_score(decrypted)
        results.append((key, decrypted, score))
    return sorted(results, key=lambda x: x[2])[:k]

def main():
    ciphers_dir = "ciphers"
    
    # Caesar cipher
    with open(os.path.join(ciphers_dir, "caesar.txt"), "r") as f:
        caesar_text = f.read().strip()
    print("\nCaesar Cipher Analysis:")
    for shift, text, score in try_caesar(caesar_text):
        print(f"Shift: {shift}, Score: {score:.2f}")
        print(f"Text: {text[:100]}...")

    # Affine cipher
    with open(os.path.join(ciphers_dir, "afines.txt"), "r") as f:
        affine_text = f.read().strip()
    print("\nAffine Cipher Analysis:")
    for a, b, text, score in try_affine(affine_text):
        print(f"a: {a}, b: {b}, Score: {score:.2f}")
        print(f"Text: {text[:100]}...")

    # Vigenère cipher
    with open(os.path.join(ciphers_dir, "vigenere.txt"), "r") as f:
        vigenere_text = f.read().strip()
    print("\nVigenère Cipher Analysis:")
    for key, text, score in try_vigenere(vigenere_text):
        print(f"Key: {key}, Score: {score:.2f}")
        print(f"Text: {text[:100]}...")

    print("\nThe following key was found manually by changing last letter for vigenere cipher.")
    key = "payaso"
    decrypted = vigenere_cipher(vigenere_text, key, encrypt=False)
    print(f"Key: {key}, Score: {score:.2f}")
    print(f"Text: {decrypted[:100]}...")


if __name__ == "__main__":
    main()
