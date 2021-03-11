import sys; input = sys.stdin.readline
n, s = map(int, input().split())
A = sorted([ int(input()) for _ in range(n)])
i, j = 0, n-1
r = 0
while i<j:
    if A[i]+A[j] <= s:
        r += j -i
        i += 1
    else:
        j -= 1

print(r)