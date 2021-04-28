import sys; input = sys.stdin.readline
from copy import deepcopy
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
rotation = [0, 2, 3, 4, 5, 6, 7, 8, 1]
position = {}
direction = {}
graph = [[0]*4 for _ in range(4)]

for i in range(4):
    arr = list(map(int, input().split()))
    for j in range(4):
        x, d = arr[2*j:2*(j+1)]
        if i==0 and j==0:
            shark = (0, 0, d)
            cnt = x
        else:
            graph[i][j] = x
            position[x]= [i, j]
            direction[x] = d

def move(i, s):
    y, x = position[i]
    d = direction[i]
    b, a = y+dy[d], x+dx[d]
    while True:
        if b<0 or b>3 or a<0 or a>3 or (b==s[0] and a==s[1]):
            d = rotation[d]
            b, a = y + dy[d], x + dx[d]
        else:
            direction[i] = d
            if graph[b][a]!=0:
                tmp = graph[b][a]
                position[i][0], position[i][1], position[tmp][0], position[tmp][1] = b, a, y, x  
                graph[b][a], graph[y][x] = graph[y][x], graph[b][a]
            else:
                position[i][0], position[i][1] = b, a  
                graph[b][a], graph[y][x] = graph[y][x], graph[b][a]
            print(f'*****{i}******')
            for g in graph:
                print(g)
            print('***********')    
            return

res = cnt
def dfs(s, cnt):
    print('상어 물고기 먹음')
    for g in graph:
        print(g)
    print('다 먹음')
    print('-----------')
    print(direction)
    global res
    for i in range(1, 17):
        if i in position:
            move(i, s)
    y, x, d = s
    flag = True
    print('물고기 이동')
    print('-----------')
    print('-----------')
    for g in graph:
        print(g)
    print('이동 끝')
    res = max(res, cnt)
    for k in range(1, 4):
        b, a = y+k*dy[d], x+k*dx[d]    
        if 0<=b<4 and 0<=a<4:
            if graph[b][a]!=0:
                tmp, graph[b][a] = graph[b][a], 0
                del position[tmp]
                dfs((b, a, direction[tmp]), cnt + tmp)
                graph[b][a] = tmp
                position[tmp] = [b, a]
                flag = False
        else:
            break
    if flag:
        res = max(res, cnt)

dfs(shark, cnt)
print(res)

