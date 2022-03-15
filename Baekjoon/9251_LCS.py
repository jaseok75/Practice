"""
Project: 백준_9251_LCS
Date: 2022.03.15.화.
Comment:
- 동적 계획법
"""

if __name__ == "__main__":
    string_A = input()
    string_B = input()
    len_A = len(string_A) + 1
    len_B = len(string_B) + 1
    LCS = [[0] * len_A for _ in range(len_B)]

    # 최장 공통 부분수열 길이 구하기
    for i in range(1, len_B):
        for j in range(1, len_A):
            if string_A[j - 1] == string_B[i - 1]:
                LCS[i][j] = LCS[i - 1][j - 1] + 1
            else:
                LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
    print(LCS[len_B - 1][len_A - 1])

    # 최장 공통 부분수열 찾기
    i, j = len_B - 1, len_A - 1
    result = ''
    while LCS[i][j] != 0:
        if LCS[i][j] == LCS[i - 1][j]:
            i -= 1
        elif LCS[i][j] == LCS[i][j - 1]:
            j -= 1
        else:
            result += string_A[j - 1]
            i, j = i - 1, j - 1
    print(''.join(reversed(result)))
