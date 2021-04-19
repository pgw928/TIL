import sys
# sys.stdin = open('section2/input.txt', 'rt')
n, k = map(int, input().split())

# n , k = 6, 3
res = -1
cnt = 1
for i in range(2, n//2+1):
    if n%i==0:
        cnt += 1
        if cnt==k:
            res = i
            break
print(res)