"""
Project: 백준_7576_토마토
Date: 2022.03.03.목
Comment:
- Gold 5
- BFS
"""

from collections import deque

def isRange(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False

def bfs(tomato):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    c_box = box

    while tomato:
        (x, y) = tomato.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isRange(nx, ny) and box[nx][ny] == 0:
                tomato.append((nx, ny))
                box[nx][ny] = box[x][y] + 1

if __name__ == "__main__":
    m, n = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    tomato = deque()

    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                tomato.append((i, j))

    bfs(tomato)

    max_days = 0
    flag = 0
    for i in range(n):
        if box[i].count(0) != 0:
            print("-1")
            flag = 1
            break
        else:
            days = max(box[i])
            max_days = max(days, max_days)
    if flag == 0:
        print(max_days - 1)
