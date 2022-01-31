"""
Project: 백준_1753_최단경로
Date: 2022.01.31.월
Author: Kim-Harim
Comment:
- Dijkstra 기법
- heapq 모듈 사용
"""

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(x, graph):
    q = []
    heapq.heappush(q, (0, x))
    distance = [INF] * (v + 1)
    distance[x] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

if __name__ == "__main__":
    v, e = map(int, input().split())
    k = int(input())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    answer = dijkstra(k, graph)
    for i in range(1, v + 1):
        if answer[i] == INF:
            print("INF")
        else:
            print(answer[i])
