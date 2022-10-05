from datetime import datetime


def date_printer(date_time):
    print(datetime.strptime(date_time, '%m/%d/%Y').strftime('%B %d, %Y'))


if __name__ == '__main__':
    date = input("Enter date in format mm/dd/yyyy: ")
    date_printer(date)
