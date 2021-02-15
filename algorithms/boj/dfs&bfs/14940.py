import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            start = (i, j)
            break


dy, dx = [1, -1, 0, 0], [0, 0, -1, 1]
def bfs(start):
    dq, check = deque(), [[0]*m for _ in range(n)]
    dq.append(start)
    while dq:
        y, x = dq.popleft()
        for k in range(4):
            b, a = y+dy[k], x+dx[k]
            if 0<=b<=n-1 and 0<=a<=m-1 and graph[b][a]==1 and check[b][a]==0:
                check[b][a] = check[y][x] + 1
                graph[b][a] = 0
                dq.append((b,a))
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                check[i][j] = -1
    return check

result = bfs(start)
for r in result:
    print(' '.join(list(map(str,r))))

