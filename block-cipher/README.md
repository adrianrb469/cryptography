# Block Cipher Implementations

This exercise provides implementations of various block cipher algorithms and modes of operation in Go.

## Implemented Algorithms

### 1. DES with ECB Mode

- **Data Encryption Standard (DES)** with Electronic Codebook (ECB) mode
- 56-bit key (8 bytes with parity bits)
- Manual PKCS#7 padding implementation

### 2. 3DES with CBC Mode

- **Triple DES** with Cipher Block Chaining (CBC) mode
- 168-bit key (24 bytes)
- Random initialization vector (IV)
- PKCS#7 padding

### 3. AES with ECB and CBC Modes

- **Advanced Encryption Standard (AES-256)** with both ECB and CBC modes
- 256-bit key (32 bytes)
- Random initialization vector (IV) for CBC mode
- PKCS#7 padding

## Project Structure

```
block-cipher/
├── crypto/
│   ├── aes/
│   │   ├── aes.go         # AES implementation (ECB and CBC modes)
│   │   └── aes_test.go    # AES tests
│   ├── des/
│   │   ├── des.go         # DES implementation (ECB mode)
│   │   └── des_test.go    # DES tests
│   ├── tripledes/
│   │   ├── tripledes.go   # 3DES implementation (CBC mode)
│   │   └── tripledes_test.go # 3DES tests
│   └── image_test.go      # Image encryption demo test
├── utils/
│   ├── padding.go         # PKCS#7 padding utilities
│   └── padding_test.go    # Padding tests
├── bill.png               # Test image for ECB vs CBC demonstration
└── main.go                # Demo application
```

## Usage

Run the demo application:

```bash
go run main.go
```

This will demonstrate:

- DES encryption and decryption in ECB mode
- 3DES encryption and decryption in CBC mode
- AES encryption and decryption in both ECB and CBC modes
- A visual demonstration of why ECB mode is not secure for data with patterns

## Tests

The project includes comprehensive unit tests for all cipher implementations. The tests demonstrate the functionality of each cipher and include educational information about the algorithms.

### Running Tests

To run all tests:

```bash
go test ./... -v
```

To run tests for a specific package:

```bash
go test ./crypto/aes -v
go test ./crypto/des -v
go test ./crypto/tripledes -v
go test ./utils -v
```

### Test Highlights

1. **DES Tests**: Includes information about the DES algorithm as a 16-round Feistel network with a 56-bit key.

2. **Triple DES Tests**: Demonstrates how 3DES addresses the key length weakness of DES.

3. **AES Tests**: Tests both ECB and CBC modes, showing how ECB preserves patterns while CBC does not.

4. **Image Encryption Demo**: A visual demonstration using `bill.png` to show why ECB mode is insecure for encrypting images.

   When you run this test:

   ```bash
   go test ./crypto -run TestImageEncryption -v
   ```

   It creates encrypted versions of the image in the `output` directory:

   - `bill_ecb.png`: The image encrypted with ECB mode (patterns from the original image may be visible)
   - `bill_cbc.png`: The image encrypted with CBC mode (should appear completely random)
   - `bill_ecb_decrypted.png` and `bill_cbc_decrypted.png`: The decrypted images (should match the original)

5. **Padding Tests**: Verify the PKCS#7 padding implementation with various data sizes and edge cases.

## Security Considerations

- **DES** is considered insecure for modern applications due to its small key size (56 bits).
- **ECB mode** does not hide data patterns and is generally not recommended for secure applications.
- **3DES** provides better security than DES but is slower than AES.
- **AES with CBC mode** is a good choice for many applications, but more modern modes like GCM (Galois/Counter Mode) provide both encryption and authentication.

## License

This project is for educational purposes only.
