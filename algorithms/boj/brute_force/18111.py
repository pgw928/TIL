import sys
from math import inf
input = sys.stdin.readline
n, m, b = map(int, input().split())


vals = dict()
for i in range(n):
    tmp = tuple(map(int, input().split()))
    for j in range(m):
        num = vals.get(tmp[j], 0)
        vals[tmp[j]] = num+1

time, height = [], []
for v in range(257):
    M, inven = 0, b
    for val, c in vals.items():
        if v - val>0:
            M += (v - val)*c
            inven -= (v - val)*c
        elif val - v > 0:
            M += 2 * (val - v)*c
            inven += (val - v)*c
    if inven < 0:continue
    time.append(M)
    height.append(v)

t_m, h_M = inf, 0
for t, h in zip(time, height):
    if t < t_m:
        t_m, h_M = t, h
    elif (t == t_m) and (h > h_M):
        h_M = h
print(t_m, h_M)