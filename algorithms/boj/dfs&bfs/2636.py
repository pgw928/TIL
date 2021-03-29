import sys; input=sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(start=(0, 0)):
    dq = deque()
    dq.append(start)
    visited = [[0]*m for _ in range(n)]
    visited[start[0]][start[1]] = 1
    while dq:
        y, x = dq.popleft()
        for k in range(4):
            yy, xx = y+dy[k], x+dx[k]
            if 0<=yy<n and 0<=xx<m and visited[yy][xx]==0:
                if graph[yy][xx]==1:
                    visited[yy][xx] = 2
                elif graph[yy][xx]==0:
                    visited[yy][xx] = 1
                    dq.append((yy, xx))

    count = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j]==2:
                graph[i][j] = 0
                count += 1
    return count

t = 0
tmp = 0
while True:
    count = bfs()
    if count:
        t += 1
        tmp = count
    else:
        break

print(t)
print(tmp)