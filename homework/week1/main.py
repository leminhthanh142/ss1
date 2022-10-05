def sales_prediction():
    total_sales = float(input("Enter projected amount of total sales: "))
    print('Total profit: $' + format(total_sales, ',.2f'))


def land_calculation():
    total_square_feet = float(input("Enter the total square feet: "))
    print("Acre: ", total_square_feet / 43560)


def distance_traveled(time):
    velocity = 70
    print(f"The distance the car will travel in {time} hours:", velocity * time, "miles")


def sales_tax():
    purchase_amount = float(input("Enter the amount of a purchase:"))
    state_sales_tax_percentage = 0.04
    county_sales_tax_percentage = 0.02
    state_sales_tax = purchase_amount * state_sales_tax_percentage
    county_sales_tax = purchase_amount * county_sales_tax_percentage
    total_sales_tax = state_sales_tax + county_sales_tax
    total_sale = purchase_amount + total_sales_tax

    print("The amount of the purchase:", purchase_amount)
    print("The state sales tax:", state_sales_tax)
    print("The county sales tax:", county_sales_tax)
    print("The total sales tax:", total_sales_tax)
    print("The total of the sale:", total_sale)


if __name__ == '__main__':
    sales_prediction()
    print("\n")

    land_calculation()
    print("\n")

    distance_traveled(6)
    distance_traveled(10)
    distance_traveled(15)
    print("\n")

    sales_tax()
    print("\n")
