def speed_check():
    speed = int(input("Enter your speed: "))
    if speed > 50:
        print("Speed in limit")
    else:
        print("Speed should be checked")


if __name__ == '__main__':
    speed_check()
