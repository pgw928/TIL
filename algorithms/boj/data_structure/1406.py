import sys
from collections import deque
input = sys.stdin.readline

dq1 = deque(input().strip())
dq2 = deque()
N = len(dq1)
M = int(input())

for _ in range(M):
    order = input().split()
    if order[0]=='P':
        dq1.append(order[1])
    elif order[0] == 'L':
        if dq1:
            dq2.appendleft(dq1.pop())
    elif order[0] == 'D':
        if dq2:
            dq1.append(dq2.popleft())
    elif order[0] == 'B':
        if dq1:
            dq1.pop()
print(''.join(dq1)+''.join(dq2))


