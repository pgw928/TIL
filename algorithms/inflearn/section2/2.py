import sys
sys.stdin = open('section2/input.txt', 'rt')
t = int(input())
for _ in range(t):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    res = sorted(arr[s-1:e])
    print(res[k-1])
    