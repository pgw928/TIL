import sys; input = sys.stdin.readline
graph = [tuple(map(int, input().split())) for _ in range(5)]

check = []
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def dfs(start, depth ,num):
    if depth==6:
        if num not in check:
            check.append(num)

        if int(str(num)[::-1]) not in check:
            check.append(int(str(num)[::-1]))
        return
    y, x = start
    for k in range(4):
        b, a = y+dy[k], x+dx[k]
        if 0<=b<5 and 0<=a<5 and depth < 6:
            dfs((b, a), depth+1, num+(graph[b][a])*10**depth)


for i in range(5):
    for j in range(5):
        dfs((i, j), 1 ,graph[i][j])
print(len(check))
