import sys

a, b = map(int, sys.stdin.readline().split())
a, b = min(a,b), max(a,b)

def gcd(x, y):

    for i in range(x,0,-1):
        if (x%i==0) and (y%i==0):
            return i


res = gcd(a, b)
print(res)
print(int(a*b/res))


