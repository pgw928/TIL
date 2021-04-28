import sys
sys.stdin = open('section7/input.txt', 'rt')
graph = [list(map(int, input().split())) for _ in range(10)]

for j in range(10):
    if graph[-1][j]==2:
        start = (9, j)
        break


dy, dx = [0, 0, -1], [1, -1, 0]
def dfs(node=start):
    y, x = node
    if y==0:
        print(x)
        sys.exit(0)
    for k in range(3):
        b, a = y+dy[k], x+dx[k]
        if 0<=b<10 and 0<=a<10 and graph[b][a]==1:
            graph[b][a] = 0
            dfs((b, a))
dfs()