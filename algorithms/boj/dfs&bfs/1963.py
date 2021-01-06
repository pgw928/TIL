# 소수 경로

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())


def isprime(p):
    if p%2==0:
        return False
    if p==2:
        return True
    i = 3
    m = int ( p**(1/2))
    for i in range(3,m+1):
        if p%i==0:
            return False
    return True
# primes = []
# for p in range(1001, 10000,2):
#     if isprime(p):
#         primes.append(p)
# print(primes)
# print(len(primes))

def make_nums(p):
    result = []
    s_p = str(p)

    for i in (set(range(1,10,2))-{int(s_p[3])}):
        new = int(s_p[0:3] + str(i))
        if isprime(new):
            result.append(new)

    for i in (set(range(0,10,1))-{int(s_p[2])}):
        new = int(s_p[0:2] + str(i) + s_p[3])
        if isprime(new):
            result.append(new)

    for i in (set(range(0,10,1))-{int(s_p[1])}):
        new = int(s_p[0] + str(i) + s_p[2:4])
        if isprime(new):
            result.append(new)

    for i in (set(range(1,10,1))-{int(s_p[1])}):
        new = int(str(i) + s_p[1:4])
        if isprime(new):
            result.append(new)

    return result

def bfs(start_node, end_node):
    visited = [0] * (10001)
    dq = deque()
    dq.append(start_node)
    visited[start_node] = 1
    while dq:
        node = dq.popleft()
        if node == end_node:
            return visited[end_node]-1
        for n_node in make_nums(node):
            if visited[n_node]==0:
                visited[n_node] = visited[node] +1
                dq.append(n_node)
    return 'Impossible'

for _ in range(T):
    A, B = map(int, input().split())
    print(A,B)
    print(bfs(A,B))

