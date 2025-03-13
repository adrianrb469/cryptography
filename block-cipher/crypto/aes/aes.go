package aes

import (
	"block-cipher/utils"
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"errors"
	"io"
)

// Makes a random 32-byte AES key
func GenerateKey() ([]byte, error) {
	key := make([]byte, 32)
	_, err := rand.Read(key)
	if err != nil {
		return nil, err
	}
	return key, nil
}

// EncryptECB encrypts plaintext using AES in ECB mode
func EncryptECB(plaintext, key []byte) ([]byte, error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}
	
	// Pad the plaintext
	padded := utils.PadMessage(plaintext, aes.BlockSize)
	ciphertext := make([]byte, len(padded))
	
	// ECB mode implementation
	for i := 0; i < len(padded); i += aes.BlockSize {
		block.Encrypt(ciphertext[i:i+aes.BlockSize], padded[i:i+aes.BlockSize])
	}
	
	return ciphertext, nil
}

// DecryptECB decrypts ciphertext using AES in ECB mode
func DecryptECB(ciphertext, key []byte) ([]byte, error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}
	
	if len(ciphertext)%aes.BlockSize != 0 {
		return nil, errors.New("ciphertext is not a multiple of the block size")
	}
	
	plaintext := make([]byte, len(ciphertext))
	
	// ECB mode implementation
	for i := 0; i < len(ciphertext); i += aes.BlockSize {
		block.Decrypt(plaintext[i:i+aes.BlockSize], ciphertext[i:i+aes.BlockSize])
	}
	
	return utils.UnpadMessage(plaintext)
}

// EncryptCBC encrypts plaintext using AES in CBC mode
func EncryptCBC(plaintext, key []byte) ([]byte, error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}
	
	// Creates a random initialization vector
	iv := make([]byte, aes.BlockSize)
	if _, err := io.ReadFull(rand.Reader, iv); err != nil {
		return nil, err
	}
	
	// Pad the plaintext
	padded := utils.PadMessage(plaintext, aes.BlockSize)
	
	// CBC mode
	ciphertext := make([]byte, len(padded)+len(iv))
	copy(ciphertext, iv) // Prepend IV to ciphertext
	
	mode := cipher.NewCBCEncrypter(block, iv)
	mode.CryptBlocks(ciphertext[len(iv):], padded)
	
	return ciphertext, nil
}

// DecryptCBC decrypts ciphertext using AES in CBC mode
func DecryptCBC(ciphertext, key []byte) ([]byte, error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}
	
	if len(ciphertext) < aes.BlockSize {
		return nil, errors.New("ciphertext too short")
	}
	
	// Extract IV from the beginning of ciphertext
	iv := ciphertext[:aes.BlockSize]
	ciphertext = ciphertext[aes.BlockSize:]
	
	if len(ciphertext)%aes.BlockSize != 0 {
		return nil, errors.New("ciphertext is not a multiple of the block size")
	}
	
	// CBC mode decryption
	plaintext := make([]byte, len(ciphertext))
	mode := cipher.NewCBCDecrypter(block, iv)
	mode.CryptBlocks(plaintext, ciphertext)
	
	return utils.UnpadMessage(plaintext)
} 