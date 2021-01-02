import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
dq = deque()

for _ in range(N):
    tmp = input().split()
    if len(tmp)>1:
        op, num = tmp[0], int(tmp[1])
    else:
        op = tmp[0]
    # print(dq)
    if op=='push':
        dq.append(num)
    elif op=='pop':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif op=='size':
        print(len(dq))
    elif op=='empty':
        if dq:
            print(0)
        else:
            print(1)
    elif op=='front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif op=='back':
        if dq:
            print(dq[-1])
        else:
            print(-1)



