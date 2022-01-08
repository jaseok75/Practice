"""
Project: 백준_단지번호붙이기_2667
Date: 2022.01.08.토.
"""

def isRange(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False

def dfs(x, y):
    global count_house
    visited[x][y] = 1
    count_house += 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if isRange(nx, ny) and visited[nx][ny] == 0 and house_map[nx][ny] == 1:
            dfs(nx, ny)
    return count_house

if __name__ == "__main__":
    N = int(input())
    house_map = []
    visited = [[0 for x in range(N)] for _ in range(N)]
    house = []
    count_house = 0
    for i in range(N):
        input_map = input()
        house_map.append(list(map(int, input_map)))

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and house_map[i][j] == 1:
                count_house = 0
                count_house = dfs(i, j)
                house.append(count_house)

    house.sort()
    print(len(house))
    for i in house:
        print(i)
