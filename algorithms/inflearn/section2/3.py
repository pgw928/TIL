import sys
sys.stdin = open('section2/input.txt', 'rt')
n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = set()
for i in range(n-2):
    for j in range(i+1, n-1):
        for l in range(j+1, n):
            res.add(arr[i] + arr[j] + arr[l])
print(sorted(list(res), reverse=True)[k-1])