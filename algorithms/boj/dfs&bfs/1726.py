import sys; input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(n)]
visited = [[[-1]*m for _ in range(n)] for _ in range(4)]
start, end = list(map(int, input().split())), list(map(int, input().split()))
start, end = (start[0]-1 ,start[1]-1 ,start[2]-1) , (end[0]-1, end[1]-1, end[2]-1)

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
def bfs(start):
    y, x, z = start
    dq = deque()
    dq.append(start)
    visited[z][y][x] = 0
    while dq:
        y, x, z = dq.popleft()
        if (y, x, z) == end:
            return visited[z][y][x]
        for k in range(1, 4):
            b, a = k*dy[z]+y, k*dx[z]+x
            if 0<=b<n and 0<=a<m and visited[z][b][a]==-1 and graph[b][a]==0:
                visited[z][b][a] = visited[z][y][x] + 1
                dq.append((b, a, z))
            elif 0<=b<n and 0<=a<m and graph[b][a]==1:
                break

        if z==1:
            if visited[2][y][x]==-1:
                visited[2][y][x]= visited[z][y][x] + 1
                dq.append((y, x, 2))
            if visited[3][y][x]==-1:
                visited[3][y][x] = visited[z][y][x] + 1
                dq.append((y, x, 3))
            if visited[0][y][x]==-1:
                visited[0][y][x] = visited[z][y][x] + 2
                dq.append((y, x, 0))

        elif z==2:
            if visited[0][y][x]==-1:
                visited[0][y][x]= visited[z][y][x] + 1
                dq.append((y, x, 0))
            if visited[1][y][x]==-1:
                visited[1][y][x] = visited[z][y][x] + 1
                dq.append((y, x, 1))
            if visited[3][y][x]==-1:
                visited[3][y][x] = visited[z][y][x] + 2
                dq.append((y, x, 3))
        elif z==0:
            if visited[2][y][x]==-1:
                visited[2][y][x]= visited[0][y][x] + 1
                dq.append((y, x, 2))
            if visited[3][y][x]==-1:
                visited[3][y][x] = visited[0][y][x] + 1
                dq.append((y, x, 3))
            if visited[1][y][x]==-1:
                visited[1][y][x] = visited[z][y][x] + 2
                dq.append((y, x, 1))
        elif z==3:
            if visited[0][y][x]==-1:
                visited[0][y][x]= visited[3][y][x] + 1
                dq.append((y, x, 0))
            if visited[1][y][x]==-1:
                visited[1][y][x] = visited[3][y][x] + 1
                dq.append((y, x, 1))
            if visited[2][y][x]==-1:
                visited[2][y][x] = visited[z][y][x] + 2
                dq.append((y, x, 2))

print(bfs(start))