"""
Project: 백준_10844_쉬운 계단 수
Date: 2022.02.07.월
Author: Kim-Harim
Comment:
- Silver 1
- 동적 계획법
"""

def solve(steps):
    for i in range(1, n):
        for j in range(1, 10):
            if (i == 2 or i == 1) and j == 1:
                steps[i][j] = 1 + steps[i - 1][j + 1]
            elif j == 1:
                steps[i][j] = steps[i - 2][j] + steps[i - 1][j + 1]
            elif j == 9:
                steps[i][j] = steps[i - 1][j - 1]
            else:
                steps[i][j] = steps[i - 1][j - 1] + steps[i - 1][j + 1]
    print(sum(steps[n - 1]) % 1000000000)

if __name__ == "__main__":
    n = int(input())
    steps = [[0] * 10 for _ in range(n)]
    steps[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    solve(steps)
