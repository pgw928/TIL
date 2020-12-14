import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

M, N = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

c = [[-1]*N for _ in range(M)]

def dfs(start_node=(0, 0), end_node=(M-1, N-1)):
    x, y = start_node

    if start_node == end_node:
        return 1
    if c[x][y] != -1:
        return c[x][y]
    c[x][y] = 0

    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        
        if a <= -1 or b <= -1 or a >= M or b >= N:
            continue
        if graph[a][b] < graph[x][y]:
            c[x][y] += dfs((a, b))
    return c[x][y]

print(dfs())

# import sys
# input = sys.stdin.readline
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# def dfs(x, y):
#     if x == m-1 and y == n-1:
#         return 1
#     if c[x][y] != -1:
#         return c[x][y]
#     c[x][y] = 0
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < m and 0 <= ny < n:
#             if a[nx][ny] < a[x][y]:
#                 c[x][y] += dfs(nx, ny)
#     return c[x][y]
# m, n = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(m)]
# c = [[-1]*n for _ in range(m)]
# print(dfs(0, 0))
