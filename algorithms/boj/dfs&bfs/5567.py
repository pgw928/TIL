import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

temp = []
for _ in range(m):
    temp.append(tuple(map(int, sys.stdin.readline().split())))

graph = { i :[] for i in range(1,n+1)}

for i in range(m):
    x, y = temp[i]
    graph[x].append(y)
    graph[y].append(x)

print(graph)

from collections import deque

start_nodes = graph[1]
def bfs(start_nodes):
    visited = []
    dq = deque()
    dq.extend(start_nodes)
    for j in range(2):
        for i in range(len(dq)):
            node = dq.popleft()
            if node not in visited:
                visited.append(node)
                dq.extend(graph[node])
    return visited
print(len(bfs(start_nodes))-1)