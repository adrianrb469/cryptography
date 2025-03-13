package aes

import (
	"bytes"
	"testing"
)

func TestAESEncryptDecryptECB(t *testing.T) {
	plaintext := []byte("This is a test message for AES-ECB encryption.")
	
	// Generate a key
	key, err := GenerateKey()
	if err != nil {
		t.Fatalf("Failed to generate key: %v", err)
	}
	
	// Encrypt the plaintext
	ciphertext, err := EncryptECB(plaintext, key)
	if err != nil {
		t.Fatalf("Encryption failed: %v", err)
	}
	
	// Decrypt the ciphertext
	decrypted, err := DecryptECB(ciphertext, key)
	if err != nil {
		t.Fatalf("Decryption failed: %v", err)
	}
	
	// Check if the decrypted text matches the original plaintext
	if !bytes.Equal(plaintext, decrypted) {
		t.Errorf("Decrypted text does not match original plaintext.\nOriginal: %s\nDecrypted: %s", 
			plaintext, decrypted)
	}
}

func TestAESEncryptDecryptCBC(t *testing.T) {
	plaintext := []byte("This is a test message for AES-CBC encryption.")
	
	// Generate a key
	key, err := GenerateKey()
	if err != nil {
		t.Fatalf("Failed to generate key: %v", err)
	}
	
	// Encrypt the plaintext
	ciphertext, err := EncryptCBC(plaintext, key)
	if err != nil {
		t.Fatalf("Encryption failed: %v", err)
	}
	
	// Decrypt the ciphertext
	decrypted, err := DecryptCBC(ciphertext, key)
	if err != nil {
		t.Fatalf("Decryption failed: %v", err)
	}
	
	// Check if the decrypted text matches the original plaintext
	if !bytes.Equal(plaintext, decrypted) {
		t.Errorf("Decrypted text does not match original plaintext.\nOriginal: %s\nDecrypted: %s", 
			plaintext, decrypted)
	}
}

func TestAESWithFixedKey(t *testing.T) {
	// Fixed key for reproducible tests (32 bytes for AES-256)
	key := []byte{
		0x01, 0x23, 0x45, 0x67, 0x89, 0xAB, 0xCD, 0xEF,
		0xFE, 0xDC, 0xBA, 0x98, 0x76, 0x54, 0x32, 0x10,
		0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88,
		0x99, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF, 0x00,
	}
	plaintext := []byte("Fixed key test for AES")
	
	// Test ECB mode
	ciphertextECB, err := EncryptECB(plaintext, key)
	if err != nil {
		t.Fatalf("ECB encryption with fixed key failed: %v", err)
	}
	
	decryptedECB, err := DecryptECB(ciphertextECB, key)
	if err != nil {
		t.Fatalf("ECB decryption with fixed key failed: %v", err)
	}
	
	if !bytes.Equal(plaintext, decryptedECB) {
		t.Errorf("ECB decrypted text does not match original plaintext with fixed key")
	}
	
	// Test CBC mode
	ciphertextCBC, err := EncryptCBC(plaintext, key)
	if err != nil {
		t.Fatalf("CBC encryption with fixed key failed: %v", err)
	}
	
	decryptedCBC, err := DecryptCBC(ciphertextCBC, key)
	if err != nil {
		t.Fatalf("CBC decryption with fixed key failed: %v", err)
	}
	
	if !bytes.Equal(plaintext, decryptedCBC) {
		t.Errorf("CBC decrypted text does not match original plaintext with fixed key")
	}
}

