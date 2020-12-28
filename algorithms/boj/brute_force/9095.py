import sys

input = sys.stdin.readline
T = int(input())

memo = {1:1, 2:2, 3:4}

def rep(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    if n not in memo:
        memo[n] =  rep(n-3) + rep(n-2) + rep(n-1)
    return memo[n]


for _ in range(T):
    n = int(input())
    print(memo)
    print(rep(n))