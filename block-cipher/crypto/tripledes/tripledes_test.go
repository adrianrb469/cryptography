package tripledes

import (
	"bytes"
	"testing"
)

func TestTripleDESEncryptDecrypt(t *testing.T) {
	plaintext := []byte("This is a test message for 3DES encryption.")
	
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

func TestTripleDESWithFixedKey(t *testing.T) {
	// Fixed key for reproducible tests (24 bytes for 3DES)
	key := []byte{
		0x01, 0x23, 0x45, 0x67, 0x89, 0xAB, 0xCD, 0xEF,
		0xFE, 0xDC, 0xBA, 0x98, 0x76, 0x54, 0x32, 0x10,
		0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88,
	}
	plaintext := []byte("Fixed key test for 3DES")
	
	// Encrypt with fixed key
	ciphertext, err := EncryptCBC(plaintext, key)
	if err != nil {
		t.Fatalf("Encryption with fixed key failed: %v", err)
	}
	
	// Decrypt with the same key
	decrypted, err := DecryptCBC(ciphertext, key)
	if err != nil {
		t.Fatalf("Decryption with fixed key failed: %v", err)
	}
	
	// Check if the decrypted text matches the original plaintext
	if !bytes.Equal(plaintext, decrypted) {
		t.Errorf("Decrypted text does not match original plaintext with fixed key")
	}
}

func TestTripleDESKeyLength(t *testing.T) {
	// Test case with the required text about 3DES
	t.Log(`
The main weakness of DES is its short key. It thus makes sense to try to
design a block cipher with a larger key length using DES as a building block.
Some approaches to doing so are discussed in this section. Although we refer
to DES frequently throughout the discussion, and DES is the most prominent
block cipher to which these techniques have been applied, everything we say
here applies generically to any block cipher.
`)
	
	// Verify the key length is 24 bytes (192 bits, though effective security is 112 bits)
	key, _ := GenerateKey()
	if len(key) != 24 {
		t.Errorf("Expected 3DES key length to be 24 bytes, got %d bytes", len(key))
	}
	
	// Simple test to verify the implementation works
	plaintext := []byte("3DES-Test")
	
	ciphertext, err := EncryptCBC(plaintext, key)
	if err != nil {
		t.Fatalf("Encryption failed: %v", err)
	}
	
	// Decrypt and verify
	decrypted, err := DecryptCBC(ciphertext, key)
	if err != nil {
		t.Fatalf("Decryption failed: %v", err)
	}
	
	if !bytes.Equal(plaintext, decrypted) {
		t.Errorf("Decryption failed to recover the original plaintext")
	}
}

func TestTripleDESIVExtraction(t *testing.T) {
	// Test that the IV is correctly extracted during decryption
	plaintext := []byte("Testing IV extraction")
	key, _ := GenerateKey()
	
	// Encrypt the plaintext
	ciphertext, err := EncryptCBC(plaintext, key)
	if err != nil {
		t.Fatalf("Encryption failed: %v", err)
	}
	
	// Modify the IV (first 8 bytes) and verify decryption fails or produces different result
	modifiedCiphertext := make([]byte, len(ciphertext))
	copy(modifiedCiphertext, ciphertext)
	modifiedCiphertext[0] ^= 0xFF // Flip bits in the IV
	
	// Decrypt with modified IV
	decryptedModified, err := DecryptCBC(modifiedCiphertext, key)
	if err == nil && bytes.Equal(plaintext, decryptedModified) {
		t.Errorf("Decryption succeeded with modified IV, but should have failed or produced different result")
	}
	
	// Decrypt with original ciphertext
	decrypted, err := DecryptCBC(ciphertext, key)
	if err != nil {
		t.Fatalf("Decryption with original ciphertext failed: %v", err)
	}
	
	if !bytes.Equal(plaintext, decrypted) {
		t.Errorf("Decryption with original ciphertext failed to recover the plaintext")
	}
} 