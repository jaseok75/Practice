"""
Project: 백준_11057_오르막 수
Date: 2022.02.09.수
Author: Kim-Harim
Comment:
- Silver 1
- 동적 계획법
"""

def solve(numbers):
    for i in range(1, n):
        for j in range(9, -1, -1):
            if j == 9:
                numbers[i][j] = 1
            else:
                numbers[i][j] = numbers[i][j + 1] + numbers[i - 1][j]
    print(sum(numbers[n - 1]) % 10007)

if __name__ == "__main__":
    n = int(input())
    numbers = [[0] * 10 for _ in range(n)]
    numbers[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    solve(numbers)
