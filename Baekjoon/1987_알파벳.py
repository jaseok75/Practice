"""
Project: 백준_1987_알파벳
Date: 2022.01.31.월
Author: Kim-Harim
Comment:
- BFS 기법 사용
- DFS는 실패했다. 이때까지 지나온 모든 칸에 적혀 있는 알파벳 관리를 하지 못했다.
- 이때까지 지나온 모든 칸에 적혀 있는 알파벳과 달라야한다. 이 조건 너무 빡세다.
- 아직 해결하지 못함
- Gold 4
"""

from collections import deque

def isRange(x, y):
    if 0 <= x < r and 0 <= y < c:
        return True
    return False

def bfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    q.append((x, y))
    c_distance = distance
    distance[x][y] += board[x][y]
    print(distance)
    while q:
        (x, y) = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if isRange(nx, ny) and board[nx][ny] not in distance[x][y]:
                distance[nx][ny] += (distance[x][y] + board[nx][ny])
                q.append((nx, ny))
    return

if __name__ == "__main__":
    r, c = map(int, input().split())
    board = [list(input()) for _ in range(r)]
    distance = [[''] * c for _ in range(r)]
    bfs(0, 0)
