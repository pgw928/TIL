import sys
from collections import deque

input = sys.stdin.readline

N, M , V = map(int, input().split())

graph =[ [] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    visited = []
    visited.append(start)
    dq = deque()
    dq.append(start)

    while dq:
        node = dq.popleft()
        for n_node in sorted(graph[node]):
            if n_node not in visited:
                visited.append(n_node)
                dq.append(n_node)
    return visited


def dfs(start):
    visited, stack = [], []
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
        for n_node in sorted(graph[node], reverse=True):
            if n_node not in visited:
                stack.append(n_node)

    return visited

result1 = dfs(V)
result2 = bfs(V)
print(' '.join(map(str, result1)))
print(' '.join(map(str, result2)))
