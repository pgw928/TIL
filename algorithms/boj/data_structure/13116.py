import sys

input = sys.stdin.readline

T = int(input())

def solution():
    n, m = map(int, input().split())
    while n!=m:
        if n < m:
            m //= 2
        else:
            n //= 2
    return 10*n
for _ in range(T):
    print(solution())
