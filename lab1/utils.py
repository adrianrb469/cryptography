ALPHABET = 'abcdefghijklmnñopqrstuvwxyz'

def clean_text(text: str) -> str:
    return ''.join(c for c in text.lower() if c in ALPHABET or c.isspace())

def mod_inverse(a: int, m: int) -> int:
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("Modular multiplicative inverse does not exist") 

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a