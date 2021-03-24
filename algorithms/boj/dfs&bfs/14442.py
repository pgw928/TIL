import sys; input = sys.stdin.readline
from collections import deque
n, m, k = map(int, input().split())
graph = [input().strip() for _ in range(n)]
visited = [[[0]*m for _ in range(n)] for _ in range(k+1)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(start=(0, 0)):
    dq = deque()
    dq.append((0,) + start)
    visited[0][start[0]][start[1]] = 1
    while dq:
        z, y, x = dq.popleft()
        for j in range(4):
            b, a = dy[j]+y , dx[j]+x
            if 0<=b<n and 0<=a<m:
                if graph[b][a]=='0' and visited[z][b][a]==0:
                    visited[z][b][a] = visited[z][y][x] + 1
                    dq.append((z, b, a))
                elif graph[b][a]=='1' and z<k and visited[z+1][b][a]==0:
                    visited[z+1][b][a] = visited[z][y][x] + 1
                    dq.append((z+1, b, a))
bfs()
result = set()
for v in visited:
    result.add(v[-1][-1])

result = result - {0}
print(min(result) if result else -1)