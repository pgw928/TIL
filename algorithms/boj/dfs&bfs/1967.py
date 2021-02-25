import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

# n이 1일때 예외처리
if n==1:
    print(0)
    exit()

# tree 받아오기 및 자식노드 2개 이상인거 candi에 저장
graph = {i:[] for i in range(1,n+1)}
candi = set()
for _ in range(n-1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    candi.add(a)

# root 노드의 자식노드가 한개이면 임시로 한개 더 만든다.
if len(graph[1])==1:
    graph[1].append((n+2,0))
    graph[n+2]=[]

def bfs(start):
    dq = deque()
    dq.append(start)
    while dq:
        node, c = dq.popleft()
        if not graph[node]:
            result[start[0]] = max(c, result[start[0]])
        else:
            for n_n, w in graph[node]:
                dq.append((n_n, c+w))

# result : 자식노드들의 하위 weight들의 합의 maximum 값
# diameter : 가능한 지름들의 집합
diameter = set()
for i in candi:
    result = {a:0 for a, b in graph[i]}
    if len(result)<=1:
        continue
    for a,b in graph[i]:
        bfs((a, b))
    diameter.add(sum(sorted(list(result.values()))[-2:]))
print(max(diameter))
