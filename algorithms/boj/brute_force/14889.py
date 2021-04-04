import sys; input = sys.stdin.readline
from itertools import combinations
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

combs = combinations(range(n), n//2)
m = float('inf')
for comb in combs:
    cnt1, cnt2 = 0, 0
    for idx, i in enumerate(comb[:-1]):
        for j in comb[idx+1:]:
            cnt1 += (graph[i][j]+graph[j][i])
    rem = list(set(range(n))-set(comb))
    for idx, i in enumerate(rem[:-1]):
        for j in rem[idx+1:]:
            cnt2 += (graph[i][j]+graph[j][i])
    m = min(m, abs(cnt1-cnt2))
print(m)
