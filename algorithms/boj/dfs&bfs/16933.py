import sys; input = sys.stdin.readline
from collections import deque
n, m, k = map(int, input().split())
graph = [input().strip() for _ in range(n)]
visited_pm = [[[float('inf')]*m for _ in range(n)] for _ in range(k+1)]
visited_am = [[[float('inf')]*m for _ in range(n)] for _ in range(k+1)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(start=(0, 0)):
    dq = deque()
    dq.append((0,) + start+ (0,))
    visited_am[0][start[0]][start[1]] = 1
    while dq:
        print(dq)
        z, y, x, c = dq.popleft()
        for j in range(4):
            b, a = dy[j]+y , dx[j]+x
            if 0<=b<n and 0<=a<m:
                if graph[b][a]=='0':
                    if c==1 and visited_pm[z][y][x]+1 < visited_am[z][b][a]:
                        dq.append((z, b, a, 0))
                        visited_am[z][b][a] = visited_pm[z][y][x] + 1

                    elif c==0 and visited_am[z][y][x]+1 < visited_pm[z][b][a]:
                        dq.append((z, b, a, 1))
                        visited_pm[z][b][a] = visited_am[z][y][x] + 1

                elif graph[b][a]=='1' and z<k:
                    if c==0 and visited_am[z][y][x]+1 < visited_pm[z+1][b][a]:
                        visited_pm[z+1][b][a] = visited_am[z][y][x] + 1
                        dq.append((z+1, b, a, 1))
                    elif c==1 and visited_pm[z][y][x]+2 < visited_pm[z+1][b][a]:
                        visited_pm[z+1][b][a] = visited_pm[z][y][x] + 2
                        dq.append(((z+1, b, a, 1)))
bfs()
result = set()
print(visited_am)
print(visited_pm)
for v in visited_am:
    result.add(v[-1][-1])
for v in visited_pm:
    result.add(v[-1][-1])

result = result - {float('inf')}

print(min(result) if result else -1)