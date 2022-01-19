"""
Project: 백준_2750_수 정렬하기
Date: 2022.01.18.화.
Comment:
- 오늘은 조금 피곤한 관계로 이거만 하자^-^
- 내일부터 다시 하자^---^
"""

if __name__ == "__main__":
    n = int(input())
    number = [int(input()) for _ in range(n)]
    number.sort()
    for numbers in number:
        print(numbers)
