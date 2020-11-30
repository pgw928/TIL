import sys

# INPUT 받아오기
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
temp_graph = []
for _ in range(M):
    temp_graph.append(list(map(int, sys.stdin.readline().split())))
graph = {i : [] for i in range(1,N+1)}

# graph 만들기
for i in range(M):
    n = temp_graph[i][0]
    m = temp_graph[i][1]
    graph[m].append(n)
    graph[n].append(m)

from collections import deque
def bfs(start_node):
    visited = []
    dq = deque()
    dq. append(start_node)
    while dq:
        node = dq.popleft()
        if node not in visited:
            visited.append(node)
            dq.extend(graph[node])
    print(visited)
    return (len(visited)-1)

print(bfs(1))
