import sys

n= int(sys.stdin.readline())

dp = {1:'SK', 2: 'CY', 3:'SK', 4:'SK', 5:'SK',6:'SK'}

def sol(k):
    if k in dp:
        return dp[k]
    else:
        for i in range(7, k+1):
            if dp[i-3]=='SK' and dp[i-1]=='SK' and dp[i-4]=='SK':
                dp[i] = 'CY'
            else:
                dp[i] = 'SK'
        return dp[k]

print(sol(n))
