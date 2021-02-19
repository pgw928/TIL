import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def sol(fun, arr):
    count = 0
    for s in fun:
        if s == 'D':
            if not arr:
                return 'error'
            if count%2==0:
                arr.popleft()
            else:
                arr.pop()

        elif s == 'R':
            count += 1
    if count%2==0:
        return  '[' + ','.join(list(map(str, arr))) + ']'
    return '[' + ','.join(list(map(str, reversed(arr)))) + ']'

for _ in range(t):
    fun = input().strip()
    n = int(input())
    if n>=1:
        arr = deque(list(map(int, input().strip()[1:-1].split(','))))
    else:
        input()
        arr = deque()
    print(sol(fun, arr))