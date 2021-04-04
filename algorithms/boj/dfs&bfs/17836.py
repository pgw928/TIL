import sys; input = sys.stdin.readline
from collections import deque
n, m, t = map(int, input().split())
graph = [tuple(map(int, input().split())) for _ in range(n)]
visited = [[[-1]*m for _ in range(n)] for _ in range(2)]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(s):
    dq = deque()
    dq.append(s+(0,))
    visited[0][s[0]][s[1]] = 0
    while dq:
        z, y, x = dq.popleft()
        if (y, x) == (n - 1, m - 1) and visited[z][y][x] <= t:
            return visited[z][y][x]
        for k in range(4):
            b, a = dy[k]+y, dx[k]+x
            if 0<=b<n and 0<=a<m:
                if graph[b][a]==0 and visited[z][b][a]==-1:
                    dq.append((z,b, a))
                    visited[z][b][a] = visited[z][y][x] + 1

                elif graph[b][a]==2 and z==0 and visited[z+1][b][a]==-1:
                    dq.append((z+1, b, a))
                    visited[z+1][b][a] = visited[z][y][x] + 1

                elif graph[b][a]==1 and z and visited[z][b][a]==-1:
                    dq.append((z, b, a))
                    visited[z][b][a] = visited[z][y][x] + 1

    return 'Fail'
print(bfs((0, 0)))