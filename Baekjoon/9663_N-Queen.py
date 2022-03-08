"""
Project: 백준_9663_N-Queen
Date: 2022.03.08.화.
Comment:
- Gold 5
- 백트래킹
"""
from collections import deque


def attack_free(chess, x, y):
    global count_queen
    for i in range(n):
        for j in range(n):
            if i == x and j == y:
                continue
            elif (i == x or j == y or abs(i - x) == abs(j - y)) and chess[i][j] == count_queen:
                chess[i][j] = False
    return chess
    pass


def select_queen(chess, queen, x, y):
    global count_total, count_queen

    for i in range(n):
        for j in range(n):
            if i == x and j == y:
                continue
            elif (i == x or j == y or abs(i - x) == abs(j - y)) and not chess[i][j]:
                chess[i][j] = count_queen

    for i in range(n):
        for j in range(n):
            if not chess[i][j]:
                chess[i][j] = True
                queen.append((i, j))
                # chess = attack(chess, i, j)
                count_queen += 1
                select_queen(chess, queen, i, j)
                # 여기로 리턴이 되는데 왜 밑으로 안 가고 attack_free 함수로 이동하는거지?
                if count_queen == n:
                    count_total += 1
                    (q, p) = queen.pop()
                    chess = attack_free(chess, p, q)
                    count_queen = 0
                    chess[p][q] = False
                    return

    (p, q) = queen.pop()
    chess = attack_free(chess, p, q)
    count_queen -= 1
    chess[p][q] = False
    return # 이거 재귀 리턴하는데 왜 다시 attack_free 함수로 이동하는거지?
    pass


if __name__ == "__main__":
    n = int(input())
    chess = [[False] * n for _ in range(n)]
    queen = deque()
    count_queen = 0
    count_total = 0

    for i in range(n):
        for j in range(n):
            chess[i][j] = True
            queen.append((i, j))
            count_queen += 1
            select_queen(chess, queen, i, j)
            chess[i][j] = -1
