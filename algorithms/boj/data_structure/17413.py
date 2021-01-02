from sys import stdin
from collections import deque
input = stdin.readline().strip()


#---------------------------------
temp = []
i = 0
l = len(input)
while True:
    stack = []
    if input[i]==' ':
        temp.append(' ')
        i += 1

    elif input[i]=='<':
        stack.append('<')
        i += 1
        while input[i] != '>':
            stack.append(input[i])
            i+=1
        stack.append('>')
        temp.append(''.join(stack))
        i+=1
    elif input[i].isalpha() or input[i].isdecimal():
        stack.append(input[i])
        i += 1
        while input[i].isalpha() or input[i].isdecimal():
            stack.append(input[i])
            i+=1
            if i == l:
                break
        temp.append(''.join(stack))
    if i >= l-1:
        break
#---------------------------------

for i, s in enumerate(temp):
    if '<' in s or '>' in s:
        continue
    temp[i] = s[::-1]
print(''.join(temp))



