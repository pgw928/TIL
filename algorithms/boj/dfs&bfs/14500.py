import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [ list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0, 1, 1, -1, -1]
dx = [0, 0, -1, 1, 1, -1, 1, -1]

def distance(A, check):
    m = math.inf
    for (y,x) in check:
        m = min(abs(A[0]-y) + abs(A[1]-x), m)
    if m==1:
        return True


def dfs(start_node, depth , current):

    y, x = start_node
    check.append((y, x))
    current += graph[y][x]

    if depth == 3:
        return current

    if depth == 2 :
        f = 8
    else:
        f= 4

    temp = []
    for k in range(f):
        b, a = y+dy[k], x+dx[k]
        if 0<=b<N and 0<=a<M:
            temp.append((b,a))

    temp.sort(key=lambda c: graph[c[0]][c[1]], reverse=True)
    for b,a in temp:
        if ((b,a) not in check) and distance((b,a) ,check):
            yy = b
            xx = a
            break
    current =  dfs((yy, xx), depth+1, current)
    return current

MA = 0
for i in range(N):
    for j in range(M):
        check = []
        MA = max(MA, dfs((i, j), 0,0))
print(MA)