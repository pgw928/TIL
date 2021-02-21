import sys

n, r = map(int, sys.stdin.readline().split())

def div(n,d):
    count = 0
    while n!=0:
        n//=d
        count += n
    return count

print(min(div(n,2)-div(n-r,2)-div(r,2),
          div(n,5)-div(n-r,5)-div(r,5)))