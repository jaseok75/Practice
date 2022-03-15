"""
Project: 백준_9251_LCS
Date: 2022.03.15.화.
Comment:
- 동적 계획법
- 이것도 메모리 제한 좀 있네
"""

if __name__ == "__main__":
    string_A = input()
    string_B = input()
    len_A = len(string_A) + 1
    len_B = len(string_B) + 1
    LCS = [[0] * len_A for _ in range(len_B)]

    for i in range(1, len_B):
        for j in range(1, len_A):
            if string_A[j - 1] == string_B[i - 1]:
                LCS[i][j] = LCS[i - 1][j - 1] + 1
            else:
                LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

    print(max(LCS[len_B - 1]))
