import sys
input = sys.stdin.readline

n = int(input())
h_w = [list(map(int, input().split())) for _ in range(n)]
count = [0]*n
for i in range(len(h_w)-1):
    a, b = h_w[i]
    for j in range(i+1,len(h_w)):
        c, d = h_w[j]
        if a>c and b>d:
            count[i] += 1
        elif a<c and b<d:
            count[j] += 1
print(count)
rank = [0]*n
k = 1
tmp = 0
while True:
    M = max([c for r,c in zip(rank, count) if r==0], default=-1)
    score = 0
    if M==-1:
        break
    for i in range(len(count)):
        if count[i] == M:
            rank[i] = k
            score += 1
    k += score


print(rank)
