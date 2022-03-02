"""
Project: 백준_2579_계단 오르기
Date: 2022.03.02.수
Comment:
- Level 3
- 동적 계획법
"""

def solve(steps):
    if n == 1:
        print(steps[n - 1])
        return
    elif n == 2:
        print(steps[0] + steps[1])
        return

    answer = []
    answer.append(steps[0])
    answer.append(max(steps[0] + steps[1], steps[1]))
    answer.append(max(steps[0] + steps[2], steps[1] + steps[2]))
    for i in range(3, n):
        answer.append(max(answer[i - 2] + steps[i], answer[i - 3] + steps[i] + steps[i - 1]))
    print(answer[n - 1])

if __name__ == "__main__":
    n = int(input())
    steps = []
    for _ in range(n):
        step = int(input())
        steps.append(step)
    solve(steps)
