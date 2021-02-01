import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    a = int(input())
    b = int(input())
    result = 1
    for i in range(1, a+2):
        result *= (b+i-1)
        result //= i
    print(result)