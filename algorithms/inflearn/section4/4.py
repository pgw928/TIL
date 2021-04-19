import sys
sys.stdin = open('section4/input.txt', 'rt')
n, m = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])

def check(k):
    i = 0
    cnt = 1
    for j in range(n):
        if arr[j] - arr[i] >= mid:
            cnt += 1
            i = j
    if cnt >= m:
        return True
    return False


lt, rt = 0, arr[-1]
res = 0
while lt<=rt:
    mid = (lt+rt)//2
    if check(mid):
        res = max(res, mid)
        lt = mid + 1
    else:
        rt = mid - 1
print(res)