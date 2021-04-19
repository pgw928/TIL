import sys
sys.stdin = open('section4/input.txt', 'rt')
n , m = map(int, input().split())
arr = list(map(int, input().split()))

def check(k):
    idx = 0
    for i in range(m):
        cnt = 0
        for j in range(idx, n):
            if cnt + arr[j] <= k:
                cnt += arr[j]
            elif i<m-1:
                idx = j
                break  
            else:
                return False
    return True        



lt, rt = 1, sum(arr)
res = float('inf')
while lt<=rt:
    mid = (lt+rt)//2
    if check(mid):
        rt = mid -1
        res = min(mid, res)    
    else:
        lt = mid + 1
print(res)