import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

def solution():
    ps = list(input().strip())[::-1]
    dq = deque()
    while ps:
        p = ps.pop()
        if p == ')':
            if dq:
                dq.popleft()
            else:
                return 'NO'
        else:
            dq.append(p)
    if dq:
        return 'NO'
    return 'YES'

for _ in range(T):
    print(solution())

