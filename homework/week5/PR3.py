def number_analysis_program(numbers):
    lowest_number = min(numbers)
    highest_number = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    return lowest_number, highest_number, total, average


if __name__ == '__main__':
    numbers = []
    for i in range(1, 21):
        num = int(input(f"Enter number {i}: "))
        numbers.append(num)

    lowest_number, highest_number, total, average = number_analysis_program(numbers)
    print(f"Lowest number: {lowest_number}")
    print(f"Highest number: {highest_number}")
    print(f"Total number: {total}")
    print(f"Average number: {average}")
