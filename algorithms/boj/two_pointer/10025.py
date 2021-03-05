import sys
input = sys.stdin.readline
n, k = map(int, input().split())

A = [tuple(map(int, input().split()))  for _ in range(n)]
check = [0]*1000001
for a, b in A:
    check[b] = a
l = max([b for a,b in A])
i, j = k, l-k
tmp1, tmp2 = sum(check[i-k:i+k+1]), sum(check[j-k:j+k+1])
M = max(tmp1, tmp2)
while i<j and i+k+1<=l and j-k>=0:
    i+=1
    j-=1
    tmp1 += (check[i+k] - check[i-1-k])
    tmp2 += (check[j-k] - check[j+k+1])
    M = max(M, tmp1, tmp2)

print(M)

