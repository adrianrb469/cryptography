# Cryptography Lab 3

This repository contains practical implementations of various cryptographic techniques including AES encryption, ChaCha20 cipher, and analysis of encryption modes with real-world applications.

## Prerequisites

- Python 3.x
- pycryptodome library
- Other dependencies in individual part requirements.txt files

## Part 1: Breaking ECB in Images

Demonstrates the weaknesses of ECB encryption mode when applied to structured data like images.

### Running the code

```bash
cd pt1
jupyter notebook main.ipynb
```

This notebook compares AES-ECB and AES-CBC encryption on images, showing how ECB mode preserves patterns in the original image making it insecure for certain types of data.

## Part 2: Capturing Encrypted Network Traffic with Wireshark

Analyzes network traffic containing AES-CBC encrypted data.

### Running the code

```bash
cd pt2
pip install -r requirements.txt

# Start the server in one terminal
python server.py

# In another terminal, run the client
python client.py
```

Capture the traffic using Wireshark to observe that encrypted data doesn't reveal content patterns but still exposes communication patterns.

## Part 3: ChaCha20 vs AES Performance Comparison

Compares performance between AES and ChaCha20 stream cipher.

### Running the code

```bash
cd pt3
pip install -r requirements.txt
jupyter notebook main.ipynb
```

This notebook performs benchmarks on both algorithms with various message sizes, measuring encryption time and memory usage.

## Part 4: Simulated Ransomware Implementation

Demonstrates how ransomware encrypts files using AES and how recovery works.

### Running the code

```bash
cd pt4
jupyter notebook main.ipynb
```

The notebook shows:

1. Creation of sample files
2. Encryption of files using AES-CBC (simulating ransomware)
3. Recovery process using the encryption key

## Key Findings

- ECB mode reveals patterns in structured data like images, making it unsuitable for many applications
- CBC mode offers better security by chaining blocks together
- ChaCha20 is generally faster than AES for larger data sets and uses less memory
- Proper key management is critical for security in all encryption systems

## Security Considerations

This code is for educational purposes only. The ransomware simulation is a learning tool to understand how such attacks work and how to protect against them.
