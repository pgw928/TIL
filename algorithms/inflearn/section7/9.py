import sys
from collections import deque
sys.stdin = open('section7/input.txt', 'rt')
graph = [list(map(int, input().split())) for _ in range(7)]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(node=(0, 0)):
    dq = deque()
    dq.append(node)
    graph[0][0] = -1
    while dq:
        y, x = dq.popleft()
        if (y,x)==(6, 6):
            return -graph[y][x]-1
        for k in range(4):
            b, a = dy[k]+y, dx[k]+x
            if 0<=b<7 and 0<=a<7 and graph[b][a]==0:
                graph[b][a] = graph[y][x] -1
                dq.append((b,a))
    return -1
print(bfs())    