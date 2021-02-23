import sys
input = sys.stdin.readline

def sol(string):
    stack = []
    for s in string:
        if s == '(' :
            stack.append(s)
        elif s == '[':
            stack.append(s)
        elif s==')':
            if not stack:
                return 'no'
            tmp = stack.pop()
            if tmp != '(':
                return 'no'
        elif s==']':
            if not stack:
                return 'no'
            tmp = stack.pop()
            if tmp != '[':
                return 'no'
    if stack:
        return 'no'
    return 'yes'

while True:
    string = input().rstrip()
    if string=='.':
        break
    print(sol(string.replace(' ', '')))