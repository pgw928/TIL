import sys; input = sys.stdin.readline
n, m = map(int, input().split())
A = tuple(map(int, input().split()))
i = 0
j = 1
c = A[i]
count = 0
while True:
    if j<=n-1:
        print(i, j, c, count)

        if c == m:
            count += 1
            c += A[j]
            j += 1
        elif c > m:
            c -= A[i]
            i += 1
        else:
            c += A[j]
            j += 1
    elif j==n:
        print(i, j, c, count)
        if c==m:
            count += 1
            break

        elif c>m:
            c -= A[i]
            i += 1
        elif c < m:
            break

print(count)