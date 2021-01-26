import sys

n = int(sys.stdin.readline())

memo = {0:1, 1:1}

for i in range(2, n+1):
    memo[i] = memo[i-1] + memo[i-2]

print(memo[n]%10007)
