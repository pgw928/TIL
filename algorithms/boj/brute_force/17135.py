import sys; input = sys.stdin.readline
from itertools import combinations
from copy import deepcopy
n, m, d = map(int, input().split())
enemy = []
for i in range(n):
    tmp = tuple(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 1:
            enemy.append((i, j))
combs = combinations([(n, i) for i in range(m)], 3)
M = 0
for comb in combs:
    d_enemy = deepcopy(enemy)
    count = 0
    while d_enemy:
        candi = set()
        for a,b in comb:
            tmp = [(x,y) for x,y in d_enemy if abs(x-a)+abs(y-b)<=d ]
            if tmp:
                kill = sorted(tmp, key=lambda x: (abs(x[0]-a)+abs(x[1]-b), x[1]))[0]
                candi.add(kill)
        count += len(candi)
        d_enemy = list(set(d_enemy) - candi)
        t_enemy = []
        for _ in range(len(d_enemy)):
            (x, y) = d_enemy.pop()
            if x+1 < n:
                t_enemy.append((x+1, y))
        d_enemy = deepcopy(t_enemy)
    M = max(M, count)
print(M)