import sys

input = sys.stdin.readline
n = int(input())

for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
for i in range(2, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
