import sys; input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(map(int, input().split()))

def check(k):
    cnt = 1
    tmp = 0
    for i in range(n):
        if arr[i] > k:
            return False
        elif arr[i] + tmp <= k:
            tmp += arr[i]
        elif arr[i] + tmp > k:
            cnt += 1
            tmp = arr[i]
        if cnt > m:
            return False
    return True

i, j = 1, sum(arr)
while i<=j:
    mid = (i+j)//2

    if check(mid):
        res = mid
        j = mid-1
    else:
        i = mid+1
print(res)