import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

dq = deque(range(1,N+1))

result = []
while dq:
    dq.rotate(-(K-1))
    result.append(dq.popleft())

print('<'+ ', '.join(map(lambda x: str(x), result)) + '>')