"""
Project: 백준_2606_바이러스
Date: 2022.02.15.화.
Author: Kim-Harim
Comment:
- Silver 3
왜 틀렸지..
"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i
    for _ in range(m):
        a, b = map(int, input().split())
        union_parent(parent, a, b)
    print(parent)
    print(parent.count(1) - 1)
