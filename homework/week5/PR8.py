codes = {
    'A': '!', 'a': '†',
    'B': '@', 'b': '¨',
    'C': '#', 'c': '≠',
    'D': '$', 'd': '≥',
    'E': '%', 'e': '≤',
    'F': '^', 'f': 'ƒ',
    'G': '&', 'g': '£',
    'H': '*', 'h': '™',
    'I': '(', 'i': '¡',
    'J': ')', 'j': 'ª',
    'K': '-', 'k': '+',
    'L': '=', 'l': '[',
    'M': ']', 'm': '{',
    'N': '}', 'n': 'µ',
    'O': '|', 'o': ';',
    'P': 'å', 'p': 'ß',
    'Q': '<', 'q': '>',
    'R': '/', 'r': '?',
    'S': '≈', 's': 'Ω',
    'T': '√', 't': '`',
    'U': '~', 'u': 'œ',
    'V': '∑', 'v': '®',
    'W': '¥', 'w': 'ˆ',
    'X': '˚', 'x': '¬',
    'Y': '•', 'y': '…',
    'Z': 'æ', 'z': '∫',
}

code_keys = list(codes.keys())
code_values = list(codes.values())


def file_encryption(file):
    f = open(file, "r")
    lines = f.readlines()
    encode_character = []
    for line in lines:
        for ch in line:
            if ch in codes:
                encode_character.append(codes[ch])
            else:
                encode_character.append(ch)

    output = open("encoded", "w")
    output.write("".join(encode_character))

    print("encode file successfully")
    output.close()
    f.close()


def file_decryption(file):
    f = open(file, "r")
    lines = f.readlines()
    decode_character = []

    for line in lines:
        for ch in line:
            if ch in codes.values():
                decode_character.append(code_keys[code_values.index(ch)])
            else:
                decode_character.append(ch)

    output = open("decoded", "w")
    output.write("".join(decode_character))

    print("decode file successfully")
    f.close()
    output.close()


if __name__ == '__main__':
    file_encryption("text")
    file_decryption("encoded")
