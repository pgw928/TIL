import sys
from collections import deque
sys.stdin = open('section7/input.txt', 'rt')
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

inf, sup = float('inf'), -float('inf')
for g in graph:
    for i in range(n):
        if g[i] > sup:
            sup = g[i]
        if g[i] < inf:
            inf = g[i]


dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(node, limit):
    dq = deque()
    dq.append(node)
    visited[node[0]][node[1]] = 1
    while dq:
        y, x = dq.popleft()
        for k in range(4):
            b, a = y+dy[k], x+dx[k]
            if 0<=b<n and 0<=a<n and visited[b][a]==0 and graph[b][a]>limit:
                visited[b][a] = 1
                dq.append((b,a))

m = 1
for k in range(inf, sup):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0 and graph[i][j]>k:
                bfs((i,j), k)
                cnt += 1
    m = max(cnt, m)
print(m)