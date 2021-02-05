import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

break_point = False
for i in range(N):
    for j in range(N):
        if graph[i][j]==9:
            graph[i][j]=0
            start = (i, j)
            break_point = True
            break
    if break_point:
        break


dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]
def bfs(start, size, count, result):

    dq = deque()
    dq.append((start[0], start[1], size, count, result))
    check[start[0]][start[1]] = 1
    temp = []
    while dq:
        b, a, s, c, r = dq.popleft()
        for k in range(4):
            y, x = dy[k]+b, dx[k]+a
            if 0<=x<=N-1 and 0<=y<=N-1 and check[y][x]==0:
                if graph[y][x] == 0 or graph[y][x] == s:
                    check[y][x] = 1
                    dq.append((y, x, s, c, r+1))
                elif (graph[y][x] < s):
                    if c+1 == s:
                        check[y][x] = 1
                        temp.append( ((y,x), s+1, 0, r+1))
                    else:
                        check[y][x] = 1
                        temp.append(((y,x), s, c+1, r + 1))
    if temp:
        temp.sort(key=lambda z: (z[3], z[0][0],z[0][1] ))
        graph[temp[0][0][0]][temp[0][0][1]] = 0
        return temp[0]
    return False


size = 2
result = 0
count = 0
while True:
    check = [[0]*N for _ in range(N)]
    tmp = bfs(start, size, count, result)
    if not tmp:
        break
    start, size, count, result = tmp
print(result)