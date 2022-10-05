def paint_job_estimator(square_footage, price_gallon):
    num_gallons = square_footage / 112
    hours_labor = num_gallons * 8
    total_price_gallon = num_gallons * price_gallon
    total_labor = hours_labor * 35
    final_total = total_price_gallon + total_labor
    return num_gallons, hours_labor, total_price_gallon, total_labor, final_total


if __name__ == '__main__':
    square_footage = input('Enter the number of square feet to be painted: ')

    # Ask for the price of the paint per gallon.
    price_gallon = input('Enter the price of the paint per gallon: ')

    num_gallons, hours_labor, total_price_gallon, total_labor, final_total = paint_job_estimator(square_footage, price_gallon)
    print("The number of gallons of paint required:", num_gallons)
    print("The hours of labor required:", hours_labor)
    print("The cost of the paint:", total_price_gallon)
    print("The labor charges:", total_labor)
    print("The total cost of the paint job:", final_total)
