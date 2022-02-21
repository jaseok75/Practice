"""
Project: 프로그래머스 '실패율'
Date: 2022.1.3.월
"""

import operator

N = 2
stages = [1]
answer = []
failure = {}

for i in range(1, N + 1):
    n_clear = stages.count(i)
    player = 0
    for stage in stages:
        if stage >= i:
            player += 1
    if player == 0:
        fail = 0
    else:
        fail = n_clear / player
    failure[i] = fail
    answer.append(fail)

l_failure = list(zip(failure.keys(), failure.values()))
sorted_failure = sorted(l_failure, key = lambda x : (-x[1], x[0]))
answer = [x[0] for x in sorted_failure]

print (answer)