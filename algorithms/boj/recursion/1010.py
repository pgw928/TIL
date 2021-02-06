import sys

input = sys.stdin.readline


# we want to comute  combination of a and b
dp = {}
def sol(b, a):

    if a==0:
        return 1
    if a==1:
        return b

    return sol(b,a-1) * (b-a+1)//a



t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(sol(b, a))

