import sys; input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
position = [[0, 0] for _ in range(m)]
direction =[0]*m
location = [[[] for _ in range(n)] for _ in range(n)]

for i in range(m):
    y, x, d = map(int, input().split())
    y, x, d = y-1 ,x-1 ,d-1
    direction[i] = d  
    position[i][0], position[i][1] = y, x
    location[y][x].append(i)

dy, dx = [0,0,-1,1], [1,-1,0,0]
rotation = [1, 0, 3, 2]
def move(i):
    y, x = position[i]
    d = direction[i]
    b, a = y+dy[d], x+dx[d]
    stack = []
    if b<0 or b>=n or a<0 or a>=n or graph[b][a]==2:
        n_b, n_a = y + dy[rotation[d]], x + dx[rotation[d]]
        direction[i] = rotation[d]
        if n_b<0 or n_b>=n or n_a<0 or n_a>=n or graph[n_b][n_a]==2:
            return
        if graph[n_b][n_a]==0:
            for j in range(len(location[y][x])):
                if i == location[y][x][j]:
                    l = len(location[y][x][j:])
                    while l:
                        tmp = location[y][x].pop()
                        stack.append(tmp)
                        position[tmp][0], position[tmp][1] = n_b, n_a
                        l -= 1
                    break
            while stack:
                location[n_b][n_a].append(stack.pop())
        elif graph[n_b][n_a]==1:
            for j in range(len(location[y][x])):
                if i == location[y][x][j]:
                    l = len(location[y][x][j:])
                    while l:
                        tmp = location[y][x].pop()
                        stack.append(tmp)
                        position[tmp][0], position[tmp][1] = n_b, n_a
                        l -= 1
                    break
            stack.reverse()
            while stack:
                location[n_b][n_a].append(stack.pop())
    else:
        if graph[b][a]==0:
            for j in range(len(location[y][x])):
                if i == location[y][x][j]:
                    l = len(location[y][x][j:])
                    while l:
                        tmp = location[y][x].pop()
                        stack.append(tmp)
                        position[tmp][0], position[tmp][1] = b, a
                        l -= 1
                    break
            while stack:
                location[b][a].append(stack.pop())
        elif graph[b][a]==1:
            for j in range(len(location[y][x])):
                if i == location[y][x][j]:
                    l = len(location[y][x][j:])
                    while l:
                        tmp = location[y][x].pop()
                        stack.append(tmp)
                        position[tmp][0], position[tmp][1] = b, a
                        l -= 1
                    break
            stack.reverse()
            while stack:
                location[b][a].append(stack.pop())


for k in range(1, 1001):
    for i in range(m):
        move(i)
        y, x = position[i]
        if len(location[y][x])==4:
            print(k)
            sys.exit(0)
print(-1)