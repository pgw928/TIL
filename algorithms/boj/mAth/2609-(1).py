import sys

a, b = map(int, sys.stdin.readline().split())
a, b = min(a,b), max(a,b)

def gcd(x, y):

    if y%x == 0:
        return x
    return gcd(y%x ,x)


res = gcd(a, b)
print(res)
print(int(a*b/res))


