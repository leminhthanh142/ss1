def pig_latin(input):
    result = []
    str_arr = input.strip().split(" ")

    for word in str_arr:
        if word.isupper():
            result.append(word[1:] + word[0] + "AY")
        else:
            result.append(word[1:] + word[0] + "ay")

    return " ".join(result)


if __name__ == '__main__':
    input_string = input("Enter here: ")
    res = pig_latin(input_string)
    print(f"Result: {res}")
