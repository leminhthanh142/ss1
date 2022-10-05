def mass_and_weight(mass):
    weight = mass * 9.8
    message = "The object"

    if weight < 100:
        message += ' is too light at ' + format(weight, ',.2f') + ' newtons.'
    elif 100 <= weight <= 500:
        message += '\'s weight at ' + format(weight, ',.2f') + ' is just right.'
    elif weight > 500:
        message += ' is too heavy at ' + format(weight, ',.2f') + ' newtons.'

    print(message)


if __name__ == '__main__':
    mass = float(input('Enter an object\'s mass: '))
    mass_and_weight(mass)
