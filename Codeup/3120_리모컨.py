"""
Project: codeup_3120_리모컨
Date: 2022.04.06.수.
Comment:
"""


def solution(a, b):
    result = 0

    while a != b:
        if b - a >= 8:
            result += 1
            a += 10
        elif b - a >= 4:
            result += 1
            a += 5
        else:
            result += 1
            a += 1
        if a > b:
            a, b = b, a

    return result


if __name__ == "__main__":
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    print(solution(a, b))
