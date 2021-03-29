import sys; input=sys.stdin.readline
from itertools import combinations
l, c = map(int, input().split())

con = {'b','c','d','f','g',
       'h','j','k','l','m',
       'n','p','q','r','s',
       't','v','w','x','y', 'z'}
col = {'a', 'e', 'i', 'o', 'u'}

A, B = [], []
arr = input().rstrip().split()
for alpha in arr:
    if alpha in con:
        A.append(alpha)
    else:
        B.append(alpha)
res = []
for i in range(2, min(l, len(A))+1):
    if len(B) >= l-i and l-i>=1:
        for combs1 in combinations(A, i):
            for combs2 in combinations(B, l-i):
                res.append(''.join(sorted(combs1 + combs2)))

res.sort()
for r in res:
    print(r)