class Car:
    def __init__(self, year, make, speed):
        self.__year_model = year
        self.__make = make
        self.__speed = speed

    def set_year_model(self, year):
        self.__year_model = year

    def set_make(self, make):
        self.__make = make

    def set_speed(self, speed=0):
        self.__speed = speed

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speeds(self):
        return self.__speed

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed


def main():
    year = input("Enter the car’s year model: ")
    make = input("Enter the make of the car: ")
    speed = 0
    my_car = Car(year, make, speed)

    for i in range(0, 5):
        my_car.accelerate()
        print("Current speed is:", my_car.get_speed())

    for x in range(0, 5):
        my_car.brake()
        print("Current speed is:", my_car.get_speed())


if __name__ == '__main__':
    main()