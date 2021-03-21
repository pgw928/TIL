import sys; input = sys.stdin.readline
from collections import deque
m, n = map(int, input().split())
graph = [input().strip() for _ in range(n)]
visited = [[10_000]*m for _ in range(n)]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(start=(0, 0), end=(n-1, m-1)):
    dq = deque()
    dq.append(start+(0,))
    visited[start[0]][start[1]] = 0
    M = 10_000
    while dq:
        y, x, c = dq.popleft()
        if (y,x) == end:
            M = min(M, c)
        for k in range(4):
            b, a = y+dy[k], x+dx[k]
            if 0<=b<n and 0<=a<m:
                if graph[b][a]=='1' and c+1<visited[b][a]:
                    dq.append((b, a, c+1))
                    visited[b][a] = c+1
                elif graph[b][a]=='0' and c<visited[b][a]:
                    dq.append((b, a, c))
                    visited[b][a] = c
    return M

print(bfs())
