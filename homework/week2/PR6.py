def roman_numerals(num):
    roman_numbers = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    return roman_numbers[num - 1]


if __name__ == '__main__':
    num = int(input("Enter a number in range of 1 through 10: "))
    res = roman_numerals(num)
    print(res)
