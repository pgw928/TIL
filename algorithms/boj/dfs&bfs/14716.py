import sys
sys.setrecursionlimit(2500*250)

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dy, dx = [1, -1, 0, 0, 1, 1, -1, -1], [0, 0, 1, -1, 1, -1, 1, -1]
def dfs(start):

    y, x = start
    graph[y][x] = 0
    for k in range(8):
        b, a = y+dy[k], x+dx[k]
        if 0<=b<=n-1 and 0<=a<=m-1 and graph[b][a]==1:
            dfs((b,a))



result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            dfs((i, j))
            result += 1
print(result)