package des

import (
	"bytes"
	"testing"
)

func TestDESEncryptDecrypt(t *testing.T) {
	plaintext := []byte("This is a test message for DES encryption.")
	
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

func TestDESWithFixedKey(t *testing.T) {
	// Fixed key for reproducible tests
	key := []byte{0x01, 0x23, 0x45, 0x67, 0x89, 0xAB, 0xCD, 0xEF}
	plaintext := []byte("Fixed key test")
	
	// Encrypt with fixed key
	ciphertext, err := EncryptECB(plaintext, key)
	if err != nil {
		t.Fatalf("Encryption with fixed key failed: %v", err)
	}
	
	// Decrypt with the same key
	decrypted, err := DecryptECB(ciphertext, key)
	if err != nil {
		t.Fatalf("Decryption with fixed key failed: %v", err)
	}
	
	// Check if the decrypted text matches the original plaintext
	if !bytes.Equal(plaintext, decrypted) {
		t.Errorf("Decrypted text does not match original plaintext with fixed key")
	}
}

func TestDESSpecification(t *testing.T) {
	// Test case with the required text about DES specification
	t.Log(`
The DES block cipher is a 16-round Feistel network with a block length of
64 bits and a key length of 56 bits. The same round function ˆ f is used in each
of the 16 rounds. The round function takes a 48-bit sub-key and, as expected
for a (balanced) Feistel network, a 32-bit input (namely, half a block). The
key schedule of DES is used to derive a sequence of 48-bit sub-keys k1, . . . , k16
from the 56-bit master key.
`)
	
	// Simple test to verify the implementation works with this knowledge
	plaintext := []byte("DES-Test")
	key, _ := GenerateKey()
	
	ciphertext, err := EncryptECB(plaintext, key)
	if err != nil {
		t.Fatalf("Encryption failed: %v", err)
	}
	
	// Verify the ciphertext is a multiple of the block size (64 bits = 8 bytes)
	if len(ciphertext)%8 != 0 {
		t.Errorf("Ciphertext length %d is not a multiple of block size 8", len(ciphertext))
	}
	
	// Decrypt and verify
	decrypted, err := DecryptECB(ciphertext, key)
	if err != nil {
		t.Fatalf("Decryption failed: %v", err)
	}
	
	if !bytes.Equal(plaintext, decrypted) {
		t.Errorf("Decryption failed to recover the original plaintext")
	}
} 