package des

import (
	"block-cipher/utils"
	"crypto/des"
	"crypto/rand"
	"errors"
)

// GenerateKey generates a random 8-byte DES key
func GenerateKey() ([]byte, error) {
	key := make([]byte, 8) 
	_, err := rand.Read(key)
	if err != nil {
		return nil, err
	}
	return key, nil
}

// EncryptECB encrypts plaintext using DES in ECB mode
func EncryptECB(plaintext, key []byte) ([]byte, error) {
	block, err := des.NewCipher(key)
	if err != nil {
		return nil, err
	}
	padded := utils.PadMessage(plaintext, des.BlockSize)
	ciphertext := make([]byte, len(padded))
	
	// ECB mode implementation
	for i := 0; i < len(padded); i += des.BlockSize {
		block.Encrypt(ciphertext[i:i+des.BlockSize], padded[i:i+des.BlockSize])
	}
	return ciphertext, nil
}

// DecryptECB decrypts ciphertext using DES in ECB mode
func DecryptECB(ciphertext, key []byte) ([]byte, error) {
	block, err := des.NewCipher(key)
	if err != nil {
		return nil, err
	}
	
	if len(ciphertext)%des.BlockSize != 0 {
		return nil, errors.New("ciphertext is not a multiple of the block size")
	}
	
	plaintext := make([]byte, len(ciphertext))
	
	// ECB mode implementation
	for i := 0; i < len(ciphertext); i += des.BlockSize {
		block.Decrypt(plaintext[i:i+des.BlockSize], ciphertext[i:i+des.BlockSize])
	}
	
	return utils.UnpadMessage(plaintext)
} 