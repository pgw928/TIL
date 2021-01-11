import sys
from collections import deque

F, S ,G, U, D = map(int, sys.stdin.readline().split())

visited = [0]* (F+1)

def bfs(start_node, end_node, up, down, total):
    dq = deque()
    dq.append(start_node)
    visited[start_node] = 1
    while dq:
        print(visited)
        node = dq.popleft()
        if node == end_node:
            return (visited[node]-1)
        for n_node in [node+up, node-down]:
            if (1 <= n_node <= total) and (visited[n_node]==0):
                visited[n_node] = visited[node] + 1
                dq.append(n_node)
    return 'use the stairs'

print(bfs(S,G,U,D,F))