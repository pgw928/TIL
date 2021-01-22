import sys

input = sys.stdin.readline
T = int(input())

memo = {1:1, 2:2, 3:4}

def rep(n):
    if memo.get(n):
        return memo[n]
    memo[n] =  rep(n-3) + rep(n-2) + rep(n-1)
    return memo[n]

for _ in range(T):
    n = int(input())
    print(rep(n))

