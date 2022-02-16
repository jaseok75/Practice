"""
Project: 백준_2751_수 정렬하기2
Date: 2022.02.16.수.
Author: Kim-Harim
Comment:
- Silver 5
"""

import heapq
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    numbers = []
    for _ in range(n):
        data = int(input())
        heapq.heappush(numbers, data)
    while numbers:
        print(heapq.heappop(numbers))
