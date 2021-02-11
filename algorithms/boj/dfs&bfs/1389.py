import sys
from collections import deque
input =sys.stdin.readline
n, m = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    dq, check = deque() ,[-1]*(n+1)
    check[0] = 0
    dq.append(start)
    check[start] = 0
    while dq:
        node = dq.popleft()
        for n_n in graph[node]:
            if check[n_n]==-1:
                check[n_n] = check[node]+1
                dq.append(n_n)

    return sum(check)

result = []
for i in range(1,n+1):
    result.append((i, bfs(i)))

result.sort(key=lambda x: x[1])
print(result[0][0])