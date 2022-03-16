"""
Project: 백준_11053_가장 긴 증가하는 부분 수열
Date: 2022.03.16.수.
Comment:
- 이진 탐색
- 동적계획법
"""

# 이진 탐색 실패했다.
"""
def binary_search(array, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid
    return end


if __name__ == "__main__":
    n = int(input())
    arr_A = list(map(int, input().split()))
    LIS = [arr_A[0]]
    idx = 0

    for i in range(1, len(arr_A)):
        if arr_A[i] > LIS[idx]:
            idx += 1
            LIS.append(arr_A[i])
        else:
            p = binary_search(LIS, arr_A[i], 0, idx)
            LIS[p] = arr_A[i]
    print(LIS)
    print(len(LIS))
"""

# 동적 계획법
if __name__ == "__main__":
    n = int(input())
    arr_A = list(map(int, input().split()))
    LIS = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr_A[j] < arr_A[i]:
                LIS[i] = max(LIS[i], LIS[j] + 1)

    print(max(LIS))
