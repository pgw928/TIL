import sys
from math import sqrt
n = int(sys.stdin.readline())
a = int(sqrt(n))
while True:
    if a*a >= n:
        print(a)
        break
    a += 1
