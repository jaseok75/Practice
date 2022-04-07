"""
Project: codeup_계단 오르기2.py
Date: 2022.04.08.금.
Comment:
- 동적계획법
"""

from collections import deque


def solution(n):
    step = deque(maxlen=3)
    step.append(1)
    if n >= 2:
        step.append(2)
    if n >= 3:
        step.append(4)
    for i in range(4, n + 1):
        new_step = (step[0] + step[1] + step[2]) % 1000
        step.append(new_step)
    return step.pop()


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
