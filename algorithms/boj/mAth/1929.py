import sys


def isprime(n):

    if n==1:
        return False

    i= 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

a, b = map(int, sys.stdin.readline().split())

for i in range(a,b+1):
    if isprime(i):
        print(i)