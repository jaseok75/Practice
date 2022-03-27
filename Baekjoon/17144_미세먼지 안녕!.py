"""
Project: 백준_17144_미세먼지 안녕!
Date: 2022.03.27.일
Comment:
- 삼성 기출 문제
"""

from collections import deque


def solution1(r, c):
    # 북, 동, 남, 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                spread = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] >= 0:
                        dust_spread[nx][ny] += (board[i][j] // 5)
                        spread += 1
                dust_spread[i][j] += (board[i][j] - ((board[i][j] // 5) * spread))
    pass


def work_1(x, y):
    for i in range(x - 1, 0, -1):
        dust_spread[i][y] = dust_spread[i - 1][y]
    for i in range(y, c - 1):
        dust_spread[0][i] = dust_spread[0][i + 1]
    for i in range(0, x):
        dust_spread[i][c - 1] = dust_spread[i + 1][c - 1]
    for i in range(c - 1, y, -1):
        dust_spread[x][i] = dust_spread[x][i - 1]
    dust_spread[x][y + 1] = 0
    pass


def work_2(x, y):
    for i in range(x + 1, r - 1):
        dust_spread[i][y] = dust_spread[i + 1][y]
    for i in range(y, c - 1):
        dust_spread[r - 1][i] = dust_spread[r - 1][i + 1]
    for i in range(r - 1, x, -1):
        dust_spread[i][c - 1] = dust_spread[i - 1][c - 1]
    for i in range(c - 1, y, -1):
        dust_spread[x][i] = dust_spread[x][i - 1]
    dust_spread[x][y + 1] = 0
    pass


if __name__ == "__main__":
    r, c, t = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(r)]
    cleaner = deque((i, j) for i in range(r) for j in range(c) if board[i][j] == -1)
    cleaner1_x, cleaner1_y = cleaner.popleft()
    cleaner2_x, cleaner2_y = cleaner.popleft()
    dust_spread = []
    for _ in range(t):
        dust_spread = [[0] * c for _ in range(r)]
        dust_spread[cleaner1_x][cleaner1_y] = -1
        dust_spread[cleaner2_x][cleaner2_y] = -1
        solution1(r, c)
        work_1(cleaner1_x, cleaner1_y)
        work_2(cleaner2_x, cleaner2_y)
        for _ in range(r):
            board = [item[:] for item in dust_spread]
    sum_dust = 0
    for idx in dust_spread:
        sum_dust += sum(idx)
    print(sum_dust + 2)
