phone_letters = {
    'A': '2', 'B': '2', 'C': '2',
    'D': '3', 'E': '3', 'F': '3',
    'G': '4', 'H': '4', 'I': '4',
    'J': '5', 'K': '5', 'L': '5',
    'M': '6', 'N': '6', 'O': '6',
    'P': '7', 'Q': '7', 'R': '7', 'S': '7',
    'T': '8', 'U': '8', 'V': '8',
    'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
}


def alphabetic_telephone_number_translator(phone_number):
    result = []
    for n in phone_number:
        if n.isdigit():
            str(result.append(n))
        elif n.isalpha():
            value = phone_letters.get(n.upper())
            result.append(value)
        else:
            result.append(n)
    return result


if __name__ == '__main__':
    phone_number = input("Enter alphabet number: ")
    res = alphabetic_telephone_number_translator(phone_number)
    print("".join(res))
