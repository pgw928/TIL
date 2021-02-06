import sys

n= int(sys.stdin.readline())

dp = {1:'SK', 2: 'CY', 3:'SK', 4:'CY'}

def sol(k):
    if k in dp:
        return dp[k]
    else:
        for i in range(5, k+1):
            if dp[i-3]=='SK' or dp[i-1]=='SK':
                dp[i] = 'CY'
            else:
                dp[i] = 'SK'
        return dp[k]

print(sol(n))
