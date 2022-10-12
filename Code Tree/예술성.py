def dfs(x, y):  # 그룹 나누기에 필요한 함수 (mat_beautiful)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited[x][y] = True
    Group[idx].append((x, y))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and Picture[x][y] == Picture[nx][ny]:
            dfs(nx, ny)
    return


def adjacency_group(a, b):  # 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수 세기
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    result = 0
    for idx_a in range(len(Group[a])):
        x, y = Group[a][idx_a][0], Group[a][idx_a][1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) in Group[b]:
                result += 1

    return result


def mat_beautiful():
    global idx, Group, visited

    # 그룹 나누기
    Group = []
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                Group.append([])
                dfs(i, j)
                idx += 1

    # 조화로움 계산
    sum_beauty = 0
    len_Group = len(Group)
    for i in range(len_Group):
        for j in range(i + 1, len_Group):
            cnt_adj = adjacency_group(i, j)
            if cnt_adj > 0:
                sum_beauty += ((len(Group[i]) + len(Group[j])) * Picture[Group[i][0][0]][Group[i][0][1]] * Picture[Group[j][0][0]][Group[j][0][1]] * cnt_adj)

    return sum_beauty


def turn_middle():
    after_turn = [[0] * n for _ in range(n)]

    # 십자가 돌리기
    idx_middle = n // 2
    for i in range(n):
        after_turn[idx_middle][i] = Picture[i][idx_middle]
        after_turn[(n - 1) - i][idx_middle] = Picture[idx_middle][i]

    # 십자가를 기준으로 4개 덩어리 돌리기
    for i in range(idx_middle):
        for j in range(idx_middle):
            after_turn[j][(idx_middle - 1) - i] = Picture[i][j]  # 왼쪽 위
            after_turn[j][(n - 1) - i] = Picture[i][(idx_middle + 1) + j]   # 오른쪽 위
            after_turn[(idx_middle + 1) + j][(idx_middle - 1) - i] = Picture[(idx_middle + 1) + i][j]   # 왼쪽 아래
            after_turn[(idx_middle + 1) + j][(n - 1) - i] = Picture[(idx_middle + 1) + i][(idx_middle + 1) + j]     # 오른쪽 아래

    for i in range(n):
        for j in range(n):
            Picture[i][j] = after_turn[i][j]


if __name__ == "__main__":
    n = int(input())
    Picture = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    Group = []  # 그룹을 나눔
    total_result = 0

    idx = 0
    total_result += mat_beautiful()
    turn_middle()
    idx = 0
    total_result += mat_beautiful()
    turn_middle()
    idx = 0
    total_result += mat_beautiful()
    turn_middle()
    idx = 0
    total_result += mat_beautiful()
    print(total_result)
