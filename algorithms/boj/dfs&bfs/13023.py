import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = { i : [] for i in range(N)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0

def dfs(start_node, depth):
    global ans
    node = start_node
    visited[node] = 1
    # print('depth:', depth, 'N:', N)
    if depth == N:
        ans = 1
        return

    n_nodes = graph[node]
    for n_node in n_nodes:
        if not visited[n_node]:
            dfs(n_node, depth+1)
            visited[n_node] = 0
    return

for i in range(N):

    visited = [0] * N
    dfs(i, 1)
print(ans)


