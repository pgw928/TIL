import sys; input = sys.stdin.readline

from collections import deque

n, m = map(int,input().split())
graph = {i:[] for i in range(1, n+1) }
for _ in range(m):
    a, b = map(int,input().split())
    graph[b].append(a)

def bfs(start):
    dq, visited = deque(), [0]* (1+n)
    dq.append(start)
    visited[start] = 1
    while dq:
        x = dq.popleft()
        for n_n in graph[x]:
            if visited[n_n]==0:
                dq.append(n_n)
                visited[n_n]=1
    return len([a for a in visited if a==1])

result = {}
for i in range(1, n+1):
    if graph[i]:
        tmp = bfs(i)
        result[i]= tmp
M = max(result.values())
ret = ' '.join(map(str, sorted([a for a, b in result.items() if b==M])))
print(ret)