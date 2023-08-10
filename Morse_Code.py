# Morse Code to Text or vice versa

def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
    return ' '.join(morse_code)

def morse_to_text(morse_code):
    inverse_dict = {value: key for key, value in MORSE_CODE_DICT.items()}
    decoded_text = []
    for code in morse_code.split(' '):
        if code in inverse_dict:
            decoded_text.append(inverse_dict[code])
    return ''.join(decoded_text)

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'
}

def main():
    print("Welcome to the Morse Code Converter!")

    choice = input("Choose '1' to convert text to Morse code or '2' to convert Morse code to text: ")
    if choice == '1':
        text = input("Enter the text to convert to Morse code: ")
        morse_code = text_to_morse(text)
        print("Morse code:", morse_code)
    elif choice == '2':
        morse_code = input("Enter the Morse code to convert to text: ")
        text = morse_to_text(morse_code)
        print("Decoded text:", text)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()