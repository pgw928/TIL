import sys
sys.stdin = open('section7/input.txt', 'rt')
n = int(input())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def dfs(node):
    global cnt
    y, x = node 
    for k in range(4):
        b, a = y+dy[k], x+dx[k]
        if 0<=b<n and 0<=a<n and graph[b][a]==1:
            graph[b][a] = 0
            dfs((b, a))
            cnt += 1

res = []
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            cnt = 1
            graph[i][j] = 0
            dfs((i, j))
            res.append(cnt)

print(len(res))
for r in sorted(res):
    print(r)    