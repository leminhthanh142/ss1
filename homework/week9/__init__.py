def gcd(a, b):
    print(a, b)

    if a == 0:
        return b

    return gcd(b % a, a)


def order_linear_search(arr, curr_index, len, key):
    if len <= 0:
        return -1

    if curr_index > len:
        return -1

    if arr[curr_index] == key:
        return curr_index + 1

    return order_linear_search(arr, curr_index + 1, len, key)


if __name__ == "__main__":
    arr = [12, 34, 54, 2, 4, 7, 3, 3, 123333]
    length = len(arr) - 1
    key = 3
    print(order_linear_search(arr, 0, length, key))
