import sys; input=sys.stdin.readline
from collections import deque
n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
def air_bfs(start):
    dq = deque()
    dq.append(start)
    check = [[0]*m for _ in range(n)]
    check[start[0]][start[1]] = 1
    while dq:
        y, x = dq.popleft()
        for k in range(4):
            b, a = dy[k]+y, dx[k]+x
            if 0<=b<n and 0<=a<m and check[b][a]==0:
                if graph[b][a]==0:
                    graph[b][a] = -1
                    dq.append((b, a))
                    check[b][a] = 1
                elif graph[b][a]==-1:
                    dq.append((b, a))
                    check[b][a] = 1
air_bfs((0,0))

def bfs(start):
    dq = deque()
    dq.append(start)

    while dq:
        y, x = dq.popleft()
        if visited[y][x] != 0:
            continue
        count = 0
        for k in range(4):
            b, a = dy[k] + y, dx[k] + x
            if 0<=b<n and 0<=a<m:
                if graph[b][a] == -1:
                    count += 1
                elif graph[b][a] == 1 and visited[b][a]==0:
                    dq.append((b, a))
        if count >= 2:
            visited[y][x] = count
        else:
            visited[y][x] = -1
        nodes.remove((y, x))


count = 0
while True:
    air_bfs((0,0))
    nodes = [(i, j) for i in range(n) for j in range(m) if graph[i][j]==1]
    visited = [[0] * m for _ in range(n)]
    if not nodes:
        break
    while nodes:
        bfs(nodes[0])
    for i in range(n):
        for j in range(m):
            if visited[i][j]>=2:
                graph[i][j] = -1
    count += 1
print(count)