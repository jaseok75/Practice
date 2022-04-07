"""
Project: 백준_19236_청소년 상어
Date: 2022.04.05.화.
Comment:
- 백트래킹
- 삼성 기출 문제
- 아직 뒷 부분 구현 덜 함.
"""

from collections import deque


def move(board, x, y):
    nx = x + dx[board[x][y + 1]]
    ny = y + dy[board[x][y + 1]]
    if 0 <= nx < 7 and 0 <= ny < 7 and board[nx][ny] != -1:
        board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
        board[x][y + 1] = board[x][y + 1]
        board[nx][ny + 1], board[x][y + 1] = board[x][y + 1], board[nx][ny + 1]
        return board
    for i in range(1, 9):
        next = (board[x][y + 1] + i) % 8
        if next == 0:
            next = 1
        nx = x + dx[next]
        ny = y + dy[next]
        if 0 <= nx < 7 and 0 <= ny < 7 and board[nx][ny] != -1:
            board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
            board[x][y + 1] = next
            board[nx][ny + 1], board[x][y + 1] = board[x][y + 1], board[nx][ny + 1]
            return board
    return board


def fish_move(board, shark):
    num = 1
    while num <= 16:
        for i in range(4):
            for j in range(0, 7, 2):
                if shark.count(num):
                    num += 1
                if board[i][j] == num:
                    board = move(board, i, j)
                    num += 1
                    for idx in board:
                        print(idx)
                    print()
    return board


def shark_move():
    pass


def solution(board, x, y, eat):
    shark = deque()
    shark.append(board[x][y])
    eat += board[x][y]
    board[x][y] = -1

    # 물고기 이동
    board = fish_move(board, shark)

    # 상어 이동

    pass


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(4)]
    dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 0, -2, -2, -2, 0, 2, 2, 2]
    eat = 0
    solution(board, 0, 0, eat)
