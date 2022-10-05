from itertools import product
import timeit

vowels = "AEUIO"


def minion_game(s):
    # kevin_words = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if s[i] in vowels]
    # stuart_words = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if s[i] not in vowels]
    #
    stuart_score = 0
    kevin_score = 0

    for i in range(len(s)):
        if s[i] in vowels:
            kevin_score += len(s[i:])
        else:
            stuart_score += len(s[i:])

    if stuart_score == kevin_score:
        print("Draw")
    if stuart_score > kevin_score:
        print("Stuart %s" % stuart_score)
    if kevin_score > stuart_score:
        print("Kevin %s" % kevin_score)


if __name__ == '__main__':
    n, m = map(int, input().split())
    array = input().split()

    A = set(input().split())
    B = set(input().split())

    res = 0
    for i in array:
        if i in A:
            res += 1
        else:
            res -= 1

    # res = sum([(i in A) - (i in B) for i in array])
    print(res)

