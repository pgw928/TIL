import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

dx, dy = [-1,-1,1,1,2,2,-2,-2], [2,-2,2,-2,1,-1,1,-1]
def bfs(start,end):
    dq, check = deque(), set()
    dq.append(start)
    check.add(start)
    while dq:
        y, x, s = dq.popleft()
        if (y,x)==end:
            return s
        for k in range(8):
            b, a = dy[k]+y, dx[k]+x
            if 0<=b<=n-1 and 0<=a<=n-1 and (b,a) not in check:
                dq.append((b,a,s+1))
                check.add((b,a))

for _ in range(t):
    n = int(input())
    a, b = map(int, input().split())
    end = tuple(map(int, input().split()))
    print(bfs((a,b,0),end))