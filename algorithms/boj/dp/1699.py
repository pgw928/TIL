import sys; input = sys.stdin.readline
n = int(input())
dp = [float('inf')]*(n+1)
dp[1] = 1
for i in range(2,n+1):
    if i**(1/2)== int(i**(1/2)):
        dp[i] = 1
    else:
        k = 1
        while k**2 <= i:
            dp[i] = min(dp[i], dp[k**2]+dp[i-k**2])
            k += 1

print(dp[n])