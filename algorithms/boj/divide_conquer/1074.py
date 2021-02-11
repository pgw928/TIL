import sys

N, r, c = map(int, sys.stdin.readline().split())

def recursion(N, r, c):

    if N == 1:
        if r == 0 and c == 0: return 0
        if r == 0 and c == 1: return 1
        if r == 1 and c == 0: return 2
        if r == 1 and c == 1: return 3

    if r < 2**(N-1) and c < 2**(N-1):
        return recursion(N-1, r, c)
    if r < 2**(N-1) and c >= 2**(N-1):
        return 2**(N)*2**(N)//4 + recursion(N-1, r, c-2**(N-1))
    if r >= 2 **(N-1) and c < 2**(N-1):
        return 2**(N)*2**(N)//2 + recursion(N-1, r-2**(N-1), c)
    if r >= 2 ** (N - 1) and c >= 2 ** (N - 1):
        return 3*2**(N)*2**(N)//4 + recursion(N-1, r-2**(N-1), c-2**(N-1))

print(recursion(N, r, c))