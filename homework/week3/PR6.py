def most_frequent_character(str):
    frequency = {}
    for ch in str.replace(" ", ""):
        if ch in frequency:
            frequency[ch] = frequency[ch] + 1
        else:
            frequency[ch] = 1

    print(frequency)
    return [k for k, v in frequency.items() if v == max(frequency.values())][0]


if __name__ == '__main__':
    input_string = input("Enter here: ")
    res = most_frequent_character(input_string)
    print(f"most frequent character is: {res}")
