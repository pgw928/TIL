import sys; input = sys.stdin.readline
from heapq import heappop, heappush
n = int(input())

hp1= []

k = int(input())
print(k)
hp2 = [k]
for j in range(2, n+1):
    if j%2==0:
        heappush(hp1, -int(input()))
    else:
        heappush(hp2, int(input()))
    a = -heappop(hp1)
    b = heappop(hp2)

    if j%2==0:
        if a <= b:
            print(a)
            heappush(hp1, -a)
            heappush(hp2, b)
        else:
            print(b)
            heappush(hp1, -b)
            heappush(hp2, a)
    else:
        if a <= b:
            print(b)
            heappush(hp1, -a)
            heappush(hp2, b)
        else:
            print(a)
            heappush(hp1, -b)
            heappush(hp2, a)
