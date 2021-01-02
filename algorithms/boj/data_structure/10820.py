import sys

input = sys.stdin.readline

def solution(s):
    result = [0, 0, 0, 0]
    for i in s:
        if i.isdecimal():
            result[2] += 1
        elif i.islower():
            result[0] += 1
        elif i.isupper():
            result[1] += 1
        elif i==' ':
            result[3] += 1
    if result ==[0, 0, 0, 0]:
        return -1
    return ' '.join(map(str, result))

while 1:
    try:
        s = input()
        res = solution(s)
        if res == -1:
            break
        else:
            print(res)
    except EOFError:
        break