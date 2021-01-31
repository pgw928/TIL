import sys
from collections import Counter

input = sys.stdin.readline
n =int(input())

A = sorted([int(input()) for _ in range(n)])

# 평균
print(int(round(sum(A)/n, 0)))

# 중앙값
print(A[n//2])
c = Counter(A)

# 최빈값
tmp = sorted(list(c.items()), key=lambda x:(x[1],-x[0]), reverse=True)
if len(tmp)==1:
    print(tmp[0][0])
else:
    if tmp[0][1] == tmp[1][1]:
        print(tmp[1][0])
    else:
        print(tmp[0][0])

# 범위
print(A[-1]-A[0])