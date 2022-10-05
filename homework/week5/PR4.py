def larger_than_n(list, number):
    result = [x for x in list if int(x) > number]
    return result


def read_file_to_list(file):
    f = open(file, "r")
    file_input = f.read()
    input_arr = file_input.replace("\n", " ").split(" ")
    return input_arr


if __name__ == '__main__':
    list = read_file_to_list("input.txt")
    numbers = larger_than_n(list, 60)
    for i in numbers:
        print(i)
