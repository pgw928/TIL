import sys; input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
res = set()
def bfs(start):
    dq = deque()
    dq.append(start)
    while dq:
        y, x = dq.popleft()
        for k in range(4):
            b, a = y+dy[k], x+dx[k]
            if 0<=b<n and 0<=a<m and visited[b][a]==0:
                if graph[b][a]==1:
                    visited[b][a] = 1
                    dq.append((b, a))
    size = 0
    for v in visited:
        size += sum(v)
    return size
M = 1
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            cnt = 0
            for k in range(4):
                b, a = i + dy[k], j + dx[k]
                if 0<=b<n and 0<=a<m and graph[b][a]==1:
                    cnt += 1
            if cnt>0:
                visited = [[0] * m for _ in range(n)]
                visited[i][j] = 1
                M = max(M, bfs((i, j)))
print(M)
