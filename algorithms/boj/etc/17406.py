import sys; input = sys.stdin.readline
from copy import deepcopy
from itertools import permutations
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def rot(start, end, s, graph):
    y1, x1 = start
    y2, x2 = end

    for i in range(s):
        tmp1, tmp2 = graph[y1+i][x2-i], graph[y2-i][x1+i]
        graph[y1+i][x1+i+1:x2+1-i] = graph[y1+i][x1+i:x2-i]
        graph[y2-i][x1+i:x2-i] = graph[y2-i][x1+i+1:x2-i+1]
        for j in range(y1+i, y2-i):
            graph[j][x1+i] = graph[j+1][x1+i]
        graph[y2-i-1][x1+i] = tmp2
        for j in range(y2-i,y1+i ,-1):
            graph[j][x2-i] = graph[j-1][x2-i]
        graph[y1+i+1][x2-i] = tmp1

    return graph

operation = []
for _ in range(k):
    r, c, s = map(int, input().split())
    start ,end = (r - s -1, c - s -1), (r + s-1, c + s-1)
    operation.append((start, end, s))

perms = permutations(operation, k)
ans = float('inf')
for perm in perms:
    graph = deepcopy(matrix)
    for rotation in perm:
        start, end, s = rotation
        graph = rot(start, end, s, graph)
    for mat in graph:
        ans = min(sum(mat), ans)
print(ans)
