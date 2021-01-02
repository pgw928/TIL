import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

stack = deque()
visited = []
pointer = 1
result = ['+']
temp = [int(input()) for _ in range(n)]
stack.append(1)

for i in range(n):
    current = temp[i]

    for j in range(pointer+1,current+1):
        stack.append(j)
        result.append('+')
    pointer = max(current, pointer)
    visited.append(stack.pop())
    result.append('-')

if visited!= temp:
    print('NO')
else:
    for op in result:
        print(op)
