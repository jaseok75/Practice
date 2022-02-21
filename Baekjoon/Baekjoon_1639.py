"""
Project: 백준 1639
Date: 2021.12.31.금
Status: 시간 초과남..
"""

input_data = input()
mid = len (input_data) // 2
left, right = 0, 0
len_data = len (input_data)
if len_data % 2 != 0:
    len_data -= 1
len_luck = 0
len_start = 0

while mid > 0:
    left_data = input_data[left:mid]
    right_data = input_data[mid:len_data - right]
    if sum(map(int, left_data)) == sum(map(int, right_data)):
        if len_luck < (mid - left):
            len_luck = (mid - left)
        mid -= 1
        len_data -= 2
        left, right = 0, 0
    else:
        left += 1
        right += 1
    if len_luck > (mid - left) or mid - left == 0:
        mid -= 1
        len_data -= 2
        left, right = 0, 0
    if len_luck > mid:
        break

# print (len_luck)

len_data = len (input_data)
if len_data % 2 != 0:
    len_data -= 1
left, right = 0, 0
mid = len (input_data) // 2 + 1
len_start = 2

while mid < len_data:
    left_data = input_data[len_start + left:mid]
    right_data = input_data[mid:len_data - right]
    if sum(map(int, left_data)) == sum(map(int, right_data)):
        if len_luck < (mid - (len_start + left)):
            len_luck = (mid - (len_start + left))
            mid += 1
            len_start += 2
            left, right = 0, 0
    else:
        left += 1
        right += 1
    if (len_luck > (mid - (len_start + left))) or (mid - (len_start + left) == 0):
        mid += 1
        len_start += 2
        left, right = 0, 0
    if len_luck > (len_data - mid):
        break

print (len_luck * 2)