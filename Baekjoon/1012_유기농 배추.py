"""
Project: 백준_1012_유기농 배추
Date: 2022.01.31.월
Author: Kim-Harim
Comment:
- DFS/BFS 기법, DFS로 해결
- Silver 2
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def isRange(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

def dfs(x, y):
    visited[x][y] = False
    for i in range(4):
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        nx = x + dx[i]
        ny = y + dy[i]
        if isRange(nx, ny) and visited[nx][ny] and field[nx][ny] == 1:
            dfs(nx, ny)
    return

def solve(field, visited):
    count = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] and field[i][j] == 1:
                count += 1
                dfs(i, j)
    return count

if __name__ == "__main__":
    t = int(input())
    m, n = 0, 0
    answer = 0
    for _ in range(t):
        m, n, k = map(int, input().split())
        field = [[0] * m for i in range(n)]
        visited = [[True] * m for i in range(n)]
        for i in range(k):
            x, y = map(int, input().split())
            field[y][x] = 1
        answer = solve(field, visited)
        print(answer)
