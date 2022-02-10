"""
Project: 백준_11051_이항 계수 2
Date: 2022.02.10.목
Author: Kim-Harim
Comment:
- Silver 1
"""

def solve(n, k):
    mul = 1
    shr = 1
    for i in range(k):
        mul *= (n - i)
        shr *= (k - i)
    print((mul // shr) % 10007)

if __name__ == "__main__":
    n, k = map(int, input().split())
    solve(n, k)
