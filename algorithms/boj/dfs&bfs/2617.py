import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = {i:[] for i in range(1,n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,-1)) # a>b 일때 a 에 넣으면 -1
    graph[b].append((a, 1))  # a>b 이면 b에 넣으면 1

def bfs(start):
    dq = deque()
    check_greater, check_less = set(), set()
    dq.append((start, 1))
    dq.append((start, -1))

    while dq:
        node, s = dq.popleft()
        for n_n, n_s in graph[node]:
            if n_n not in check_greater:
                if s==1 and n_s==1:
                    dq.append((n_n, n_s))
                    check_greater.add(n_n)
            if n_n not in check_less:
                if s==-1 and n_s==-1:
                    dq.append((n_n, n_s))
                    check_less.add(n_n)

    if len(check_greater)> n//2 or len(check_less)>n//2:
        return 1
    return 0

count = 0
for i in range(1, n+1):
    count += bfs(i)
print(count)
