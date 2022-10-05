vowels_letters = "aeuio"


def vowels_count(str):
    count = 0
    for ch in str:
        if ch.lower() in vowels_letters:
            count = count + 1
    return count


def consonants_count(str):
    count = 0
    for ch in str:
        if ch.lower() not in vowels_letters and ch.isalpha():
            count = count + 1
    return count


if __name__ == '__main__':
    input_string = input("Enter here: ")
    vowels = vowels_count(input_string)
    consonants = consonants_count(input_string)
    print(f"vowels: {vowels} \nconsonants: {consonants}")
