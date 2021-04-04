import sys; input = sys.stdin.readline
from collections import deque
m, n = map(int, input().split())
graph = [input().rstrip() for _ in range(n)]
visited = [[1]*m for _ in range(n)]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(s):
    dq = deque()
    dq.append(s)
    cnt = 1
    flag = 'W' if graph[s[0]][s[1]] == 'W' else 'B'
    visited[s[0]][s[1]] = 0
    while dq:
        y, x = dq.popleft()
        for k in range(4):
            b, a = dy[k]+y, dx[k]+x
            if 0<=b<n and 0<=a<m and graph[b][a]==flag and visited[b][a]:
                dq.append((b, a))
                cnt += 1
                visited[b][a] = 0
    return cnt**2

w, b = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j]=='W' and visited[i][j]:
            w += bfs((i, j))
        elif graph[i][j]=='B' and visited[i][j]:
            b += bfs((i, j))
print(w, b)