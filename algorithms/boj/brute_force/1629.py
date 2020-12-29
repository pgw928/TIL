import sys

A, B, C = map(int, sys.stdin.readline().split())
def pow_custom(a, b, c):
    ret = 1
    while b :
        if b%2 == 1:
            ret *= a
            ret %= c
        a = a*a%c
        b //= 2
        print('b : ',b, ', a :',a, ', ret :', ret)
    return ret

print(pow_custom(A, B, C))