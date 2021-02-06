import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int,input().split())
graph = {i:[] for i in range(1, n+1) }
for _ in range(m):
    a, b = map(int,input().split())
    graph[b].append(a)

print(graph)

def bfs(start):
    dq =deque()
    dq.append((start, 1))
    check = set()
    check.add(start)
    while dq:
        node , c = dq.popleft()
        for n_node in graph[node]:
            if n_node not in check:
                dq.append((n_node, c+1))
                check.add(n_node)
    return c


start_nodes = []
for i in range(1, n+1):
    if graph[i]:
        for j in graph[i]:
            if graph[j]:
                start_nodes.append(i)
print(f'start_nodes:{start_nodes}')

result = {}
for node in start_nodes:
    result[node] = bfs(node)

M = max([b for (a,b) in result.items()])
ans = [a for (a,b) in result.items() if b==M]
print(' '.join(map(str, ans)))