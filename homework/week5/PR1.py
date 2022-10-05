from random import randint


def random_number_generator(digits):
    start_range = 10 ** (digits - 1)
    end_range = (10 ** digits) - 1
    return randint(start_range, end_range)


def lottery_number_generator():
    number_list = []
    for i in range(0, 7):
        number_list.append(random_number_generator(7))

    return number_list


if __name__ == '__main__':
    number_list = lottery_number_generator()
    for i in number_list:
        print(i)
