"""
Project: codeup_3007기억력 테스트 7
Date: 2022.04.08.금.
Comment:
- 동적계획법
"""


def sum_list(arr, n):
    easy_test = [0] * (n + 1)
    easy_test[1] = arr[0]
    for i in range(2, n + 1):
        easy_test[i] = easy_test[i - 1] + arr[i - 1]
    return easy_test


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    sum_num = sum_list(arr, n)
    for _ in range(m):
        a, b = map(int, input().split())
        print(sum_num[b] - sum_num[a - 1])
