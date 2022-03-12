"""
Project: 백준_15652_N과 M(4)
Date: 2022.03.12.토.
Comment:
- 백트래킹
"""


def solution():
    if len(num) == m:
        print(' '.join(map(str, num)))
        return

    for i in range(1, n + 1):
        if len(num) < 1 or i >= num[len(num) - 1]:
            num.append(i)
            solution()
            num.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())
    num = []
    solution()
