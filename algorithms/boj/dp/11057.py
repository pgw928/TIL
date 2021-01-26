import sys

n = int(sys.stdin.readline())

score = 1
for i in range(0,n):
    score *= (10+i)
    score //= (i+1)

print(score%10007)