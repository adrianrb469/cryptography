package tripledes

import (
	"block-cipher/utils"
	"crypto/cipher"
	"crypto/des"
	"crypto/rand"
	"errors"
	"io"
)

// GenerateKey generates a random 24-byte 3DES key
func GenerateKey() ([]byte, error) {
	// 3DES requires a 24-byte key (168 bits, but effective security is 112 bits)
	key := make([]byte, 24)
	_, err := rand.Read(key)
	if err != nil {
		return nil, err
	}
	return key, nil
}

// EncryptCBC encrypts plaintext using 3DES in CBC mode
func EncryptCBC(plaintext, key []byte) ([]byte, error) {
	block, err := des.NewTripleDESCipher(key)
	if err != nil {
		return nil, err
	}
	
	// Create initialization vector
	iv := make([]byte, des.BlockSize)
	if _, err := io.ReadFull(rand.Reader, iv); err != nil {
		return nil, err
	}
	
	// Pad the plaintext
	padded := utils.PadMessage(plaintext, des.BlockSize)
	
	// CBC mode
	ciphertext := make([]byte, len(padded)+len(iv))
	copy(ciphertext, iv) // Prepend IV to ciphertext
	
	mode := cipher.NewCBCEncrypter(block, iv)
	mode.CryptBlocks(ciphertext[len(iv):], padded)
	
	return ciphertext, nil
}

// DecryptCBC decrypts ciphertext using 3DES in CBC mode
func DecryptCBC(ciphertext, key []byte) ([]byte, error) {
	block, err := des.NewTripleDESCipher(key)
	if err != nil {
		return nil, err
	}
	
	if len(ciphertext) < des.BlockSize {
		return nil, errors.New("ciphertext too short")
	}
	
	// Extract IV from the beginning of ciphertext
	iv := ciphertext[:des.BlockSize]
	ciphertext = ciphertext[des.BlockSize:]
	
	if len(ciphertext)%des.BlockSize != 0 {
		return nil, errors.New("ciphertext is not a multiple of the block size")
	}
	
	// CBC mode decryption
	plaintext := make([]byte, len(ciphertext))
	mode := cipher.NewCBCDecrypter(block, iv)
	mode.CryptBlocks(plaintext, ciphertext)
	
	return utils.UnpadMessage(plaintext)
} 