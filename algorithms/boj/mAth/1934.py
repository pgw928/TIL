import sys; input = sys.stdin.readline
t = int(input())
def gcd(a, b):
    if a > b:
        a, b = b, a
    while True:
        q, r = divmod(b, a)
        if r == 0:
            return a
        b, a = a, r
for _ in range(t):
    a, b = map(int, input().split())
    print(a*b//gcd(a, b))