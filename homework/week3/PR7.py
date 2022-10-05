import re


def word_separator(input):
    capitalize_word_regex = "[A-Z][^A-Z]*"
    str_arr = re.findall(capitalize_word_regex, input)

    result = [word[0].lower() + word[1:] for word in str_arr[1:]]

    return str_arr[0] + " " + " ".join(result)


if __name__ == '__main__':
    input_string = input("Enter here: ")
    res = word_separator(input_string)
    print(f"Result: {res}")
