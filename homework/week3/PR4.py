def sentence_capitalizer(string):
    sentences = string.split(". ")
    result = [word[0].capitalize() + word[1:] for word in sentences]
    return ". ".join(result)


if __name__ == '__main__':
    input_str = input("Enter sentences: ")
    res = sentence_capitalizer(input_str)
    print(res)
