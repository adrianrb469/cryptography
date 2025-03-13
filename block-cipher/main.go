package main

import (
	"block-cipher/crypto/aes"
	"block-cipher/crypto/des"
	"block-cipher/crypto/tripledes"
	"bytes"
	"fmt"
	"os"
	"path/filepath"
)

func main() {
	message := []byte("This is a secret message.")
	
	fmt.Println("=== DES with ECB mode ===")
	desKey, err := des.GenerateKey()
	if err != nil {
		fmt.Println("Error generating DES key:", err)
		return
	}
	
	desCiphertext, err := des.EncryptECB(message, desKey)
	if err != nil {
		fmt.Println("Error encrypting with DES:", err)
		return
	}
	
	desPlaintext, err := des.DecryptECB(desCiphertext, desKey)
	if err != nil {
		fmt.Println("Error decrypting with DES:", err)
		return
	}
	
	fmt.Printf("Original Message: %s\n", message)
	fmt.Printf("DES Key (hex): %x\n", desKey)
	fmt.Printf("DES Ciphertext (hex): %x\n", desCiphertext)
	fmt.Printf("DES Decrypted: %s\n\n", desPlaintext)
	
	fmt.Println("=== 3DES with CBC mode ===")
	tripleDESKey, err := tripledes.GenerateKey()
	if err != nil {
		fmt.Println("Error generating 3DES key:", err)
		return
	}
	
	tripleDESCiphertext, err := tripledes.EncryptCBC(message, tripleDESKey)
	if err != nil {
		fmt.Println("Error encrypting with 3DES:", err)
		return
	}
	
	tripleDESPlaintext, err := tripledes.DecryptCBC(tripleDESCiphertext, tripleDESKey)
	if err != nil {
		fmt.Println("Error decrypting with 3DES:", err)
		return
	}
	
	fmt.Printf("Original Message: %s\n", message)
	fmt.Printf("3DES Key (hex): %x\n", tripleDESKey)
	fmt.Printf("3DES Ciphertext (hex): %x\n", tripleDESCiphertext)
	fmt.Printf("3DES Decrypted: %s\n\n", tripleDESPlaintext)
	
	fmt.Println("=== AES with ECB mode ===")
	aesKey, err := aes.GenerateKey()
	if err != nil {
		fmt.Println("Error generating AES key:", err)
		return
	}
	
	aesECBCiphertext, err := aes.EncryptECB(message, aesKey)
	if err != nil {
		fmt.Println("Error encrypting with AES-ECB:", err)
		return
	}
	
	aesECBPlaintext, err := aes.DecryptECB(aesECBCiphertext, aesKey)
	if err != nil {
		fmt.Println("Error decrypting with AES-ECB:", err)
		return
	}
	
	fmt.Printf("Original Message: %s\n", message)
	fmt.Printf("AES Key (hex): %x\n", aesKey)
	fmt.Printf("AES-ECB Ciphertext (hex): %x\n", aesECBCiphertext)
	fmt.Printf("AES-ECB Decrypted: %s\n\n", aesECBPlaintext)
	
	fmt.Println("=== AES with CBC mode ===")
	aesCBCCiphertext, err := aes.EncryptCBC(message, aesKey)
	if err != nil {
		fmt.Println("Error encrypting with AES-CBC:", err)
		return
	}
	
	aesCBCPlaintext, err := aes.DecryptCBC(aesCBCCiphertext, aesKey)
	if err != nil {
		fmt.Println("Error decrypting with AES-CBC:", err)
		return
	}
	
	fmt.Printf("Original Message: %s\n", message)
	fmt.Printf("AES Key (hex): %x\n", aesKey)
	fmt.Printf("AES-CBC Ciphertext (hex): %x\n", aesCBCCiphertext)
	fmt.Printf("AES-CBC Decrypted: %s\n", aesCBCPlaintext)
	
	fmt.Println("\n=== Demonstrating ECB vs CBC with repeating patterns ===")
	
	repeatingMessage := bytes.Repeat([]byte("ABCD"), 10)
	
	ecbRepeating, _ := aes.EncryptECB(repeatingMessage, aesKey)
	cbcRepeating, _ := aes.EncryptCBC(repeatingMessage, aesKey)
	
	fmt.Printf("Repeating Message: %s\n", repeatingMessage)
	fmt.Printf("AES-ECB Ciphertext (hex): %x\n", ecbRepeating)
	fmt.Printf("AES-CBC Ciphertext (hex): %x\n", cbcRepeating)
	fmt.Println("Notice how ECB mode preserves patterns in the original data, while CBC does not.")
	
	fmt.Println("\n=== Demonstrating ECB vs CBC with an image ===")
	
	imagePath := "bill.png"
	
	if _, err := os.Stat(imagePath); os.IsNotExist(err) {
		fmt.Printf("Image file %s does not exist\n", imagePath)
		return
	}
	
	imageData, err := os.ReadFile(imagePath)
	if err != nil {
		fmt.Printf("Failed to read image file: %v\n", err)
		return
	}
	
	ecbEncrypted, err := aes.EncryptECB(imageData, aesKey)
	if err != nil {
		fmt.Printf("Failed to encrypt image with ECB: %v\n", err)
		return
	}
	
	cbcEncrypted, err := aes.EncryptCBC(imageData, aesKey)
	if err != nil {
		fmt.Printf("Failed to encrypt image with CBC: %v\n", err)
		return
	}
	
	outputDir := "output"
	if err := os.MkdirAll(outputDir, 0755); err != nil {
		fmt.Printf("Failed to create output directory: %v\n", err)
		return
	}
	
	ecbOutputPath := filepath.Join(outputDir, "bill_ecb.png")
	if err := os.WriteFile(ecbOutputPath, ecbEncrypted, 0644); err != nil {
		fmt.Printf("Failed to write ECB encrypted image: %v\n", err)
		return
	}
	
	cbcOutputPath := filepath.Join(outputDir, "bill_cbc.png")
	if err := os.WriteFile(cbcOutputPath, cbcEncrypted, 0644); err != nil {
		fmt.Printf("Failed to write CBC encrypted image: %v\n", err)
		return
	}
	
	fmt.Println("Image encryption completed.")
	fmt.Println("Original image:", imagePath)
	fmt.Println("ECB encrypted image:", ecbOutputPath)
	fmt.Println("CBC encrypted image:", cbcOutputPath)
	fmt.Println()
}