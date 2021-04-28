import sys; input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
graph = dict()
for _ in range(m):
    a, b, c = map(int, input().split())
    if a not in graph:
        graph[a] = [(b,c)]
    else:
        graph[a].append((b,c))
    if b not in graph:
        graph[b] = [(a, c)]
    else:
        graph[b].append((a, c))


s, e = map(int, input().split())

def bfs(s, e, m):
    dq = deque()
    dq.append(s)
    visited = [0] * (n + 1)
    visited[s] = 1
    while dq:
        x = dq.popleft()
        if x==e:
            return True
        for y,c in graph[x]:
            if visited[y]==0 and c >=m:
                dq.append(y)
                visited[y] = 1
    return False

i ,j = 1, 1_000_000_000
while i<j-1:
    m = (i+j)//2
    if bfs(s, e, m):
        i = m
    else:
        j = m
if bfs(s,e,j):
    print(j)
else:
    print(i)