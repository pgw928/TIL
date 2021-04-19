import sys
sys.stdin = open('section5/input.txt', 'rt')
arr = input().rstrip().replace('()', '0')
print(arr)
stack = []
res = 0
for s in arr:
    if s=='0':
       res += len(stack)
    elif s=='(':
        stack.append('(')
    elif s==')':
        stack.pop()
        res += 1
print(res)

