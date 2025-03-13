package utils

import (
	"errors"
)

// PadMessage applies PKCS#7 padding to the plaintext
func PadMessage(plaintext []byte, blockSize int) []byte {
	paddingLen := blockSize - (len(plaintext) % blockSize)
	if paddingLen == 0 {
		paddingLen = blockSize
	}
	padding := make([]byte, paddingLen)
	for i := range padding {
		padding[i] = byte(paddingLen)
	}
	return append(plaintext, padding...)
}

// UnpadMessage removes PKCS#7 padding from the padded data
func UnpadMessage(padded []byte) ([]byte, error) {
	if len(padded) == 0 {
		return nil, errors.New("empty padded data")
	}
	
	paddingLen := int(padded[len(padded)-1])
	if paddingLen > len(padded) {
		return nil, errors.New("invalid padding length")
	}
	
	// Validate padding
	for i := len(padded) - paddingLen; i < len(padded); i++ {
		if padded[i] != byte(paddingLen) {
			return nil, errors.New("invalid padding")
		}
	}
	
	return padded[:len(padded)-paddingLen], nil
} 