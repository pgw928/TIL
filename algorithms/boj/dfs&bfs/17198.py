import sys; input = sys.stdin.readline
from collections import deque
graph = [list(input().strip()) for _ in range(10)]

for i in range(10):
    for j in range(10):
        if graph[i][j] =='L':
            river = i, j
        elif graph[i][j] =='B':
            barn = i, j
        elif graph[i][j] == 'R':
            rock = i, j
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(river):
    dq = deque()
    dq.append((river[0],river[1],0))
    check = [river]
    while dq:
        y, x, c= dq.popleft()
        if (y, x)== barn:
            return c-1
        for k in range(4):
            b, a = y+dy[k], x+dx[k]
            if 0<=b<10 and 0<=a<10 and (b,a)!=rock and (b,a) not in check:
                dq.append((b,a, c+1))
                check.append((b,a))
print(bfs(river))