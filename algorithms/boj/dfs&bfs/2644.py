import sys

n = int(sys.stdin.readline())
a,b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = { i : [] for i in range(1,n+1) }
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

print(graph)
point = [0]*(n+1)
point[a]=1
from collections import deque
def bfs(start_node=a):

    visited = []
    dq = deque()
    dq.append(start_node)
    k = 0
    while dq:
        node = dq.popleft()
        if node not in visited:
            visited.append(node)
            tmp = graph[node]
            l = len(tmp)
            for j in range(l):
                if point[tmp[j]] == 0:
                    point[tmp[j]] += (1+point[node])
            dq.extend(graph[node])
    return visited


bfs()
print(-1 if point[b]==0 else point[b]-1)