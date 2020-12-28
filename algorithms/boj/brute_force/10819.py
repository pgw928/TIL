import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

M = 0
for perm in permutations(A):
    tmp = [ abs(perm[i+1]-perm[i]) for i in range(len(perm)-1)]
    M = max(sum(tmp), M)
print(M)
