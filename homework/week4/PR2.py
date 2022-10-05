def calories_from_fat_and_carbohydrates(fat, carbohydrates):
    calories_from_fat = fat * 9
    calories_from_carbohydrates = carbohydrates * 4
    return calories_from_fat, calories_from_carbohydrates


if __name__ == '__main__':
    fat = int(input("Enter fat grams: "))
    carbohydrates = int(input("Enter carbohydrate grams: "))

    cff, cfc = calories_from_fat_and_carbohydrates(fat, carbohydrates)
    print("calories_from_fat:", cff)
    print("calories_from_carbohydrates:", cfc)
