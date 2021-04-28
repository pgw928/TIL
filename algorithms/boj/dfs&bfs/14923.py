import sys; input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
hy, hx = map(int, input().split())
ey, ex = map(int, input().split())
ey, ex = ey-1, ex-1
graph = [tuple(map(int, input().split())) for _ in range(n)]
visited = [[[-1]*m for _ in range(n)] for _ in range(2)]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(node):
    y, x = node
    dq = deque()
    dq.append((0,)+node)
    visited[0][y][x] = 0
    while dq:
        z, y, x = dq.popleft()
        for k in range(4):
            b, a = y+dy[k], x+dx[k]
            if 0<=b<n and 0<=a<m:
                if graph[b][a]==0 and visited[z][b][a]==-1:
                    visited[z][b][a] = visited[z][y][x] + 1
                    dq.append((z, b, a))
                elif graph[b][a]==1 and z==0 and visited[1][b][a]==-1:
                    visited[1][b][a] = visited[z][y][x] + 1
                    dq.append((1, b, a))

    if visited[0][ey][ex]==visited[1][ey][ex]:
        return visited[0][ey][ex]
    if visited[0][ey][ex] >=0 and visited[1][ey][ex] >= 0:
        return min(visited[0][ey][ex], visited[1][ey][ex])
    return max(visited[0][ey][ex], visited[1][ey][ex])

start = hy-1, hx-1
print(bfs(start))
