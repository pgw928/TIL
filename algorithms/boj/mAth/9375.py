import sys; input = sys.stdin.readline
from itertools import combinations
t = int(input())

for _ in range(t):
    n = int(input())
    dic = {}
    for _ in range(n):
        a, b = input().strip().split()
        dic[b] = dic.get(b, 0) + 1
    res = 1
    for d in dic:
        res *= (dic[d]+1)
    res -= 1
    print(res)
