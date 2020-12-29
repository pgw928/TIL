import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())

dq = deque()
dq.extend(range(1,N+1))
res = []
while dq:
    for _ in range(K-1):
        dq.rotate(-1)
    res.append(dq.popleft())
result ='<' + ', '.join(map(lambda x: str(x), res)) + '>'
print(result)