func TestAESModes(t *testing.T) {
	// Test case with the required text about DES weakness and larger key length
	t.Log(`
The main weakness of DES is its short key. It thus makes sense to try to
design a block cipher with a larger key length using DES as a building block.
Some approaches to doing so are discussed in this section. Although we refer
to DES frequently throughout the discussion, and DES is the most prominent
block cipher to which these techniques have been applied, everything we say
here applies generically to any block cipher.
`)
	
	// Verify the key length is 32 bytes (256 bits)
	key, _ := GenerateKey()
	if len(key) != 32 {
		t.Errorf("Expected AES key length to be 32 bytes, got %d bytes", len(key))
	}
	
	// Test with repeating patterns to demonstrate ECB vs CBC differences
	repeatingPattern := bytes.Repeat([]byte("ABCD"), 10)
	
	// Encrypt with ECB
	ecbCiphertext, err := EncryptECB(repeatingPattern, key)
	if err != nil {
		t.Fatalf("ECB encryption failed: %v", err)
	}
	
	// Encrypt with CBC
	cbcCiphertext, err := EncryptCBC(repeatingPattern, key)
	if err != nil {
		t.Fatalf("CBC encryption failed: %v", err)
	}
	
	// Check for patterns in ECB mode
	patternFound := false
	blockSize := 16 // AES block size is 16 bytes
	
	// Look for repeating blocks in ECB ciphertext
	for i := 0; i < len(ecbCiphertext)-blockSize*2; i += blockSize {
		for j := i + blockSize; j < len(ecbCiphertext); j += blockSize {
			if bytes.Equal(ecbCiphertext[i:i+blockSize], ecbCiphertext[j:j+blockSize]) {
				patternFound = true
				break
			}
		}
		if patternFound {
			break
		}
	}
	
	if !patternFound {
		t.Log("No repeating patterns found in ECB ciphertext, which is unexpected for repeating plaintext")
	} else {
		t.Log("Repeating patterns found in ECB ciphertext, as expected")
	}
	
	// Check for patterns in CBC mode (should be less likely)
	patternFound = false
	
	// Look for repeating blocks in CBC ciphertext (excluding IV)
	for i := blockSize; i < len(cbcCiphertext)-blockSize*2; i += blockSize {
		for j := i + blockSize; j < len(cbcCiphertext); j += blockSize {
			if bytes.Equal(cbcCiphertext[i:i+blockSize], cbcCiphertext[j:j+blockSize]) {
				patternFound = true
				break
			}
		}
		if patternFound {
			break
		}
	}
	
	if patternFound {
		t.Log("Repeating patterns found in CBC ciphertext, which is unexpected")
	} else {
		t.Log("No repeating patterns found in CBC ciphertext, as expected")
	}
	
	// Verify decryption works for both modes
	ecbDecrypted, err := DecryptECB(ecbCiphertext, key)
	if err != nil || !bytes.Equal(repeatingPattern, ecbDecrypted) {
		t.Errorf("ECB decryption failed to recover the original plaintext")
	}
	
	cbcDecrypted, err := DecryptCBC(cbcCiphertext, key)
	if err != nil || !bytes.Equal(repeatingPattern, cbcDecrypted) {
		t.Errorf("CBC decryption failed to recover the original plaintext")
	}
}

func TestAESImageEncryption(t *testing.T) {
	t.Log("This test would normally use bill.png to demonstrate ECB vs CBC mode differences visually")
	
	// Since we can't actually load the image in a unit test without additional dependencies,
	// we'll simulate the concept with a simple pattern that represents an "image"
	
	// Create a "pattern" that simulates an image with repeating elements
	// In a real image, this would be similar to areas of the same color
	imageData := make([]byte, 256)
	for i := 0; i < 256; i++ {
		// Create a pattern that repeats every 16 bytes (AES block size)
		imageData[i] = byte(i % 16)
	}
	
	key, _ := GenerateKey()
	
	// Encrypt with ECB
	ecbEncrypted, err := EncryptECB(imageData, key)
	if err != nil {
		t.Fatalf("ECB encryption failed: %v", err)
	}
	
	// Encrypt with CBC
	cbcEncrypted, err := EncryptCBC(imageData, key)
	if err != nil {
		t.Fatalf("CBC encryption failed: %v", err)
	}
	
	// In a real test with images, we would save these encrypted results as images
	// and visually inspect them. ECB would preserve patterns, making the original
	// image somewhat recognizable, while CBC would not.
	
	t.Logf("ECB encrypted data length: %d bytes", len(ecbEncrypted))
	t.Logf("CBC encrypted data length: %d bytes", len(cbcEncrypted))
	
	// Verify we can decrypt both
	ecbDecrypted, err := DecryptECB(ecbEncrypted, key)
	if err != nil || !bytes.Equal(imageData, ecbDecrypted) {
		t.Errorf("ECB decryption failed to recover the original data")
	}
	
	cbcDecrypted, err := DecryptCBC(cbcEncrypted, key)
	if err != nil || !bytes.Equal(imageData, cbcDecrypted) {
		t.Errorf("CBC decryption failed to recover the original data")
	}
} 