import sys

input = sys.stdin.readline

n = int(input())

forest = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*n for _ in range(n)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(i, j):
    if visited[i][j] < 0:
        visited[i][j] = 0
        for d in range(4):
            x, y = i+dx[d], j+dy[d]
            if 0<=x<n and 0<=y<n and forest[i][j] < forest[x][y]:
                visited[i][j] = max(visited[i][j], dfs(x, y))
        visited[i][j] += 1
    return visited[i][j]

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))
print(ans)

