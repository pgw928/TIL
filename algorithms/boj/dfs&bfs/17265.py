import sys; input = sys.stdin.readline
from collections import deque
n = int(input())
graph = [input().strip().split() for _ in range(n)]
visited_max = [[-float('inf')]*n for _ in range(n)]
visited_min = [[float('inf')]*n for _ in range(n)]
dy, dx = [1, 0], [0, 1]
def bfs(start=(0, 0)):
    dq = deque()
    dq.append(start + (graph[start[0]][start[1]],))
    visited_max[start[0]][start[1]] = int(graph[start[0]][start[1]])
    visited_min[start[0]][start[1]] = int(graph[start[0]][start[1]])
    while dq:
        y, x, s = dq.popleft()
        for k in range(2):
            b, a = dy[k]+y, dx[k]+x
            if 0<=b<n and 0<=a<n:
                if graph[b][a].isnumeric():
                    n_s = eval(s + graph[b][a])
                    if visited_max[b][a] < n_s:
                        dq.append((b,a, f'{n_s}'))
                        visited_max[b][a] = n_s
                    if visited_min[b][a] > n_s:
                        dq.append((b, a, f'{n_s}'))
                        visited_min[b][a] = n_s
                else:
                    if visited_max[b][a] < int(s):
                        dq.append((b,a, s+graph[b][a]))
                        visited_max[b][a] = int(s)
                    if visited_min[b][a] > int(s):
                        dq.append((b, a, s+graph[b][a]))
                        visited_min[b][a] = int(s)
    return visited_max[n-1][n-1], visited_min[n-1][n-1]


result = bfs()
print(result[0], result[1])
