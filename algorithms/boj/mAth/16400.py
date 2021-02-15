import sys
import math

n = int(sys.stdin.readline())


def is_prime_number(n):
    array = [True for _ in range(n+1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [ i for i in range(2, n+1) if array[i] ]

money = is_prime_number(n)
print(money)
dp = [0]*(n+1)
dp[0] = 1
for i in money[1:]:
    for j in range(i,n+1):
        dp[j] += dp[j-i]

print(dp[-1]%123456789)