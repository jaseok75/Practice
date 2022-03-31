"""
Project: 백준_14891_톱니바퀴
Date: 2022.03.31.목.
Comment:
- 삼성 기출 문제
list_name = 회전시킬 리스트
rotate = int(list_name.pop(0))%len(list_name)
rotate_list = list_name[len(list_name)-rotate:]+list_name[:len(list_name)-rotate]
"""

from collections import deque


def turn(gear, num, direct):
    connect = [-1, 1]
    default_num = deque()
    default_num.append(num)
    turn_gear = deque()
    turn_gear.append((num, direct))
    while turn_gear:
        num, direct = turn_gear.popleft()
        # 양 옆에 톱니바퀴 확인해서 돌릴 톱니바퀴 선택
        for i in range(2):
            connect_gear = num + connect[i]
            if 0 <= connect_gear < 4 and not default_num.count(connect_gear) and gear[connect_gear][2 * (-connect[i])] != gear[num][2 * connect[i]]:
                turn_gear.append((connect_gear, direct * (-1)))
                default_num.append(connect_gear)
        # 톱니바퀴 회전
        gear[num] = gear[num][direct * (-1):] + gear[num][:direct * (-1)]
    return gear


def solution(gear, k):
    for _ in range(k):
        num, direct = map(int, input().split())
        gear = turn(gear, num - 1, direct)
    result = 0
    for i in range(4):
        result += (int(gear[i][0]) * (2 ** i))
    print(result)
    pass


if __name__ == "__main__":
    gear = [list(str(input())) for i in range(4)]
    k = int(input())
    solution(gear, k)
