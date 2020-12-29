import sys
from itertools import combinations as comb


input = sys.stdin.readline

N, S = map(int, input().split())

A = list(map(int, input().split()))

count = 0
for i in range(2,len(A)+1):
    for c in comb(A,i):
        if sum(c)==0:
            count+=1

print(count)