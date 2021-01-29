import sys
from collections import Counter
input = sys.stdin.readline
n= int(input())
A = map(int, sys.stdin.readline().split())

m = int(input())
B = map(int, sys.stdin.readline().split())

C = Counter(A)
' '.join(map(str, [C.get(b,0) for b in B]))