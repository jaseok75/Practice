"""
Project: 백준_15649_N과 M(1)
Date: 2022.02.05.토.
Author: Kim-Harim
Comment:
- Silver 3
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
