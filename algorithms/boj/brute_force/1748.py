import sys

input = sys.stdin.readline

def sol():
    N = input().strip()
    l_N = len(N)
    N = int(N)
    return sum(map(lambda x: 10**(x-1)*9*x, range(1, l_N))) + (N-10**(l_N-1)+1)*l_N

print(sol())

