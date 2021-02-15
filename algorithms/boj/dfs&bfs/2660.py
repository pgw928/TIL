import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

graph = {i:[] for i in range(1,n+1)}
while True:
    a, b = map(int,input().split())
    if (a, b) == (-1, -1):
        break
    graph[a].append(b)
    graph[b].append(a)

def bfs(st):
    dq, check = deque(), [-1]*(n+1)
    dq.append(st)
    check[st] = 0
    while dq:
        x = dq.popleft()
        for y in graph[x]:
            if check[y]==-1:
                dq.append(y)
                check[y] = check[x] + 1

    return max(check)
result = []
for i in range(1, n+1):
    result.append((i, bfs(i)))

print(result)

result.sort(key=lambda x:(x[1], x[0]))
print(result)
m = result[0][1]

count = 0
candi = []
for a, b in result:
    if b==m:
        count +=1
        candi.append(a)
    else:
        break
print(m, count)
print(' '.join(list(map(str,candi))))