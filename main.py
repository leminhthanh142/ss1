# This is a sample Python script.
from collections import OrderedDict


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    regex_integer_in_range = r"^[1-9][0-9]{5,5}$"  # Do not delete 'r'.
    regex_alternating_repetitive_digit_pair = r"(\d)[\d]\1+"  # Do not delete 'r'.
    P = input()

    print(re.findall(regex_alternating_repetitive_digit_pair, P))

    print(bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
