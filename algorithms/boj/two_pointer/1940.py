import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
A = sorted(list(map(int, input().split())))

i, j = 0, len(A)-1

count = 0
while i<j:

    tmp = A[i] + A[j]
    print(i,j)
    if tmp == m:
        count += 1
        i += 1
        j -= 1
    elif tmp > m:
        j -= 1
    else:
        i += 1

print(count)




