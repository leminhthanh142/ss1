ticket_A = 20
ticket_B = 15
ticket_C = 10


def stadium_seating(a, b, c):
    return a * ticket_A, b * ticket_B, c * ticket_C


if __name__ == '__main__':
    ticket_class_A = int(input("Enter tickets class A: "))
    ticket_class_B = int(input("Enter tickets class B: "))
    ticket_class_C = int(input("Enter tickets class C: "))

    res_A, res_B, res_C = stadium_seating(ticket_class_A, ticket_class_B, ticket_class_C)
    print("Sale for A:", res_A)
    print("Sale for B:", res_B)
    print("Sale for C:", res_C)
