import sys; input = sys.stdin.readline
from itertools import permutations
n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
for perm in permutations(arr, n):
    ct_pt = False
    curr = 500
    for a in perm:
        if curr+a-k < 500:
            ct_pt = True
            break
        curr += a - k
    if ct_pt:
        continue
    count += 1
print(count)