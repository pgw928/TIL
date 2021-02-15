import sys

n = int(sys.stdin.readline())

dp = {1:'CY', 2:'SK', 3:'CY', 4:'SK'}

while True:
    if n in dp:
        print(dp[n])
        break
    else:
        for i in range(5, n+1):
            if dp[i-1]=='CY' and dp[i-3]=='CY':
                dp[i] = 'SK'
            elif ('SK','SK') == (dp[i-1],dp[i-3]):
                dp[i] = 'CY'
            else:
                dp[i] = 'SK'