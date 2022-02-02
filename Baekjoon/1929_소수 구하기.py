"""
Project: 백준_1929_소수 구하기
Date: 2022.02.02.수
Author: Kim-Harim
Comment:
- Silver 2
- 소수 판별
- 1은 소수가 아니다.
"""

import math

"""
def solve2(n):
    array = [True for i in range(n + 1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return [i for i in range(2, n + 1) if array[i]]
"""

def solve(m, n):
    for i in range(m, n + 1):
        if i == 1:
            continue
        flag = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            print(i)

if __name__ == "__main__":
    m, n = map(int, input().split())
    solve(m, n)
