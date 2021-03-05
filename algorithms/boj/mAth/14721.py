import sys
from math import inf
input = sys.stdin.readline

n = int(input())

X, Y = [], []
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)


def rss(u, v):
    return sum([(u*x+v-y)**2 for x, y in zip(X, Y)])
res = inf
for k in range(1, 101):
    for s in range(1, 101):
        tmp = rss(k, s)
        if tmp < res:
            res = tmp
            a_b = [k, s]

print(a_b[0], a_b[1])