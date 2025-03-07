package main

import (
	"crypto/des"
	"crypto/rand"
	"fmt"
)

func padMessage(plaintext []byte) []byte {
	blockSize := des.BlockSize
	paddingLen := blockSize - (len(plaintext) % blockSize)
	if paddingLen == blockSize {
		paddingLen = blockSize
	}
	padding := make([]byte, paddingLen)
	for i := range padding {
		padding[i] = byte(paddingLen)
	}
	return append(plaintext, padding...)
}

func generateKey() ([]byte, error) {
	key := make([]byte, 8) 
	_, err := rand.Read(key)
	if err != nil {
		return nil, err
	}
	return key, nil
}

func encryptDES(plaintext, key []byte) ([]byte, error) {
	block, err := des.NewCipher(key)
	if err != nil {
		return nil, err
	}
	padded := padMessage(plaintext)
	ciphertext := make([]byte, len(padded))
	for i := 0; i < len(padded); i += des.BlockSize {
		block.Encrypt(ciphertext[i:i+des.BlockSize], padded[i:i+des.BlockSize])
	}
	return ciphertext, nil
}

func main() {
	message := []byte("This is a secret message.")
	key, err := generateKey()
	if err != nil {
		fmt.Println("Error generating key", err)
		return
	}

	ciphertext, err := encryptDES(message, key)
	if err != nil {
		fmt.Println("Error encrypting", err)
		return
	}

	fmt.Printf("Original Message: %s\n", message)
	fmt.Printf("Generated Key (hex): %x\n", key)
	fmt.Printf("Ciphertext (hex): %x\n", ciphertext)
}