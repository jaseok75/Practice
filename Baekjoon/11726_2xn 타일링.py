"""
Project: 백준_11726_2xn 타일링
Date: 2022.03.27.일
Comment:
- silver 3
"""


def solution(n):
    if n == 1:
        return 1
    arr[1] = 1
    arr[2] = 2
    for i in range(3, n + 1):
        arr[i] = arr[i - 2] + arr[i - 1]
    return arr[n]


if __name__ == "__main__":
    n = int(input())
    arr = [0] * (n + 1)
    print(solution(n) % 10007)
