def age_classifier(age):
    if age < 0:
        print("Invalid age!")
    elif age == 1:
        print("he or she is an infant")
    elif 1 < age < 13:
        print(" he or she is a child.")
    elif 13 < age < 20:
        print("he or she is a teenager")
    else:
        print("he or she is an adult.")


if __name__ == '__main__':
    age = int(input("Enter your age: "))
    age_classifier(age)
