import sys
from collections import deque
from math import inf
input = sys.stdin.readline

M, N = map(int, input().split())

graph = [list(input()) for _ in range(N)]
nodes = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'C':
            nodes.append((i,j))

start = (nodes[0][0], nodes[0][1], 4)
end_node = nodes[1]

check = [[inf]*M for _ in range(N)]
count = [[[0,0,0,0] for _ in range(M)] for _ in range(N)]
print(count)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
rever = {0:1, 1:0, 2:3, 3:2}
def bfs(start, end_node):
    flag = True

    dq = deque()
    dq.append(start)
    check[start[0]][start[1]] = 0
    while dq:
        y, x, s = dq.popleft()
        for k in range(4):
            b , a = y + dy[k] , x + dx[k]
            if (y == 10) and (x == 8):
                print(y, x, s, '--->', b, a, k, 'count :', count[y][x][k])
            if (0<=b<=N-1) and (0<=a<=M-1) and (check[y][x] <= check[b][a]) and (graph[b][a]!='*') and (count[y][x][k]==0):
                if s != k:
                    check[b][a] = min(check[y][x]+1, check[b][a])
                    # count[y][x][k] = 1
                    count[b][a][rever[k]] = 1
                else:
                    if (y== 10) and (x==8) and k==1:
                        print('여기:',check[b][a], check[y][x])
                    check[b][a] = min(check[y][x], check[b][a])
                    # count[y][x][k] = 1
                    count[b][a][rever[k]] = 1
                dq.append((b, a, k))
            if count[10][8][1]== 1 and flag:
                print('ㅅㅂ 여기다')
                flag = False
            if (y == 10) and (x == 8):
                print(y, x, s, '--->', b, a, k, 'check :', check[y][x], '--->', check[b][a])
    return check[end_node[0]][end_node[1]]-1


print(bfs(start, end_node))
for a in check:
    print(a)
print(count)