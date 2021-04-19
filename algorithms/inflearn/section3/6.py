import sys
sys.stdin = open('section3/input.txt', 'rt')
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
M = 0
for g in graph:
    tmp = sum(g)
    if tmp > M:
        M = tmp
for i in range(n):
    tmp = sum([graph[j][i] for j in range(n)])
    if tmp > M:
        M = tmp

tmp = sum([graph[j][j] for j in range(n)])
if tmp > M:
    M = tmp
tmp = sum([graph[n-1-j][j] for j in range(n)])
if tmp > M:
    M = tmp
print(M)