import sys

input = sys.stdin.readline
T = int(input())

def rep(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    return (rep(n-1) + rep(n-2)+ rep(n-3))