import sys; input = sys.stdin.readline
n = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x: (x[1],x[0]))

print(arr)

start = 0
result = 0
for a, b in arr:
    if a >= start:
        start = b
        result += 1

print(result)