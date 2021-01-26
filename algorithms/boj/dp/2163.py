import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    sticker = [tuple(map(int, input().split())) for _ in range(2)]
    memo = {0:(0,0) ,1:(sticker[0][0], sticker[1][0])}

    for i in range(2, n+1):
        memo[i] = (max(memo[i-1][1], memo[i-2][1]) + sticker[0][i-1] , max(memo[i-1][0],memo[i-2][0]) + sticker[1][i-1] )
    print(max(memo[n]))
