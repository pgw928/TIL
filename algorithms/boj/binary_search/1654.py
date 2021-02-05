import sys
input = sys.stdin.readline

n,m = map(int, input().split())
A = sorted([int(input()) for _ in range(n)])

def binary_search(A, m):

    start = 0
    end = sum(A)//m
    result = 0
    while start <= end:
        mid = (start+end)//2
        if mid==0:
            start+=1
            continue
        s = sum([a//mid for a in A])
        if s >= m:
            result = max(result, mid)
            start = mid+1
        elif s < m:
            end = mid-1
    return result

print(binary_search(A, m))