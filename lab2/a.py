B64_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
PADDING = '='

def text_to_binary(text):
    # ord() gets the ASCII value of the character...
    binary_output = ' '.join(format(ord(char), '08b') for char in text)
    return binary_output

def binary_to_text(binary): 
    text = ""       
    for i in range(0, len(binary),8):    
        text += chr(int(binary[i:i+8], 2))
    return text

def text_to_base64(text):
    binary = text_to_binary(text).replace(' ', '') #  Make sure to remove spaces.
    base64 = ""
    
    while len(binary) % 6 != 0:
        binary += '0'
        
    for i in range(0, len(binary), 6):
        chunk = binary[i:i+6]
        index = int(chunk, 2)
        base64 += B64_CHARS[index]
    
    padding_length = (3 - (len(text) % 3)) % 3
    base64 += PADDING * padding_length
    
    return base64

def base64_to_text(base64):
    binary_str = []
        
    for char in base64:
        # Skip padding characters in conversion.
        if char == PADDING:
            continue
        index = B64_CHARS.index(char)
        binary_str.append(format(index, '06b'))
    
    full_binary = ''.join(binary_str)
    bytes_data = bytearray()
    
    for i in range(0, len(full_binary), 8):
        byte_bits = full_binary[i:i+8].ljust(8, '0')
        bytes_data.append(int(byte_bits[:8], 2))
    
    return bytes(bytes_data).decode('utf-8')

def xor(text, key):
    text_binary = text_to_binary(text).replace(' ', '')
    key_binary = text_to_binary(key).replace(' ', '')
    
    max_len = max(len(text_binary), len(key_binary))
    text_binary = text_binary.ljust(max_len, '0')
    key_binary = key_binary.ljust(max_len, '0')
    
    result_binary = ''
    for i in range(max_len):
        result_binary += str(int(text_binary[i]) ^ int(key_binary[i]))
    
    result = binary_to_text(result_binary)
    return result

def run_all_examples():
    print("\n--- Running all examples ---\n")
    
    print("Examples for Text to Binary:")
    input_text = "Hello"
    print(f"Input: {input_text}")
    print("Output:", text_to_binary(input_text))
    input_text = "Python"
    print(f"\nInput: {input_text}")
    print("Output:", text_to_binary(input_text))
    
    print("\nExamples for Binary to Text:")
    binary_hello = text_to_binary("Hello").replace(" ", "")
    print(f"Input: {binary_hello}")
    print("Output:", binary_to_text(binary_hello))
    binary_python = text_to_binary("Python").replace(" ", "")
    print(f"\nInput: {binary_python}")
    print("Output:", binary_to_text(binary_python))
    
    print("\nExamples for Text to Base64:")
    input_text = "Man"
    print(f"Input: {input_text}")
    print("Output:", text_to_base64(input_text))
    input_text = "Hello"
    print(f"\nInput: {input_text}")
    print("Output:", text_to_base64(input_text))
    
    print("\nExamples for Base64 to Text:")
    input_b64 = "TWFu"
    print(f"Input: {input_b64}")
    print("Output:", base64_to_text(input_b64))
    input_b64 = "SGVsbG8="
    print(f"\nInput: {input_b64}")
    print("Output:", base64_to_text(input_b64))
    
    print("\n--- End of examples ---\n")

def main():
    while True:
        print("\n1. Text to Binary")
        print("2. Binary to Text")
        print("3. Text to Base64")
        print("4. Base64 to Text")
        print("5. XOR")
        print("6. Run All Examples")
        print("7. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                text = input("Enter text: ")
                print(text_to_binary(text))
            case "2":
                binary = input("Enter binary (no spaces): ")
                print(binary_to_text(binary))
            case "3":
                text = input("Enter text: ")
                print(text_to_base64(text))
            case "4":
                base64_str = input("Enter base64: ")
                print(base64_to_text(base64_str))
            case "5":
                text = input("Enter text: ")
                key = input("Enter key: ")
                print(xor(text, key))
            case "6":
                run_all_examples()
            case "7":
                break
            case _:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()