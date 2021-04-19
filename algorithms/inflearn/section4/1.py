import sys
sys.stdin = open('section4/input.txt','rt')
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(arr)
i, j = 0, n-1
while i<=j:
    mid = (i+j)//2
    if arr[mid]==m:
        print(mid+1)
        break
    elif arr[mid]<m:
        i = mid+1
    else:
        j = mid-1