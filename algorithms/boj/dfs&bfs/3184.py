import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
check = [[True]*m for _ in range(n)]

dy, dx = [1, -1, 0, 0], [0, 0, -1, 1]
def bfs(start):

    dq = deque()
    dq.append(start)
    check[start[0]][start[1]] =False
    sheep, wolf = 0, 0
    if graph[start[0]][start[1]]=='v':
        wolf += 1
    elif graph[start[0]][start[1]] == 'o':
        sheep += 1
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            b, a = dy[i]+y, dx[i]+x
            if 0<=b<=n-1 and 0<=a<=m-1 and graph[b][a]!='#' and check[b][a]==True:
                if graph[b][a]=='o':
                    sheep += 1
                elif graph[b][a]=='v':
                    wolf += 1
                check[b][a] = False
                dq.append((b,a))
    if sheep==0 or wolf==0:
        return sheep, wolf
    if sheep>wolf:
        return sheep, 0
    if sheep<=wolf:
        return 0, wolf


o, v = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j]!='#' and check[i][j]==True:
            s, w = bfs((i,j))
            o += s
            v += w
print(o, v)

