import sys
from math import inf
from itertools import combinations

input = sys.stdin.readline

n , m = map(int, input().split())

graph = [tuple(map(int, input().split())) for _ in range(n)]

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            house.append((i, j))
        elif graph[i][j]==2:
            chicken.append((i, j))
ans = inf
for i in range(1,m+1):
    combs = combinations(chicken, i)
    for comb in combs:
        dist_h = {j: inf for j in range(len(house))}
        for idx, (h1, h2) in enumerate(house):
            for c1, c2 in comb:
                dist_h[idx] = min(abs(c1 - h1) + abs(c2 - h2), dist_h[idx])
        ans = min(ans, sum(dist_h.values()))

print(ans)
