"""
Project: 백준_토마토_7576
Date: 2022.01.08.토.
"""

from collections import deque

def isRange(x, y):
    if 0 <= x < M and 0 <= y < N:
        return True
    else:
        return False

def bfs(x, y):
    global ripe
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    ripe.append((x, y))
    index = 0

    while index < len(ripe):
        (x, y) = ripe.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isRange(nx, ny) and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                c_box = box
                ripe.append((nx, ny))
        #index += 1

def tomato(N, M, box):
    global ripe
    ripe = deque()
    for i in range(M):
        for j in range(N):
            if box[i][j] == 1:
                ripe.append((i, j))
    for i in range(M):
        for j in range(N):
            if box[i][j] == 1:
                bfs(i, j)

    box = sum(box, [])
    if box.count(0) > 0:
        return -1
    else:
        num_max = max(box)
        if num_max == -1:
            return -1
        else:
            return num_max - 1

if __name__ == "__main__":
    N, M = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(M)]

    days = tomato(N, M, box)
    print(days)
