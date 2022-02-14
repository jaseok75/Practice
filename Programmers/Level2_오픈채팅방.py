"""
Project: 프로그래머스_오픈채팅방
Date: 2022.02.14.월.
Comment:
- Level 2
"""

def solution(record):
    answer = []
    user = dict()

    for input_msg in record:
        data = input_msg.split(' ')
        if (data[0] == "Enter"):
            user[data[1]] = data[2]
        elif (data[0] == "Change"):
            user[data[1]] = data[2]

    for input_msg in record:
        data = input_msg.split(' ')
        if (data[0] == "Enter"):
            answer.append(user[data[1]] + "님이 들어왔습니다.")
        elif (data[0] == "Leave"):
            answer.append(user[data[1]] + "님이 나갔습니다.")

    return answer

if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))
