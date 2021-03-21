import sys; input = sys.stdin.readline
n , m = int(input()), int(input())
s = input().strip()
rel = 'IO'*n + 'I'
count = 0
i = 0
while i <= m-1 - 2*n:
    if s[i:i+2*n+1]==rel:
        count += 1
        i += 2
    else:
        i+=1
print(count)