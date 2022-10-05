def magic_date(month, day, year):
    message = '\n' + format(month) + '/' \
              + format(day) + '/' \
              + format(year) + \
              ' is '

    if (month * day) != year:
        message += "not "

    message += "magic."
    print(message, "\n\n")


if __name__ == '__main__':
    month = int(input('\nEnter the month from 1 through 12: '))
    day = int(input('Enter the day from 1 through 31: '))
    year = int(input('Enter the year (2 digits): '))
    magic_date(month, day, year)
