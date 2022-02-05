"""
Project: 백준_9095_1,2,3 더하기
Date: 2022.02.05.토.
Author: Kim-Harim
Comment:
- Silver 3
"""

def solve(persons):
    persons.sort()
    for i in range(1,n):
        persons[i] += persons[i - 1]
    print(sum(persons))

if __name__ == "__main__":
    n = int(input())
    persons = list(map(int, input().split()))
    solve(persons)
