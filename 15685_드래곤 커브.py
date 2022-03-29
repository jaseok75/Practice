"""
Project: 백준_15685_드래곤 커브
Date: 2022.03.29.화
Comment:
- 삼성 기출 문제
"""

from collections import deque


def turn90(x, y, g):
    for _ in range(g):
        turn_size = len(direct)
        for i in range(turn_size):
            turn = (direct[turn_size - 1 - i] + 1) % 4
            nx = x + dx[turn]
            ny = y + dy[turn]
            if 0 <= nx < 101 and 0 <= ny < 101:
                board[nx][ny] = 1
                if rect.count((nx, ny)) == 0:
                    rect.append((nx, ny))
            x, y = nx, ny
            direct.append(turn)
    pass


def rect_check():
    rect_x = [0, 1, 1]
    rect_y = [1, 1, 0]
    rect_count = 0
    while rect:
        x, y = rect.popleft()
        is_rect = 0
        for i in range(3):
            nx = x + rect_x[i]
            ny = y + rect_y[i]
            if 0 <= nx < 101 and 0 <= ny < 101 and board[nx][ny] == 1:
                is_rect += 1
            else:
                break
        if is_rect == 3:
            rect_count += 1
    return rect_count
    pass


if __name__ == "__main__":
    n = int(input())
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    time = 0
    board = [[0] * 101 for i in range(101)]
    rect = deque()

    for _ in range(n):
        y, x, d, g = map(int, input().split())
        direct = deque()
        board[x][y] = 1
        if rect.count((x, y)) == 0:
            rect.append((x, y))
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 101 and 0 <= ny < 101:
            board[nx][ny] = 1
            if rect.count((nx, ny)) == 0:
                rect.append((nx, ny))
        x, y = nx, ny
        direct.append(d)
        turn90(x, y, g)
    print((rect_check()))
