import sys; input = sys.stdin.readline
from collections import deque
m, n = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

s2e = []
for i in range(n):
    for j in range(m):
        if graph[i][j]=='C':
            s2e.append((i, j))

# 북 남 서 동
dy, dx = [-1, 1, 0, 0], [0 ,0, -1, 1]
visited = [[-1]*m for _ in range(n)]
def bfs(node):
    y, x = node
    dq = deque()
    dq.append(node + (0, 0))
    dq.append(node + (0, 1))
    dq.append(node + (0, 2))
    dq.append(node + (0, 3))
    visited[y][x] = 0
    result = []
    while dq:
        print(dq)
        y, x, c, f = dq.popleft()
        if graph[y][x]=='C':
            result.append(c)
            continue
        b, a = dy[f] + y, dx[f] + x
        if 0 <= b < n and 0 <= a < m and visited[b][a] >= c+1 and (graph[b][a] == '.' or graph[b][a]=='C'):
            dq.append((b, a, c, f))
            if f == 0:
                dq.append((b, a, c+1, 2))
                dq.append((b, a, c+1, 3))
            elif f == 1:
                dq.append((b, a, c+1, 2))
                dq.append((b, a, c+1, 3))
            elif f == 2:
                dq.append((b, a, c+1, 0))
                dq.append((b, a, c+1, 1))
            elif f == 3:
                dq.append((b, a, c+1, 0))
                dq.append((b, a, c+1, 1))
            if graph[b][a]!='C':
                visited[b][a] = c+1
    return result
start = s2e[0]
end = s2e[1]
graph[start[0]][start[1]]='.'
print(bfs(start))

