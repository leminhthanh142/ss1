def day_of_the_week_check(num):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(days[num - 1])


if __name__ == '__main__':
    num = int(input("Enter a number in range of 1 through 7: "))
    day_of_the_week_check(num)
