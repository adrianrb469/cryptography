package crypto

import (
	"block-cipher/crypto/aes"
	"bytes"
	"fmt"
	"os"
	"path/filepath"
	"testing"
)

// TestImageEncryption demonstrates the visual difference between ECB and CBC modes
// using the bill.png image. This test is marked as a manual test because it requires
// visual inspection of the output images.
func TestImageEncryption(t *testing.T) {
	// Skip this test in normal test runs
	if testing.Short() {
		t.Skip("Skipping image encryption test in short mode")
	}

	// Path to the bill.png image
	imagePath := filepath.Join("..", "bill.png")
	
	// Check if the image exists
	if _, err := os.Stat(imagePath); os.IsNotExist(err) {
		t.Fatalf("Image file %s does not exist", imagePath)
	}
	
	// Read the image file
	imageData, err := os.ReadFile(imagePath)
	if err != nil {
		t.Fatalf("Failed to read image file: %v", err)
	}
	
	// Generate an AES key
	key, err := aes.GenerateKey()
	if err != nil {
		t.Fatalf("Failed to generate AES key: %v", err)
	}
	
	// Encrypt the image with ECB mode
	ecbEncrypted, err := aes.EncryptECB(imageData, key)
	if err != nil {
		t.Fatalf("Failed to encrypt image with ECB: %v", err)
	}
	
	// Encrypt the image with CBC mode
	cbcEncrypted, err := aes.EncryptCBC(imageData, key)
	if err != nil {
		t.Fatalf("Failed to encrypt image with CBC: %v", err)
	}
	
	// Save the encrypted images
	outputDir := filepath.Join("..", "output")
	if err := os.MkdirAll(outputDir, 0755); err != nil {
		t.Fatalf("Failed to create output directory: %v", err)
	}
	
	ecbOutputPath := filepath.Join(outputDir, "bill_ecb.png")
	if err := os.WriteFile(ecbOutputPath, ecbEncrypted, 0644); err != nil {
		t.Fatalf("Failed to write ECB encrypted image: %v", err)
	}
	
	cbcOutputPath := filepath.Join(outputDir, "bill_cbc.png")
	if err := os.WriteFile(cbcOutputPath, cbcEncrypted, 0644); err != nil {
		t.Fatalf("Failed to write CBC encrypted image: %v", err)
	}
	
	// Decrypt the images to verify the encryption works
	ecbDecrypted, err := aes.DecryptECB(ecbEncrypted, key)
	if err != nil {
		t.Fatalf("Failed to decrypt ECB image: %v", err)
	}
	
	cbcDecrypted, err := aes.DecryptCBC(cbcEncrypted, key)
	if err != nil {
		t.Fatalf("Failed to decrypt CBC image: %v", err)
	}
	
	// Verify the decrypted images match the original
	if !bytes.Equal(imageData, ecbDecrypted) {
		t.Errorf("ECB decrypted image does not match original")
	}
	
	if !bytes.Equal(imageData, cbcDecrypted) {
		t.Errorf("CBC decrypted image does not match original")
	}
	
	// Save the decrypted images for verification
	ecbDecryptedPath := filepath.Join(outputDir, "bill_ecb_decrypted.png")
	if err := os.WriteFile(ecbDecryptedPath, ecbDecrypted, 0644); err != nil {
		t.Fatalf("Failed to write ECB decrypted image: %v", err)
	}
	
	cbcDecryptedPath := filepath.Join(outputDir, "bill_cbc_decrypted.png")
	if err := os.WriteFile(cbcDecryptedPath, cbcDecrypted, 0644); err != nil {
		t.Fatalf("Failed to write CBC decrypted image: %v", err)
	}
	
	// Print information about the test
	fmt.Println("Image encryption test completed.")
	fmt.Println("Original image:", imagePath)
	fmt.Println("ECB encrypted image:", ecbOutputPath)
	fmt.Println("CBC encrypted image:", cbcOutputPath)
	fmt.Println("ECB decrypted image:", ecbDecryptedPath)
	fmt.Println("CBC decrypted image:", cbcDecryptedPath)
	fmt.Println()
	fmt.Println("Note: The ECB encrypted image may show patterns from the original image,")
	fmt.Println("while the CBC encrypted image should appear completely random.")
	fmt.Println("This demonstrates why ECB mode is not secure for encrypting data with patterns.")
} 