# Cryptography Lab 1

This lab contains implementations and analysis tools for classical ciphers including Caesar, Affine, and Vigenère ciphers.

## Files Structure

- `a_1.py`: Interactive cipher implementation with encryption/decryption functionality
- `a_2.py`: Letter frequency analysis tool with visualization
- `b.py`: Cryptanalysis tools for breaking classical ciphers
- `crypto/`: Module containing cipher implementations
  - `caesar.py`: Caesar cipher implementation
  - `affine.py`: Affine cipher implementation
  - `vigenere.py`: Vigenère cipher implementation
  - `utils.py`: Shared utilities and constants

## Usage

### Interactive Cipher Tool (a_1.py)

Run the interactive tool to encrypt/decrypt messages using different ciphers:

```bash
python a_1.py
```

Options:

1. Caesar Cipher - Simple shift cipher
2. Affine Cipher - Linear transformation cipher
3. Vigenère Cipher - Polyalphabetic substitution cipher
4. Exit
5. Run Tests - Executes test cases for all ciphers

### Frequency Analysis Tool (a_2.py)

Visualize letter frequencies in Spanish text and compare with theoretical frequencies:

```bash
python a_2.py
```

Enter your text when prompted, and the tool will display a horizontal bar chart comparing the letter frequencies of your input text against theoretical Spanish language frequencies.

### Cryptanalysis Tool (b.py)

Attempts to break encrypted messages using frequency analysis:

```bash
python b.py
```

The tool will analyze encrypted texts from the `ciphers/` directory:

- `caesar.txt`: Caesar-encrypted text
- `afines.txt`: Affine-encrypted text
- `vigenere.txt`: Vigenère-encrypted text

For each cipher type, it will display potential decryptions ranked by how well they match Spanish language letter frequencies.

## Spanish Alphabet

The implementation uses the Spanish alphabet (27 letters including 'ñ'):

```
abcdefghijklmnñopqrstuvwxyz
```

## Note

This is an educational implementation focused on classical ciphers. These ciphers are not secure for real-world encryption and should only be used for learning purposes.
