import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m, k = map(int, input().split())
trash = {tuple(map(int, input().split())) for _ in range(k)}

dy, dx = [-1, 1, 0, 0], [0, 0, 1, -1]
check = [[False]*(m+1) for _ in range(n+1)]
def dfs(start):
    y, x = start
    global count
    count += 1
    for i in range(4):
        b, a = y+dy[i], x+dx[i]
        if 1<=b<=n and 1<=a<=m and (b, a) in trash and check[b][a]==False:
            check[b][a] = True
            dfs((b,a))

result = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if (i,j) in trash and check[i][j]==False:
            count = 0
            check[i][j]=True
            dfs((i,j))
            result = max(count, result)
print(result)