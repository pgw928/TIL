import sys; input = sys.stdin.readline
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

mal = {}
position = [[[] for _ in range(n)] for _ in range(n)]
for i in range(1,m+1):
    b, a, d = map(int, input().split())
    position[b-1][a-1].append(i)
    mal[i] = [b-1, a-1, d]


dy, dx = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
rotate = [0, 2, 1, 4, 3]
def move(i,y,x,d):
    b, a = y+dy[d], x+dx[d]
    if 0<=b<n and 0<=a<n and graph[b][a]!=2:
        mal[i] = [b, a, d]
        if graph[b][a]==0:
            position[y][x].reverse()           
            for i in range(len(position[y][x])):
                tmp = position[y][x].pop()
                mal[tmp][0], mal[tmp][1] = b, a
                position[b][a].append(tmp)
        elif graph[b][a]==1:
            for i in range(len(position[y][x])):
                tmp = position[y][x].pop()
                mal[tmp][0], mal[tmp][1] = b, a
                position[b][a].append(tmp)    
    else:
        n_b, n_a = y+dy[rotate[d]], x+dx[rotate[d]]
        if n_b<0 or n_b>=n or n_a<0 or n_a>=n or graph[n_b][n_a]==2:
            mal[i] = [y, x, rotate[d]]
        else:
            mal[i][2] = rotate[d]
            if graph[n_b][n_a]==0:
                position[y][x].reverse()
                for i in range(len(position[y][x])):
                    tmp = position[y][x].pop()
                    mal[tmp][0], mal[tmp][1] = n_b, n_a
                    position[n_b][n_a].append(tmp)

            elif graph[n_b][n_a]==1:      
                for i in range(len(position[y][x])):
                    tmp = position[y][x].pop()
                    mal[tmp][0], mal[tmp][1] = n_b, n_a
                    position[n_b][n_a].append(tmp)

for k in range(1,1001):
    for i in range(1, m+1):
        y, x, d = mal[i]
        if position[y][x][0]==i:
            move(i, y, x, d)
        y, x, d = mal[i]
        if len(position[y][x])>=4:
            print(k)
            sys.exit(0)
print(-1)