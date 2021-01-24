import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coins = [int(input())  for _ in range(N)]
coins.reverse()
print(coins)

i = 0
score = 0
while True:
    tmp = K//coins[i]
    if tmp > 0:
        score += tmp
        K -= tmp * coins[i]
    else:
        i += 1
    if K==0:
        break
print(score)
