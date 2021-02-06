import sys

input = sys.stdin.readline

a = int(input())
b = int(input())


def isprime(n):

    if n==1:
        return False
    i = 2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

s = 0
flag = True
for n in range(a,b+1):
    if isprime(n):
        s += n
        if flag:
            m = n
            flag = False

if s!=0:
    print(s)
    print(m)
else:
    print(-1)