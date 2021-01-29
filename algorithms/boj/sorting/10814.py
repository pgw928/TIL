import sys
input = sys.stdin.readline
n= int(input())
for a,b in sorted([sys.stdin.readline().strip().split() for _ in range(n)], key=lambda x:int(x[0])):
    print(a,b)