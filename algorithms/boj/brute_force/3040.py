import sys
from itertools import combinations

A = []
for _ in range(9):
    A.append(int(sys.stdin.readline()))

comb = combinations(A, 7)
for a in comb:
    if sum(a) == 100:
        result = a
        break
for a in result:
    print(a)