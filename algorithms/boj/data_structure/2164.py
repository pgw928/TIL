import sys
from collections import deque

input = sys.stdin.readline
n= int(input())

dq = deque(range(1,n+1))
while len(dq)>1:
    dq.popleft()
    dq.rotate(-1)

print(dq[0])