import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [tuple(input().strip()) for _ in range(n)]

dy, dx = [1, -1, 0, 0], [0, 0, -1, 1]


def bfs(start):
    dq, visited = deque(), [[-1] * m for _ in range(n)]
    dq.append(start)
    visited[start[0]][start[1]] = 0
    while dq:
        y, x = dq.popleft()
        for k in range(4):
            b, a = y + dy[k], x + dx[k]
            if 0 <= b <= n - 1 and 0 <= a <= m - 1 and graph[b][a] == 'L' and visited[b][a] == -1:
                dq.append((b, a))
                visited[b][a] = visited[y][x] + 1

    return max([max(g) for g in visited])


M = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]=='L':
            count = 0
            cont_pt = False
            for k in range(4):
                b, a = i+dy[k], j+dx[k]
                if 0<=b<n and 0<=a<m and graph[b][a]=='L':
                    count += 1
                    if  k==2 and count >=2:
                        cont_pt = True
                        break
                    if count>=3:
                        cont_pt = True
                        break
            if cont_pt:
                continue
            M = max(M, bfs((i, j)))
print(M)