import sys; input = sys.stdin.readline
n = int(input())
graph = [[0]*101 for _ in range(101)]


dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
def make_dragon(x, y, d, g):
    tmp = [(x,y)]
    graph[y][x] = 1
    cnt = -1
    while cnt!=g:
        if cnt==-1:
            x += dx[d]
            y += dy[d]
            cnt += 1
            tmp.append((x,y))
            graph[y][x] = 1
        else:
            for i, j in tmp[:-1][::-1]:
                tmp.append((x+y-j, -x+y+i))
                graph[-x+y+i][x+y-j] = 1
            cnt += 1
            x, y = tmp[-1]
    
for _ in range(n):
    x, y, d, g = list(map(int, input().split()))
    make_dragon(x,y,d,g)

cnt = 0
for i in range(100):
    for j in range(100):
        if graph[i][j]==1 and graph[i+1][j]==1 and graph[i][j+1]==1 and graph[i+1][j+1]==1:
            cnt += 1
print(cnt)