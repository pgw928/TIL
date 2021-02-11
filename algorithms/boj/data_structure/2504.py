import sys
from collections import deque
input = sys.stdin.readline
A = input().strip()

sum = 0
dq = deque()
tmp = deque()
dq.append(A[0])

for idx, s in enumerate(A[1:],1):
    if (s=='(') or (s=='['):
        dq.append(s)
        if A[idx-1]==')' or A[idx-1]==']':
            tmp.append('+')

    elif (s==')'):
        if A[idx-1] == '(':
            dq.pop()
            tmp.append(2)
        else:
            dq.pop()
            tmp.append(tmp.pop()*2)
            tmp.append('*')

    elif (s == ']'):
        if A[idx-1] == '[':
            dq.pop()
            tmp.append(3)
        else:
            dq.pop()
            tmp.append(tmp.pop()*3)
            tmp.append('*')

print(tmp)


