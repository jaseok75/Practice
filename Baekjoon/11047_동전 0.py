"""
Project: 백준_11047_동전 0
Date: 2022.02.01.화.
Author: Kim-Harim
Comment:
- Silver 2
- 그리디
"""

def solve(k, coins):
    idx = n - 1
    count = 0
    while k != 0:
        if k >= coins[idx]:
            count += (k // coins[idx])
            k %= coins[idx]
        else:
            idx -= 1
    return count

if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = []
    for _ in range(n):
        coin = int(input())
        coins.append(coin)
    answer = solve(k, coins)
    print(answer)
