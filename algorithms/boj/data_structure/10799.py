import sys

input = sys.stdin.readline()
print(input)

stack = []
i = 0
l = len(input)
count = 0
while True:
    if input[i:i+2]=='()':
        count += len(stack)
        i += 2
        print(count)
    elif input[i] == ')':
        stack.pop()
        count += 1
        i += 1
        print(count)
    else:
        stack.append(input[i])
        i += 1
    if i>=l-1:
        break

print(count)