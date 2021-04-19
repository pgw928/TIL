import sys
sys.stdin = open('section5/input.txt', 'rt')
a = input().rstrip()

stack = []

for i in range(len(a)):
    if a[i].isnumeric():
        stack.append(int(a[i]))
    elif a[i]=='+':
        x = stack.pop()
        y = stack.pop()
        stack.append(x + y)
    elif a[i]=='*':
        x = stack.pop()
        y = stack.pop()
        stack.append(x * y)
    elif a[i]=='-':
        x = stack.pop()
        y = stack.pop()
        stack.append(y - x)
    elif a[i]=='/':
        x = stack.pop()
        y = stack.pop()
        stack.append(y // x)
    print(stack)
print(stack)