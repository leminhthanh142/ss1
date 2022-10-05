import random


def roll(number_of_throws):
    retval = []
    for i in range(0, number_of_throws):
        retval.append(random.randint(1, 6))

    return sorted(retval)


if __name__ == '__main__':
    number_of_throws = int(input("Enter number of throw: "))
    numbers = roll(number_of_throws)
    for i in numbers:
        print(i)
