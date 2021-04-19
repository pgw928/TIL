import sys
sys.stdin = open('section3/input.txt', 'rt')
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

i, j = 0, 0
res = []
while i<=n-1 and j<=m-1:
    if a[i] < b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1
if i==n:
    res += b[j:]
else:
    res += a[i:]
for r in res:
    print(r, end=' ')
