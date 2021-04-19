import sys
from collections import deque
sys.stdin = open('section5/input.txt', 'rt')
n, m = map(int, input().split())
arr = list(map(int, input().split()))
dq = deque([(arr[i],i) for i in range(n)])


cnt = 0
while True:
    x, idx = dq.popleft()    
    if all(x >= y[0] for y in dq):
        cnt += 1
        if m==idx:
            break 
    else:
        dq.append((x, idx))
print(cnt)

