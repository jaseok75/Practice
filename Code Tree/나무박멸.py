from collections import deque


def cnt_yes_tree(x, y): # 인접한 네 개의 칸 중 나무가 있는 칸 수 세기 (solution_1)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    result = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and Tree_Info[nx][ny] > 0:
            result += 1

    return result


def solution_1():   # 나무 성장
    for i in range(n):
        for j in range(n):
            if Tree_Info[i][j] > 0:
                Tree_Info[i][j] += cnt_yes_tree(i,j)


def cnt_no_tree(x, y):  # 인접한 네 개의 칸 중 나무가 없는 칸 수 세기 (solution_2)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    no_Tree = deque()

    result = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and Tree_Info[nx][ny] == 0:
            result += 1
            no_Tree.append((nx, ny))

    return result, no_Tree


def solution_2():   # 나무 번식
    after_breeding = [[x for x in y] for y in Tree_Info]    # 번식하기 전과 후를 나누기 위함 -> 번식한 후
    for i in range(n):
        for j in range(n):
            if Tree_Info[i][j] > 0:
                cnt_blank, position = cnt_no_tree(i, j)
                if cnt_blank == 0:  # 나무 번식할 곳 없으면 번식 안하고 건너뛰기
                    continue
                cnt_breeding = Tree_Info[i][j] // cnt_blank # 번식해서 심을 나무 수
                while position:
                    x, y = position.popleft()
                    after_breeding[x][y] += (Tree_Info[x][y] + cnt_breeding)
    return after_breeding


def solution_3(after_breeding):   # 제초제 뿌리기
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, 1, -1]
    spray = [[x for x in y] for y in after_breeding]
    max_spray = 0
    max_spray_x, max_spray_y = 0, 0
    for i in range(n):
        for j in range(n):
            if after_breeding[i][j] == 0:
                spray[i][j] = 0
                if max_spray < spray[i][j]:
                    max_spray = spray[i][j]
                    max_spray_x, max_spray_y = i, j
            elif after_breeding[i][j] > 0:
                for f_t in range(4):
                    for e in range(k):
                        nx = i + dx[f_t] * e + dx[f_t]  # 제초제를 끝까지 뻗어나가게 하기 위함
                        ny = j + dy[f_t] * e + dy[f_t]
                        if 0 <= nx < n and 0 <= ny < n and after_breeding[nx][ny] > 0:  # 박멸되는 나무 수 구하기
                            spray[i][j] += after_breeding[nx][ny]
                        else:   # 더 이상 제초제를 뿌릴 수 없으면 그만하고 나가기
                            break
                if max_spray < spray[i][j]:
                    max_spray = spray[i][j] # 가장 많이 박멸되는 나무 수
                    max_spray_x, max_spray_y = i, j  # 제초제 뿌릴 나무 위치

    Zero_Space[max_spray_x][max_spray_y] = c + 1
    after_breeding[max_spray_x][max_spray_y] = -c - 1
    for f_t in range(4):
        for e in range(k):
            nx = max_spray_x + dx[f_t] * e + dx[f_t]
            ny = max_spray_y + dy[f_t] * e + dy[f_t]
            if 0 <= nx < n and 0 <= ny < n and after_breeding[nx][ny] > 0:
                Zero_Space[nx][ny] = c + 1  # 박멸된 나무 위치 기억하기
                after_breeding[nx][ny] = -c - 1     # 나무 박멸됨, c년 동안 유지할 것
            elif 0 <= nx < n and 0 <= ny < n and after_breeding[nx][ny] == 0:
                Zero_Space[nx][ny] = c + 1  # 박멸된 나무 위치 기억하기
                after_breeding[nx][ny] = -c - 1     # 나무 박멸됨, c년 동안 유지할 것
                break
            elif 0 <= nx < n and 0 <= ny < n and after_breeding[nx][ny] < 0 and [nx, ny] not in Break_Space:
                Zero_Space[nx][ny] = c + 1  # 박멸된 나무 위치 기억하기
                after_breeding[nx][ny] = -c - 1    # 나무 박멸됨, c년 동안 유지할 것
                break
            else:
                break

    for i in range(n):
        for j in range(n):
            Tree_Info[i][j] = after_breeding[i][j]

    return max_spray


if __name__ == "__main__":
    # 격자의 크기(n), 박멸이 진행되는 년 수(m), 제초제의 확산 범위(k), 제초제가 남아있는 년 수(c)
    n, m, k, c = list(map(int, input().split()))
    Tree_Info = [list(map(int, input().split())) for _ in range(n)]
    Break_Space = []
    Zero_Space = [[0] * n for _ in range(n)]
    for q in range(n):
        for w in range(n):
            if Tree_Info[q][w] == -1:
                Break_Space.append([q, w])

    result_sum = 0
    for _ in range(m):
        solution_1()
        breeding = solution_2()
        sol_3 = solution_3(breeding)
        result_sum += sol_3

        for q in range(n):
            for w in range(n):
                if Zero_Space[q][w] > 0:
                    Zero_Space[q][w] -= 1
                    Tree_Info[q][w] += 1

    print(result_sum)
