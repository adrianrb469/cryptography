theoretical_freq = {
        'A': 0.1253, 'B': 0.0142, 'C': 0.0468, 'D': 0.0586, 'E': 0.1368,
        'F': 0.0069, 'G': 0.0101, 'H': 0.0070, 'I': 0.0625, 'J': 0.0044,
        'K': 0.0002, 'L': 0.0497, 'M': 0.0315, 'N': 0.0671, 'Ñ': 0.0031,
        'O': 0.0868, 'P': 0.0251, 'Q': 0.0088, 'R': 0.0687, 'S': 0.0798,
        'T': 0.0463, 'U': 0.0393, 'V': 0.0090, 'W': 0.0001, 'X': 0.0022,
        'Y': 0.0090, 'Z': 0.0052
    }

def relative_frequency(text):
    text = text.upper()
    
    # Don't lose any characters that are technically in the alphabet...
    replacements = {
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U', 'Ü': 'U'
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)

    text = ''.join(e for e in text if e in theoretical_freq)
    
    return {char: text.count(char) / len(text) for char in set(text)}


message = input('Message: ')

print(relative_frequency(message))