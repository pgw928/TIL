import sys; input = sys.stdin.readline
import heapq
n = int(input())
topn = list(map(int, input().split()))
heapq.heapify(topn)
for _ in range(n-1):
    for a in list(map(int, input().split())):
        heapq.heappush(topn, a)
        heapq.heappop(topn)
print(heapq.heappop(topn))
