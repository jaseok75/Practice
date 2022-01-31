"""
Project: 백준_1463_1로 만들기
Date: 2022.01.31.월
Author: Kim-Harim
Comment:
- 동적 프로그래밍 기법
- 동빈나 동적 프로그래밍에 '1로 만들기'와 비슷한 문제
"""

# 재귀 함수 방법
"""
s={1:0,2:1}
def f(n):
 if n in s:return s[n]
 m=1+min(f(n//2)+n%2,f(n//3)+n%3)
 s[n]=m
 return m
"""

def solve(n):
    answer = [0] * 1000001

    for i in range(2, n + 1):
        answer[i] = answer[i - 1] + 1
        if i % 3 == 0:
            answer[i] = min(answer[i], answer[i // 3] + 1)
        if i % 2 == 0:
            answer[i] = min(answer[i], answer[i // 2] + 1)
        answer[i] = min(answer[i], answer[i - 1] + 1)
    return answer[n]

if __name__ == "__main__":
    n = int(input())
    answer = solve(n)
    print(answer)
