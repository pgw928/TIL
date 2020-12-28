import sys
from itertools import combinations

input = sys.stdin.readline

N ,S = map(int, input().split())

arr = list(map(int, input().split()))

count = 0

for i in range(1,N+1):
    for comb in combinations(arr,i):
        if S == sum(comb):
            count += 1
print(count)