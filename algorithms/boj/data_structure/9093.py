import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = input().split()
    result = ''
    for i, w in enumerate(s):
        result += w[::-1]+' '
    print(result.strip())