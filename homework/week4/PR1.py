assessment_percentage = 0.6
tax_percentage = 0.0072


def property_tax(value):
    assessment = value * assessment_percentage
    tax = assessment * tax_percentage
    return round(assessment), round(tax)


if __name__ == '__main__':
    value = int(input("Enter a value: "))
    assessment, tax = property_tax(value)
    print("assessment:", assessment)
    print("tax:", tax)
