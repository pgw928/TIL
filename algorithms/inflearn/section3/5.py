import sys
sys.stdin = open('section3/input.txt', 'rt')
n, m = map(int, input().split())
arr = list(map(int, input().split()))
i, j  = 0, 1
current = arr[i]
cnt = 0 

while True:
    if current==m:
        current -= arr[i]
        i += 1
        cnt += 1
    elif current < m:
        if j<n:
            current += arr[j]
            j += 1
        else:
            break
    else:
        current -= arr[i]
        i += 1
    
print(cnt)