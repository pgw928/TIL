import sys

input = sys.stdin.readline
t = int(input())

def isprime(k):

    if k==0 or k==1:
        return False
    i = 2
    while i*i<=k:
        if k%i==0:
            return False
        i+=1
    return True


for _ in range(t):
    n = int(input())
    while True:
        if isprime(n):
            print(n)
            break
        n+=1
