from logo import logo

print(logo)
# Create dictionary with relation English letter - Morse code
morse = {
    'a': ".-",
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': "..-.",
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': "-.-",
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': ".--.",
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': "..-",
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': "--..",
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': "....-",
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': "----.",
    '&': '.-...',
    "'": '.----.',
    '@': '.--.-.',
    ')': '-.--.-',
    '(': '-.--.',
    ':': "---...",
    ',': '--..--',
    '=': '-...-',
    '!': '-.-.--',
    '.': '.-.-.-',
    '-': "-....-",
    '*': '-..-',
    "%": '------..-.-----',
    '+': '.-.-.',
    '"': '.-..-.',
    '?': '..--..',
    '/': "-..-.",
    ' ': '/'
}
in_process = True


# For direction Morse code - English find key by value
def get_letter(val):
    for key, value in morse.items():
        if val == value:
            return key
    return "key doesn't exist"


# Create loop to repeat if needed more
while in_process:
    # Create input to get direction of translation
    direction = input("Do you want to convert to Morse code (type 'M' or 'Morse') or from Morse code "
                      "(type 'EN')? ").lower()
    # Create input to get text to convert
    user_string = input("Please enter text to convert: ").lower()
    converted_word = []
    if direction == "m" or direction == 'morse':
        string = list(user_string)
        # Search in dictionary related symbols
        for i in range(len(string)):
            symbol = morse[string[i]]
            converted_word.append(symbol)
        user_output = ' '.join(converted_word)
        print("Your text in Morse code is: " + user_output)
    elif direction == 'en':
        string = user_string.split(' ')
        for i in range(len(string)):
            symbol = string[i]
            letter = get_letter(symbol)
            converted_word.append(letter)
        user_output = ''.join(converted_word)
        print("Your text is: " + user_output)
    else:
        print("You entered invalid option, please try again")
    continue_converter = input("Do you want to convert something else (Y or N): ").lower()
    if continue_converter == 'y' or continue_converter == 'yes':
        in_process = True
    else:
        in_process = False

