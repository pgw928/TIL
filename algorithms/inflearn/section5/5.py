import sys
from collections import deque
sys.stdin = open('section5/input.txt', 'rt')
n, k = map(int, input().split())
dq = deque(range(1, n+1))
while dq:
    dq.rotate(-(k-1))
    x = dq.popleft()
print(x)

