"""
Project: 프로그래머스 '숫자 문자열과 영단어'
Date: 2021.12.28.화
"""

data = input('input data : ')

while data.isdigit() == False:
    if 'one' in data:
        data = data.replace ('one', '1')
    elif 'two' in data:
        data = data.replace ('two', '2')
    elif 'three' in data:
        data = data.replace ('three', '3')
    elif 'four' in data:
        data = data.replace ('four', '4')
    elif 'five' in data:
        data = data.replace ('five', '5')
    elif 'six' in data:
        data = data.replace ('six', '6')
    elif 'seven' in data:
        data = data.replace ('seven', '7')
    elif 'eight' in data:
        data = data.replace ('eight', '8')
    elif 'nine' in data:
        data = data.replace ('nine', '9')
    elif 'zero' in data:
        data = data.replace ('zero', '0')

output_data = int(data)

print (output_data)