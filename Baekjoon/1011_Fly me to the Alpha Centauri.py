"""
Project: 백준_1011_Fly me to the Alpha Centauri
Date: 2022.03.14.월.
Comment:
- 백트래킹
- 시간초과 남.
- n만큼 다 도는 것이 아니라 스텝별로 돌게 구성하면 시간초과 해결될 듯
"""


def solution(x, y):
    distance = y - x
    count = 0
    move = 1
    move_count = 1
    p = move_count
    flag = 0
    while True:
        count += 1
        if count == distance:
            break
        p -= 1
        if p == 0:
            flag += 1
            move += 1
            if flag % 2 == 0:
                move_count += 1
                p = move_count
            else:
                p = move_count
    print(move)
    pass


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        solution(x, y)
