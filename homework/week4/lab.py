# 1-69
# 1-24
# overdue

frequency_dict = {}
overdue_dict = {}


def read_file_to_list(file):
    f = open(file, "r")
    file_input = f.read()
    input_arr = file_input.replace("\n", " ").split(" ")
    new_arr = [int(i) for i in input_arr]
    return new_arr


def dict_sort(dict_input, is_reverse=False):
    return sorted(dict_input.items(), key=lambda item: item[1], reverse=is_reverse)


def frequency_dict_generate():
    input_arr = read_file_to_list("input.txt")

    for i in input_arr:
        if i not in frequency_dict:
            frequency_dict[i] = 1
        else:
            frequency_dict[i] += 1


def overdue_dict_generate():
    input_arr = read_file_to_list("input.txt")
    index = 1
    for i in input_arr:
        if i not in overdue_dict:
            for j in input_arr[index:]:
                if i not in overdue_dict:
                    overdue_dict[i] = 1
                elif i != j:
                    overdue_dict[i] += 1
                elif i == j:
                    break

        index += 1


def get_ten_most_common(input_dict):
    sorted_dict = dict_sort(input_dict, True)
    return sorted_dict[:10]


def get_ten_least_common(input_dict):
    sorted_dict = dict_sort(input_dict, True)
    return sorted_dict[-10:]


if __name__ == '__main__':
    frequency_dict_generate()
    overdue_dict_generate()

    ten_most_common = get_ten_most_common(frequency_dict)
    print("Ten most common number order by frequency: ")
    for i in ten_most_common:
        print(i[0], f"frequency {i[1]}")

    ten_least_common = get_ten_least_common(frequency_dict)
    print("Ten least common number order by frequency: ")
    for i in ten_least_common:
        print(i[0], f"frequency {i[1]}")

    ten_most_overdue = get_ten_most_common(overdue_dict)
    print("Ten most overdue number order by frequency: ")
    for i in ten_most_overdue:
        print(i[0], f"overdue {i[1]}")

    print("frequency of number from 1-69")
    for i in range(1, 70):
        if i in frequency_dict:
            print(f"{i} frequency: {frequency_dict[i]}")

    print("frequency of number from 1-24")
    for i in range(1, 25):
        if i in frequency_dict:
            print(f"{i} frequency: {frequency_dict[i]}")

