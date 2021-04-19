import sys
sys.stdin = open('section3/input.txt', 'rt')

arr = list(range(21))
for _ in range(10):
    i, j = map(int, input().split())
    arr[i:j+1] = arr[i:j+1][::-1]
print(' '.join(list(map(str, arr[1:]))))