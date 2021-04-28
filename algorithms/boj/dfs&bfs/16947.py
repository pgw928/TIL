import sys; input= sys.stdin.readline
from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n):
    a, b  = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

flag = False
def dfs(x):
    global cycle, flag
    for y in graph[x]:
        if visited[y]==-1:
            visited[y] = visited[x] + 1
            dfs(y)
            visited[y] = -1
        if y==i and visited[x]-visited[i]> 1:
            cycle = {idx for idx, v in enumerate(visited) if v>-1}
            flag = True

def bfs(x):
    dq, visited = deque(), [-1]*(n+1)
    dq.append(x)
    visited[x] = 0
    while dq:
        y = dq.popleft()
        if y in cycle:
            return visited[y]
        else:
            for z in graph[y]:
                if visited[z]==-1:
                    visited[z] = visited[y] + 1
                    dq.append(z)


for i in range(1, n+1):
    visited = [-1]*(n+1)
    visited[i] = 0
    dfs(i)
    if flag:
        break

result = [0]*(n+1)
for i in range(1,n+1):
    if i not in cycle:
        result[i] = bfs(i)
print(' '.join(list(map(str,result[1:]))))