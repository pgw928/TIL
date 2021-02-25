import sys
from collections import deque

#-- input --
input = sys.stdin.readline
n = int(input())
A = tuple(map(int, input().split()))
k = int(input())

# -- tree --
graph = [[] for _ in range(n)]
for idx, a in enumerate(A):
    if a==-1:
        start = idx
    elif a!=-1 and idx!=k:
        graph[a].append(idx)
graph[k] = []
print(graph)
# -- bfs --
count = 0
def bfs(start):
    global count
    dq = deque()
    dq.extend(graph[start])
    while dq:
        node = dq.popleft()
        if not graph[node]:
            count += 1
        else:
            for n_n in graph[node]:
                dq.append(n_n)

# -- result --
bfs(start)
if n==2:
    if k!=0:
        print(1)
else:
    print(count)
