import sys
sys.stdin = open('section3/input.txt', 'rt')
n = int(input())

for _ in range(n):
    st = input().rstrip().lower()
    l = len(st)
    
    if l%2==0:
        left, right = st[:l//2], st[l//2:][::-1]    
    else:
        left, right = st[:l//2], st[l//2+1:][::-1]
    if left == right:
        print('YES')
    else:
        print('NO')