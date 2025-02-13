from PIL import Image

def load_images(original_path, key_path):
    """Load and prepare both images for XOR operation."""
    # Important, convert to RGB mode to account for different formats...
    original = Image.open(original_path).convert('RGB')
    key = Image.open(key_path).convert('RGB')
    
    key = key.resize(original.size, Image.Resampling.LANCZOS)
    
    return original, key


def xor_images(image1, image2):
    """Perform XOR operation between two images."""
    if image1.size != image2.size:
        raise ValueError("Images must be the same size")
    
    image1_bytes = image1.tobytes()
    image2_bytes = image2.tobytes()
    xor_bytes = bytes(a ^ b for a, b in zip(image1_bytes, image2_bytes))
    
    return Image.frombytes(mode="RGB", size=image1.size, data=xor_bytes)


def main():
    try:
        original, key = load_images("gengar.jpg", "key.jpg")
        
        result = xor_images(original, key)

        print('Result image has been saved to xor_image.png.')
        result.save("xor_image.png")
        
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
