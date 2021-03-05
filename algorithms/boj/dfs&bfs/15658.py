import sys
from math import inf
from itertools import permutations

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

plus, minus, prod, divi = map(int, input().split())
operator = {0:plus, 1:minus, 2:prod, 3:divi}
M, m = -inf, inf

def dfs(res, start):
    global M, m
    if start == n-1:
        M, m = max(res, M), min(res, m)
        return
    for i in range(4):
        if i == 0 and operator[i]>0:
            operator[i] -= 1
            dfs(res+A[start+1], start+1)
            operator[i] += 1
        elif i == 1 and operator[i]>0:
            operator[i] -= 1
            dfs(res - A[start + 1], start + 1)
            operator[i] += 1
        elif i == 2 and operator[i]> 0:
            operator[i] -= 1
            dfs(res * A[start + 1], start + 1)
            operator[i] += 1
        elif i == 3 and operator[i]> 0:
            operator[i] -= 1
            if res<0:
                dfs(-((-res) // A[start + 1]), start + 1)
            else:
                dfs(res // A[start + 1], start + 1)
            operator[i] += 1
    return

dfs(A[0], 0)
print(M)
print(m)