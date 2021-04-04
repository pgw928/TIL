import sys; input = sys.stdin.readline
from collections import deque
a, b, c = map(int, input().split())
total = a+b+c
visited = [[1]*1501 for _ in range(1501)]
def bfs(a, b, c):
    dq  = deque()
    dq.append((a,b,c))

    while dq:
        x, y, z = dq.popleft()
        if x==y and y==z:
            return 1
        if x<y and visited[x][y]:
            visited[x][y] = 0
            dq.append((2*x, y-x, z))
        elif y<x and visited[y][x]:
            visited[y][x] = 0
            dq.append((x-y, 2*y, z))

        if y<z and visited[y][z]:
            visited[y][z] = 0
            dq.append((x, 2*y, z-y))
        elif z<y and visited[z][y]:
            visited[z][y] = 0
            dq.append((x, y-z, 2*z))

        if x<z and visited[x][z]:
            visited[x][z] = 0
            dq.append((2*x, y, z-x))
        elif z<x and visited[z][x]:
            visited[z][x] = 0
            dq.append((x-z, y, 2*z))
    return 0

if total%3!=0:
    print(0)
else:
    print(bfs(a, b, c))