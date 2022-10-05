def areas_of_rectangle(length, width):
    return length * width


if __name__ == '__main__':
    length1 = float(input("Enter the length of the first rectangle: "))
    width1 = float(input("Enter the width of the first rectangle: "))

    length2 = float(input("Enter the length of the second rectangle: "))
    width2 = float(input("Enter the width of the second rectangle: "))

    areas_of_rectangle1 = areas_of_rectangle(length1, width1)
    areas_of_rectangle2 = areas_of_rectangle(length2, width2)

    if areas_of_rectangle1 > areas_of_rectangle2:
        print("Areas of the first rectangle is grater than the second one ")
    elif areas_of_rectangle1 == areas_of_rectangle2:
        print("2 areas are the same")
    else:
        print("Areas of the second rectangle is grater than the first one ")

