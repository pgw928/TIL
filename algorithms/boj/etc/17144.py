import sys; input = sys.stdin.readline
n, m ,t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    if graph[i][0]==-1:
        machine = [(i, 0), (i+1, 0)]
        break

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def solution1(graph):
    n_g = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            count = 0
            if graph[i][j] > 4:
                for k in range(4):
                    y, x = i+dy[k] ,j+dx[k]
                    if 0<=y<n and 0<=x<m and graph[y][x]>-1:
                        n_g[y][x] += graph[i][j]//5
                        count += 1
            n_g[i][j] += graph[i][j] - count * (graph[i][j]//5)
    return n_g

def solution2(n_g):
    top = machine[0]
    tmp = n_g[top[0]][-1]
    n_g[top[0]][1:] = [0] + n_g[top[0]][1:-1]
    for i in range(top[0]-1,0,-1):
        n_g[i][m-1], tmp = tmp, n_g[i][m-1]
    tmp1 = n_g[0][0]
    n_g[0][:] = n_g[0][1:]+[tmp]
    for i in range(1,top[0]):
        n_g[i][0], tmp1 = tmp1, n_g[i][0]

    down = machine[1]
    tmp = n_g[down[0]][-1]
    n_g[down[0]][1:] = [0] + n_g[down[0]][1:-1]
    for i in range(down[0]+1, n-1):
        tmp, n_g[i][m-1] = n_g[i][m-1] , tmp
    tmp1 = n_g[n-1][0]
    n_g[n-1][:] = n_g[n-1][1:]+[tmp]
    for i in range(n-2,down[0],-1):
        n_g[i][0], tmp1  = tmp1, n_g[i][0]
    return n_g

for _ in range(t):
    n_g = solution1(graph)
    graph = solution2(n_g)

score = 0
for g in graph:
    score += sum(g)
print(score+2)