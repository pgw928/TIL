import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

def bfs(start):
    dq = deque()
    dq.append((start, 1))
    check[start] = 1
    while dq:
        node, color = dq.popleft()
        for n_n in graph[node]:
            if check[n_n] == color:
                return False
            if not check[n_n]:
                dq.append((n_n, -color))
                check[n_n] = -color
    return True

for _ in range(t):
    v, e = map(int, input().split())
    graph = {i:set() for i in range(1,v+1)}
    break_pt = False
    for _ in range(e):
        a, b  = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)
    check = [0]*(v+1)
    for i in  range(1,v):
        if check[i]==0:
            print(i)
            if not bfs(i):
                print('NO')
                break_pt = True
                break
    if break_pt:
        continue
    print('YES')





