import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

A = list(map(int, input().split()))
count = sorted(list(Counter(A).items()), key=lambda x: x[0],reverse= True)

dic = {a : len(count)-idx-1 for idx, (a, b) in enumerate(count)}
result = [dic[a] for a in A]
print(' '.join(map(str, result)))
