import sys
from itertools import combinations

input = sys.stdin.readline

heights = [ int(input()) for _ in range(9)]

print(heights)

for hs in combinations(heights,7):
    print(hs)
    if sum(hs) == 100:
        hs = list(hs)
        hs.sort()
        for h in hs:
            print(h)
        break