import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(h)]
check = [[[0]*(k+1) for _ in range(w)] for _ in range(h)]

dy1 = [1, 1, -1, -1, 2, 2, -2, -2]
dx1 =  [2, -2, 2, -2, 1, -1, 1, -1]
dy2, dx2 = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(start = (0,0,0,0), end=(h-1,w-1)):
    dq = deque()
    dq.append(start)
    check[start[0]][start[1]]= [1]*(k+1)
    while dq:
        y, x, s, result = dq.popleft()
        if (y,x)==end:
            return result
        if s<k:
            for i in range(8):
                b, a = y+dy1[i], x+dx1[i]
                if (0<=b<=h-1) and (0<=a<=w-1) and (check[b][a][s+1]==0) and (graph[b][a]==0):
                    dq.append((b, a, s+1, result+1))
                    check[b][a][s+1] = 1
        for i in range(4):
            b, a = y+dy2[i], x+dx2[i]
            if (0 <= b <= h-1) and (0 <= a <= w-1) and (check[b][a][s]==0) and (graph[b][a]==0):
                dq.append((b, a, s, result+1))
                check[b][a][s] = 1
    return -1

print(bfs())