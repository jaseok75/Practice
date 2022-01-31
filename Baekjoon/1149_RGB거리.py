"""
Project: 백준_1149_RGB거리
Date: 2022.01.31.월
Author: Kim-Harim
Comment:
- 동적 계획법
- 시도 몇 번만에 드디어 성공!~!
"""

def solve(costs):
    answers = [[0] * 3 for _ in range(n)]
    answers[0][0] = costs[0][0]
    answers[0][1] = costs[0][1]
    answers[0][2] = costs[0][2]
    for i in range(1, n):
        for j in range(3):
            if j == 0:
                answers[i][j] = costs[i][j] + min(answers[i - 1][1], answers[i - 1][2])
            elif j == 1:
                answers[i][j] = costs[i][j] + min(answers[i - 1][0], answers[i - 1][2])
            elif j == 2:
                answers[i][j] = costs[i][j] + min(answers[i - 1][0], answers[i - 1][1])
    return min(answers[n - 1])

if __name__ == "__main__":
    n = int(input())
    costs = [list(map(int, input().split())) for _ in range(n)]
    answer = solve(costs)
    print(answer)
