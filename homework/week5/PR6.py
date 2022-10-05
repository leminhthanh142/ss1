def read_file_to_list(file):
    f = open(file, "r")
    file_input = f.read()
    input_arr = file_input.replace("\n", " ").split(" ")
    return input_arr


def search_name(girl_name, boy_name):
    girl_names = read_file_to_list("GirlNames.txt")
    boy_names = read_file_to_list("BoyNames.txt")

    girl_name_find = girl_names.count(girl_name) > 0
    if girl_name_find:
        print("Girl name was among the most popular")
    else:
        print("Girl name was not among the most popular")

    boy_name_find = boy_names.count(boy_name) > 0
    if boy_name_find:
        print("Boy name was among the most popular")
    else:
        print("Boy name was not among the most popular")


if __name__ == '__main__':
    names = input("Enter a boy name, a girl name or both (separate by ','): ").replace(" ", "").split(",")
    print(names)
    search_name(names[0], names[1])
