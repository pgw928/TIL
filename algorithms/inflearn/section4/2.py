import sys
sys.stdin = open('section4/input.txt','rt')
n, m = map(int, input().split())
arr = [int(input()) for _ in  range(n)]

def check(k):
    s = 0
    for x in arr:
        s += x//k
        if s>=m:
            return True
    return False

i, j = 1, max(arr)
res = 1
while i<=j:
    mid = (i+j)//2
    if check(mid):
        res = max(mid, res)
        i = mid + 1
    else:
        j = mid - 1
print(res)