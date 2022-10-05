def initials(full_name):
    full_name_arr = full_name.split(" ")
    result = []
    for name in full_name_arr:
        result.append(name[0])
    return ". ".join(result)


if __name__ == '__main__':
    full_name = input("Enter your full name: ")
    res = initials(full_name)
    print(res)
