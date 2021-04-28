import sys; input = sys.stdin.readline
from collections import deque
n, k = map(int, input().split())

a = (input().rstrip())

res = ''
s = 1
stack = []
for i in range(n):
    if k>0:
        if res + a[i+1:] > res + a[i:-1]:
            stack.append(i)
            k -= 1
        else:
            res += (a[0])
            a = a[i:]

print(res)
