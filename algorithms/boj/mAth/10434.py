import sys

input = sys.stdin.readline

t = int(input())

def is_prime(n):
    if n==1:
        return False
    i = 2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

def is_happy(n):
    check = set()
    check.add(n)
    while True:
        A = str(n)
        s = 0
        for a in A:
            s += int(a)*int(a)
        if s==1:
            return True
        if s in check:
            return False
        n = s
        check.add(s)



def sol(b):
    if is_prime(b) and is_happy(b):
        return 'YES'
    return 'NO'



for _ in range(t):
    a, b = map(int, input().split())
    c = sol(b)
    print(a, b, c)