"""
Project: 백준_15649_N과 M(1)
Date: 2022.02.05.토.
Author: Kim-Harim
Comment:
- Silver 3
"""

"""
첫 번째 방법
"""
import itertools

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [x for x in range(1, n + 1)]
    nCr = list(itertools.permutations(arr, m))
    for i in range(len(nCr)):
        for j in range(len(nCr[i])):
            print(nCr[i][j], end=' ')
        print()

"""
두 번째 방법
"""
"""
Project: 백준_15649_N과 M(1)
Date: 2022.03.11.금.
Comment:
- 백트래킹
- 쉬울줄 알았는데 너무 어려운걸
-  join은 좋은 친구
"""


def solution():
    if len(num) == m:
        print(' '.join(map(str, num)))

    for i in range(1, n + 1):
        if i not in num:
            num.append(i)
            solution()
            num.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())
    num = []
    solution()
