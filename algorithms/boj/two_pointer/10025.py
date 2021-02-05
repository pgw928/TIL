import sys
input = sys.stdin.readline
N, K = map(int, input().split())

A = sorted([tuple(map(int, input().split()))  for _ in range(N)], key=lambda x: x[1])

m = 0
i = A[0][1]+2
j = A[-1][1]-2
while i<j:

    temp1 = sum([a for a, b in A if abs(b-i)<=3])
    temp2 = sum([a for a, b in A if abs(b-j) <= 3])
    m = max(temp1, temp2, m)
    i+=1
    j-=1

print(m)

