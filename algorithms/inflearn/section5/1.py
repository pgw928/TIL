import sys
sys.stdin = open('section5/input.txt', 'rt')
n, m = map(int, input().split())
arr = list(map(int, list(str(n))))
l = len(arr)

i, k = 0, 0
stack = []
while i<l:
    if stack and (k < m) and (stack[-1] < arr[i]):
        stack.pop()
        k += 1
    else:
        stack.append(arr[i])
        i += 1
    
for s in stack[:l-m]:
    print(s, end='')
