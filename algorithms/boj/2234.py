import sys; input = sys.stdin.readline
from collections import deque
m, n = map(int, input().split())
graph = [tuple(map(int, input().split())) for _ in range(n)]
visited = [[[0]*m for _ in range(n)] for _ in range(2)]

dy, dx = [0, 0, 1, -1], [-1, 1, 0, 0]
def bfs(node):
    y, x = node
    dq = deque()
    dq.append((0,)+node)
    visited[0][y][x] = 1
    while dq:
        z, y, x = dq.popleft()
        tmp = int(bin(graph[y][x])[2:])
        flag = {0:0, 1:0, 2:0, 3:0}
        for idx, k in enumerate([10, 100, 1000, 10000]):
            if tmp%k!=0:
                flag[idx] = 1
            tmp -= tmp%k
        for k in range(4):
            b, a = y+dy[k], x+dx[k]
            if 0<=b<n and 0<=a<m:
                if flag[k]==0 and visited[z][b][a]==0:
                    visited[z][b][a] = visited[z][y][x] + 1
                    dq.append((z, b, a))
                elif flag[k]==1 and z==0 and visited[1][b][a]==0:
                    visited[1][b][a] = visited[z][y][x] + 1
                    dq.append((1, b, a))
        for k in range(2):
            for v in visited[k]:
                print(v)
            print('---------')

for i in range(n):
    for j in range(m):
        if visited[0][i][j]==0:
            bfs((i, j))
for k in range(2):
    for v in visited[k]:
        print(v)
    print('---------')
