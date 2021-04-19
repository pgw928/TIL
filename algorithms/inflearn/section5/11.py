import sys
from heapq import heappop, heappush
sys.stdin = open('section5/input.txt', 'rt')
hp = []
while True:
    n = int(input())
    if n==-1:
        break
    if n==0:
        if not hp:
            print(-1)
        else:
            print(-heappop(hp))
    else:
        heappush(hp, -n)
