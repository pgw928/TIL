import sys
sys.stdin = open('section5/input.txt', 'rt')
a = input().rstrip()

stack = []
res = ''
for x in a:
    if x.isnumeric():
        res += x
    elif x=='*' or x=='/':
        while stack and (stack[-1]=='*' or stack[-1]=='/'):
            res += stack.pop()
        stack.append(x)
    elif x=='+' or x=='-':
        while stack and (stack[-1]=='+' or stack[-1]=='-' or stack[-1]=='*' or stack[-1]=='/') :
            res += stack.pop()
        stack.append(x)
    elif x=='(':
        stack.append(x)
    elif x==')':
        while stack[-1]!='(':
            res += stack.pop()
        stack.pop()
    print(res, stack)
while stack:
    res += stack.pop()
print(res)