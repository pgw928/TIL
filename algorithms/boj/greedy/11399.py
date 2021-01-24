import sys

input = sys.stdin.readline

n = int(input())
P = list(map(int, input().split()))
P.sort()

score = 0
current = 0
for i in range(n):
    current += P[i]
    score += current

print(score)