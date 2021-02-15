import sys
from collections import deque
n = int(sys.stdin.readline())

check = {}
def bfs(start):
    dq = deque()
    dq.append(start)

    while dq:
        x = dq.popleft()
        if x>=2:
            if x%3 == 0 and x//3 not in check:
                check[x//3] = x
                dq.append(x//3)
            if x%2 == 0 and x//2 not in check:
                check[x//2] = x
                dq.append(x//2)
            if x-1 not in check:
                check[x-1] = x
                dq.append(x-1)
    result = [1]
    while result[-1]!=start:
        result.append(check[result[-1]])
    return result



result = bfs(n)
print(len(result)-1)
print(' '.join(map(str, result[::-1])))
