import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [tuple(input().strip()) for _ in range(n)]

temp = [(i,j) for i in range(n) for j in range(m) if graph[i][j]=='L']

dy, dx = [1, -1 ,0 ,0], [0, 0, -1, 1]
visited = [ [[-1, -1] for _ in range(m)] for _ in range(n)]
print(visited)
def bfs(start):
    dq = deque()
    dq.append((start[0], start[1], 0))
    visited[start[0]][start[1]][0] = 1
    while dq:
        y, x, s = dq.popleft()
        M = max(s, M)
        for k in range(4):
            b, a = y+dy[k], x+dx[k]
            if 0<=b<=n-1 and 0<=a<=m-1 and graph[b][a]=='L':
                if (b,a) not in visited:
                dq.append((b,a,s+1))
                visited.add((b,a))
    return M

M = 0
for i, j in temp:
    M = max(bfs((i,j)), M)
print(M)