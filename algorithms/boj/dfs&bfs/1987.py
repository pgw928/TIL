import sys; input = sys.stdin.readline
sys.setrecursionlimit(8000)
n, m = map(int, input().split())

graph = [tuple(input().strip()) for _ in range(n)]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
M = 0
def dfs(start):
    global M
    y, x = start
    flag = True
    for k in range(4):
        b, a = y+dy[k], x+dx[k]
        if 0<=b<n and 0<=a<m:
            idx = ord(graph[b][a]) - ord('A')
            if check[idx]==0:
                check[idx] = check[ord(graph[y][x])-ord('A')] + 1
                dfs((b,a))
                check[idx] = 0
                flag = False
    if flag:
        M = max(M, check[ord(graph[y][x])-ord('A')])

check = [0]*26
check[ord(graph[0][0])-ord('A')] = 1
dfs((0,0))

print(M)