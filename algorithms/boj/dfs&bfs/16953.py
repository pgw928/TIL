import sys
from collections import deque
a, b = map(int, sys.stdin.readline().split())

def bfs(start):
    check = set()
    dq = deque()
    dq.append((start,1))
    check.add(start)
    while dq:
        n, c = dq.popleft()
        print(n, c)
        if n==b:
            return c
        for n_n in [2*n, int(str(n)+'1')]:
            if n_n<=b and (n_n not in check):
                dq.append((n_n, c+1))
                check.add(n_n)
    return -1

print(bfs(a))