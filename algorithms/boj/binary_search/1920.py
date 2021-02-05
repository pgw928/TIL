import sys
input = sys.stdin.readline

n = int(input())
A = sorted(list(map(int, input().split())))
m = int(input())
B = list(map(int, input().split()))

def binary_search(A,x):
    start = 0
    end = len(A)-1
    while start <= end:
        mid = (start+end)//2

        if A[mid] == x:
            return 1
        elif A[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in range(m):
    print(binary_search(A,B[i]))

