import sys
import heapq
input = sys.stdin.readline
n = int(input())
A = []
for _ in range(n):
    k = int(input())
    if k==0:
        if not A:
            print(0)
        else:
            tmp = heapq.heappop(A)
            print(tmp[0]*tmp[1])
    else:
        if k < 0:
            heapq.heappush(A,(-k,-1))
        else:
            heapq.heappush(A,(k,1))
