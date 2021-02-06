import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
check = [[-1]*n for _ in range(n)]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def dfs(start):
    y, x = start
    if check[y][x] == -1:
        check[y][x] = 0
        for k in range(4):
            b, a = y+dy[k], x+dx[k]
            if (0<=b<=n-1) and (0<=a<=n-1):
                if graph[y][x] < graph[b][a]:
                    check[y][x] = max(dfs((b,a)), check[y][x])
        check[y][x] += 1
    return check[y][x]

m = 0
for i in range(n):
    for j in range(n):
        m = max(dfs((i,j)),m)
print(m)
