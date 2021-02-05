import sys

input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
check = [[0]*n for _ in range(n)]
# 4
# 14 9 12 10
# 1 11 5 4
# 7 15 2 13
# 6 3 16 8

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(start):

    y, x = start
    flag = True
    result = set()
    for k in range(4):
        b, a = y+dy[k], x+dx[k]
        if (0<=b<=n-1) and (0<=a<=n-1):
            if graph[y][x] < graph[b][a]:
                check[b][a] = max(check[y][x] + 1, check[b][a])
                result.add(dfs((b,a)))
                flag = False
    if flag:
        return check[y][x]
    print(y,x,result)
    return max(result)

m = 0
for i in range(n):
    for j in range(n):
        check[i][j] = max(check[i][j], 1)
        m = max(dfs((i,j)),m)

print(m)



