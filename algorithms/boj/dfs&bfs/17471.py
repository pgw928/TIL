import sys; input = sys.stdin.readline
from collections import deque
from itertools import combinations
n = int(input())
people = (0,) + tuple(map(int, input().split()))
graph = {i:[] for i in range(1, n+1)}
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    if tmp[0]!=0:
        graph[i].extend(tmp[1:])

def bfs(start, S):
    dq, check = deque(), set()
    dq.append(start)
    check.add(start)
    while dq:
        x = dq.popleft()
        for y in graph[x]:
            if (y in S) and (y not in check):
                check.add(y)
                dq.append(y)
    if len(check)==len(S):
        return True
    return False

def sum_subset(S):
    s = 0
    for i in S:
        s += people[i]
    return s

res = float('inf')
for k in range(1, n//2+1):
    combs = combinations(range(1,n+1), k)
    for A in combs:
        B = {i for i in range(1,n+1)} - set(A)
        if bfs(A[0],A) and bfs(list(B)[0],B):
            res = min(abs(sum_subset(A)-sum_subset(B)), res)

print(-1 if res==float('inf') else res)

