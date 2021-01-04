import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())


visited = [0]* (10**5+1)


def bfs(start_node, end_node):
    dq = deque()
    dq.append(start_node)
    visited[start_node] = 1
    while dq:
        node = dq.popleft()
        if node == end_node:
            return visited[node]-1
        for i, n_node in enumerate([node*2, node-1, node+1]):
            if 0 <= n_node <= 10**5 and visited[n_node]==0:
                if i!=0:
                    visited[n_node] = visited[node] + 1
                    dq.append(n_node)
                else:
                    visited[n_node] = visited[node]
                    dq.append(n_node)

print(bfs(N, K))

