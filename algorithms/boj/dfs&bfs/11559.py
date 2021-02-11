import sys
from collections import deque

graph = [list(sys.stdin.readline().strip()) for _ in range(12)]

def drop(graph):
    for i in range(6):
        k = 11
        for j in range(11,-1,-1):
            if graph[j][i]!='.':
                if k!=j:
                    graph[k][i] = graph[j][i]
                    graph[j][i] = '.'
                k -= 1


dx , dy = [0,0,1,-1], [1,-1,0,0]
def bfs(start):

    dq, check = deque(), set()
    dq.append(start)

    y, x, c = start
    check.add((y,x))
    while dq:
        y, x, c = dq.popleft()

        for k in range(4):
            b, a = y+dy[k], x+dx[k]
            if (0<=b<=11) and (0<=a<=5) and (graph[b][a]==c) and ((b,a) not in check):
                check.add((b,a))
                dq.append((b,a,c))

    if len(check) > 3:
        for (y,x) in check:
            graph[y][x]='.'
        return 1
    return 0


count = 0
while True:
    tmp = 0
    for i in range(12):
        for j in range(6):
            if graph[i][j]!='.':
                tmp += bfs((i,j ,graph[i][j]))
    if tmp:
        count += 1
    else:
        print(count)
        break
    drop(graph)